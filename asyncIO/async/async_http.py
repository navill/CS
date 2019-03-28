import asyncio
import socket
from bs4 import BeautifulSoup
from urllib.parse import urlsplit

def print_response(response):
	soup=BeautifulSoup(response, 'html.parser')
	print(soup.prettify())


async def fetcher():
	url='https://xkcd.com/'
	r=urlsplit(url)
	reader, writer=await asyncio.open_connection(r.hostname, 443, ssl=True)

	writer.write('GET {} HTTP/1.1\r\nHost: xkcd.com\r\nConnection: close\r\n\r\n'.format(r.path).encode())
	response=b''	

	while True:
		line=await reader.readline()
		if not line:
			break
		
		response+=line

	print_response(response)

asyncio.run(fetcher())

