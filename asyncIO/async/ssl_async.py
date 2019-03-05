import socket
import ssl
from bs4 import BeautifulSoup
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ

selector=DefaultSelector()

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setblocking(False)
ss=ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_TLS)

request='GET / HTTP/1.1\r\nHost: xkcd.com\r\nConnection: close\r\n\r\n'

ss.connect(('xkcd.com',443))

def on_connected():
	selector.unregister(ss.fileno())

selector.register(ss.fileno(), EVENT_WRITE, on_connected)

while True:
	event=selector.select()
	for key, mask in event:
		callback=key.data
		callback()
	break

response=b''
is_done=False
def on_readable():
	global is_done
	chunk=ss.recv(4096)
	if chunk:
		response+=chunk
	else:
	 	is_done=True

ss.send(request)
selector.register(ss.fileno(), EVENT_READ, on_readable)
while True:
	event=selector.select()
	for key, mask in event:
		callback=key.data
		callback()
	if is_done:
		break

print(response)
