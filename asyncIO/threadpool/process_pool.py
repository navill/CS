import socket
import ssl
from bs4 import BeautifulSoup
from queue import Queue
import multiprocessing
import time
import os

def parse_links(response):
    soup=BeautifulSoup(response, 'html.parser')
    anchors=soup.find_all('a')
    links=[]
    for anchor in anchors:
        if anchor.get('href'):
            links.append(anchor['href'])
    return links

class FetchProcess(multiprocessing.Process):
    def __init__(self, pool):
        super().__init__()
        self.pool=pool

    def fetch(self, url):
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ss=ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_TLS)
        ss.connect(('xkcd.com', 443))
        request='GET {} HTTP/1.1\r\nHost: xkcd.com\r\nConnection: close\r\n\r\n'.format(url)
        ss.send(request.encode('ascii'))
        response=b''
        chunk=ss.recv(4096)
        while chunk:
            response+=chunk
            chunk=ss.recv(4096)

        print(response)
        links=parse_links(response)
        
        if links:
            self.pool.cv.acquire()
            for link in links:
                self.pool.tasks.put(link)
            self.pool.cv.notify_all()
            self.pool.cv.release()
            time.sleep(0.02)
        ss.close()
        
    def run(self):
        while True:
            self.pool.cv.acquire()
            while not self.pool.stopped and self.pool.tasks.empty():
                self.pool.cv.wait()

            if self.pool.stopped:
                self.pool.cv.notify()
                self.pool.cv.release()
                time.sleep(0.02)
                return

            url=self.pool.tasks.get()
            self.pool.cv.release()
            time.sleep(0.02)

            self.fetch(url)

class MyProcessPool:
    cv=multiprocessing.Condition()
    stopped=False
    def __init__(self):
        self.processes=[FetchProcess(self) for _ in range(os.cpu_count())]

        self.tasks=Queue()
        self.tasks.put('/')

        for p in self.processes:
            p.start()

    def close_all_threads(self):
        self.cv.acquire()
        self.stopped=True
        self.cv.notify()
        self.cv.release()
        time.sleep(0.02)

        for p in self.processes:
            p.join()

if __name__=="__main__":
    pp=MyProcessPool()


