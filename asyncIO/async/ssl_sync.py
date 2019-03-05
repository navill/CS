import socket
import ssl
from bs4 import BeautifulSoup

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss=ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_TLS)

request='GET / HTTP/1.1\r\nHost: xkcd.com\r\nConnection: close\r\n\r\n'

ss.connect(('xkcd.com',443))
ss.send(request.encode())

response=b''
chunk=ss.recv(4096)
while chunk:
	response+=chunk
	chunk=ss.recv(4096)

print(response)
