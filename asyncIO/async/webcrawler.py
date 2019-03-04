from asyncio import Queue
import asyncio
import aiohttp
from bs4 import BeautifulSoup

class Crawler:
	def __init__(self, root_url):
		self.max_tasks=10
		self.q=Queue()
		self.seen_urls=set()

		self.q.put(root_url)

	async def crawl(self):
		self.session=aiohttp.ClientSession(loop=loop)
		workers=[asyncio.Task(self.work()) for _ in range(self.max_tasks)]

		await self.q.join()
		for w in workers:
			w.cancel()
		self.sesson.close()

	async def work(self):
		while True:
			url = await self.q.get()
			await self.fetch(url)
			self.q.task_done()

	async def fetch(self, url):
		response = await self.session.get(url)
		links = await self.parse_links(reponse)
		for link in links.difference(self.seen_urls):
			self.q.put_nowait(link)
		self.seen_urls.update(links)
		print(response)
		
	async def parse_links(self, response):
		soup=BeautifulSoup(response, 'html.parser')
		anchors=soup.find_all('a')
		links=[]
		for anchor in anchors:
			if anchor.get('href'):
				links.append(anchor['href'])
		return links



loop=asyncio.get_event_loop()
crawler=Crawler('https://xkcd.com')
loop.run_until_complete(crawler.crawl())

