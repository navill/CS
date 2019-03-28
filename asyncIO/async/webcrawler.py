import asyncio
from bs4 import BeautifulSoup
from urllib.parse import urlsplit, urljoin

class Crawler:
	def __init__(self, root_url):
		self.max_workers=10
		self.q=asyncio.Queue()
		self.root_url=root_url
		self.seen_urls=set()
		self.q.put_nowait(root_url)

	async def crawl(self):
		workers=[asyncio.create_task(self.worker()) for _ in range(self.max_workers)]

		await self.q.join()

		for w in workers:
			w.cancel()

		await asyncio.gather(*workers, return_exceptions=True)

	async def worker(self):
		while True:
			url=await self.q.get()
			await self.fetch(url)
			self.q.task_done()

	async def fetch(self, url):
		self.seen_urls.add(url)
		print('*'*80)
		r=urlsplit(url)
		print(url)
		if r.scheme=='https':
			reader, writer=await asyncio.open_connection(r.hostname, 443, ssl=True)
		else:
			reader, writer=await asyncio.open_connection(r.hostname, 80)
		writer.write('GET {} HTTP/1.1\r\nHost: {}\r\nConnection: close\r\n\r\n'.format(r.path, r.hostname).encode())

		response=b''

		while True:
			line=await reader.readline()
			if not line:
				break

			response+=line
	
		self.print_response(response)
		links=self.parse_links(response)
		for link in links.difference(self.seen_urls):
			self.q.put_nowait(link)

	def print_response(self, response):
		soup=BeautifulSoup(response, 'html.parser')
		print(soup.prettify())
	
	def make_whole_url(self, link):
		url=urljoin(self.root_url, link)
		return url

	def parse_links(self, response):
		soup=BeautifulSoup(response, 'html.parser')
		anchors=soup.find_all('a')
		links=set()
		for anchor in anchors:
			if anchor.get('href'):
				links.add(self.make_whole_url(anchor['href']))
		return links
			
crawler=Crawler('https://xkcd.com/')
loop=asyncio.get_event_loop()
loop.run_until_complete(crawler.crawl())


