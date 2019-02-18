from asyncio import Queue
import asyncio
import aiohttp

class Crawler:
    def __init__(self, root_url, max_redirect):
        self.max_tasks=10
        self.max_redirect=max_redirect
        self.q=Queue()
        self.seen_urls=set()

        #aiohttp's ClientSession does connection pooling and
        #HTTP keep-alives for us
        self.session=aiohttp.ClientSession(loop=loop)

        self.q.put((root_url, self.max_redirect))

    @asyncio.coroutine
    def crawl(self):
        #run the crawler until all work is done.
        
        # if the workers were threads 
        # to avoid creating expensive threads
        # a thread pool typically grows on demand
        # coroutines are cheap, so start the maximum number allowed
        workers=[asyncio.Task(self.work()) for _ in range(self.max_tasks)]

        #when all work is done, exit.
        yield from self.q.join()
        for w in workers:
            w.cancel()

    @asyncio.coroutine
    def work(self):
        while True:
            url, max_redirect=yield from self.q.get()

            yield from self.fetch(url, max_redirect)
            self.q.task_done()

    @asyncio.coroutine
    def fetch(self, url, max_redirect):
        response=yield from self.session.get(
            url, allow_redirecs=False)

        try:
            if is_redirect(response):
                if max_redirect > 0:
                    next_url=response.headers['location']
                    if next_url in self.seen_urls:
                        return
                    
                    self.seen_urls.add(next_url)
                    self.q.put_nowait((next_url, max_redirect-1))
            else:
                links=yield from self.parse_links(response)
                for link in links.difference(self.seen_urls):
                    self.q.put_nowait((link, self.max_redirect))
                self.seen_urls.update(links)
        finally:
            yield from response.release()



loop=asyncio.get_event_loop()

crawler=Crawler('http://xkcd.com', max_redirect=10)

loop.run_until_complete(crawler.crawl())
