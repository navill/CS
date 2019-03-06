# because each callback has its own stack,
# the local variables in the stack frame will be lost on returning
# it means it lost the state and context of where I am doing.
# To keep state, the stacks must be stored in the heap and passed into callbacks as parameters 
# it ls called "stack ripping" 
import socket 
import ssl 
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ 
from bs4 import BeautifulSoup
import time
import pprint

urls_go=set(['/'])
urls_done=set()

selector=DefaultSelector()

class Fetcher:
	def __init__(self, url):
		self.response=b''
		self.url=url
		self.context=None
		self.sock=None
		self.ssock=None

	def fetch(self):
		self.context=ssl.create_default_context()
		self.sock=socket.socket(socket.AF_INET)
		self.sock.setblocking(False)
		self.ssock=self.context.wrap_socket(self.sock, server_hostname='xkcd.com')
		
		try:
			self.ssock.connect(('xkcd.com', 443))
		except:
			pass

		selector.register(self.ssock.fileno(), EVENT_WRITE, self.connected) 
	
	def connected(self, key, mask):
		cert=self.ssock.getpeercert()
		pprint.pprint(cert)

		selector.unregister(self.ssock.fileno())
		request='GET {} HTTP1.0\r\nHost: xkcd.com\r\n\r\n'.format(self.url)
			
		try:	
			self.ssock.sendall(request.encode())
		except (ssl.SSLWantReadError, ssl.SSLWantWriteError):
			pass

		selector.register(self.ssock.fileno(), EVENT_READ, self.read_response)
		
	def read_response(self, key, mask):
		try:	
			chunk=self.ssock.recv(4096)
		except (ssl.SSLWantReadError, ssl.SSLWantWriteError):
			pass
		
		if chunk:
			self.response+=chunk
		else:
			selector.unregister(self.ssock.fileno())
			links=self.parse_links()

			for link in links.difference(urls_done):
				urls_go.add(link)
				Fetcher(link).fetch()

			urls_done.update(links)
			urls_go.remove(self.url)

	def parse_links(self):
		soup=BeautifulSoup(self.response, 'html.parser')
		anchors=soup.find_all('a')
		links=set()
		for anchor in anchors:
			if anchor.get('href'):
				links.add(anchor['href'])
		
		return links
	
	def print_response(self):
		soup=BeautifulSoup(self.response, 'html.parser')
		print(soup.prettify())

def loop():
	while True: 
		events=selector.select()
		for key, mask in events:
			callback=key.data
			callback(key, mask)

fetcher=Fetcher('/')
fetcher.fetch()

loop()
