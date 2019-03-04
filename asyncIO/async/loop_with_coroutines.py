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
import ssl
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ

selector=DefaultSelector()

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

def read(ss):
	f=Future()

	def on_readable():
		f.set_result(ss.recv(4096))

	selector.register(ss.fileno(), EVENT_READ, on_readable)
	chunk=yield from f
	selector.unregister(ss.fileno())
	return chunk

def read_all(ss):
	response=[]
	chunk=yield from read(ss)
	while chunk:
		response.append(chunk)
		chunk=yield from read(ss)
	
	return b''.join(response)

class Fetcher:
	def fetch(self, url):
		response=b''
		sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.setblocking(False)
		ss=ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_TLS)
		try:
			ss.connect(('xkcd.com', 443))
		except BlockingIOError:
			pass

		f=Future()
		
		def on_connected():
			f.set_result(None)

		selector.register(ss.fileno(), EVENT_WRITE, on_connected)

		yield from  f

		selector.unregister(ss.fileno())
		print('connected')

		request='GET {} HTTP/1.1\r\nHost: xkcd.com\r\nConnection: close\r\n\r\n'.format(url)
		ss.sendall(request.encode())
		
		response=yield from read_all(ss)
		"""	
		while True:
			f=Future()

			def on_readable():
				f.set_result(ss.recv(4096))

			selector.register(ss.fileno(), EVENT_READ, on_readable)

			chunk=yield f
			selector.unregister(ss.fileno())
			if chunk:
				response+=chunk
			else:
				break
		"""
		print(response)

class Task:
	def __init__(self, coro):
		self.coro=coro
		f=Future()
		f.set_result(None)
		self.step(f)

	def step(self, future):
		try:
			next_future=self.coro.send(future.result)
		except StopIteration:
			return

		next_future.add_done_callback(self.step)

def loop():
	while True:
		events=selector.select()
		for key, mask in events:
			callback=key.data
			callback()

fetcher=Fetcher()
Task(fetcher.fetch('/'))

loop()

