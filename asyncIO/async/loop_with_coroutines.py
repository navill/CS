# fetch method is a coroutine
# which means that STACK MANAGEMENT of fetch() is AUTOMATIC 
# as that of THREAD is

# and TASK MANAGEMENT of fetch() is COOPERATIVE
# as that of EVENT-DRIVEN is

# Consider that


#            automatic               COROUTINE      MULTITHREADED
# management
#            manual                 EVENT-DRIVEN 
#                         serial     cooperative     preemptive

import socket
from bs4 import BeautifulSoup
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ
import sys

selector=DefaultSelector()
host=sys.argv[1]

class Future:
	def __init__(self):
		self.result=None
		self._callbacks=[]
	
	def add_done_callback(self, fn):
		self._callbacks.append(fn)

	def set_result(self, result):
		self.result=result
		for fn in self._callbacks:
			fn(self)

	def __iter__(self):
		yield self
		return self.result

def read(sock):
	f=Future()

	def on_readable():
		f.set_result(sock.recv(4096))

	selector.register(sock.fileno(), EVENT_READ, on_readable)
	chunk=yield from f
	selector.unregister(sock.fileno())
	return chunk

def read_all(sock):
	response=[]
	chunk=yield from read(sock)
	while chunk:
		response.append(chunk)
		chunk=yield from read(sock)
	return b''.join(response)

class Fetcher:
	def fetch(self, url):
		response=b''
		sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.setblocking(False)
		try:
			sock.connect((host, 80))
		except BlockingIOError:
			pass

		f=Future()
		
		def on_connected():
			f.set_result(None)

		selector.register(sock.fileno(), EVENT_WRITE, on_connected)

		yield from  f

		selector.unregister(sock.fileno())
		print('connected')

		request='GET {} HTTP/1.1\r\nHost: {}\r\nConnection: close\r\n\r\n'.format(url, host)
		sock.sendall(request.encode())
		
		response=yield from read_all(sock)
		"""	
		while True:
			f=Future()

			def on_readable():
				f.set_result(sock.recv(4096))

			selector.register(sock.fileno(), EVENT_READ, on_readable)

			chunk=yield f
			selector.unregister(sock.fileno())
			if chunk:
				response+=chunk
			else:
				break
		"""
		self.print_html(response)
		return 'done'

	def print_html(self, response):
		soup=BeautifulSoup(response, 'html.parser')
		print(soup.prettify())

class Task:
	def __init__(self, coro):
		self.coro=coro
		f=Future()
		f.set_result(None)
		self.step(f)

	def step(self, future):
		try:
			next_future=self.coro.send(None)
		except StopIteration as exc:
			print(f'task has been {exc.value}')
			raise StopError

		next_future.add_done_callback(self.step)

def run_forever():
	while True:
		events=selector.select()
		for key, mask in events:
			callback=key.data
			callback()

def run_until_complete(coro):
	task=Task(coro)
	try:
		run_forever()
	except StopError:
		print("coroutine completed!")
		pass

class StopError(BaseException):
	pass

fetcher=Fetcher()

run_until_complete(fetcher.fetch('/'))

