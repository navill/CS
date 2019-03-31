import socket
import ssl
from bs4 import BeautifulSoup
from queue import Queue
import threading
import time
import os

def print_response(response):
    soup=BeautifulSoup(response, 'html.parser')
    print(soup.prettify())

def parse_links(response):
    soup=BeautifulSoup(response, 'html.parser')
    anchors=soup.find_all('a')
    links=[]
    for anchor in anchors:
        if anchor.get('href'):
            links.append(anchor['href'])
    return links

class FetchThread(threading.Thread):
    def __init__(self, pool):
        super().__init__()
        self.pool=pool

    def fetch(self, url):
        context=ssl.create_default_context()
        ssock=context.wrap_socket(socket.socket(socket.AF_INET), server_hostname='xkcd.com')
        ssock.connect(('xkcd.com', 443))
        request='GET {} HTTP/1.1\r\nHost: xkcd.com\r\nConnection: close\r\n\r\n'.format(url)
        ssock.sendall(request.encode())
        response=b''
        chunk=ssock.recv(4096)
        while chunk:
            response+=chunk
            chunk=ssock.recv(4096)

        print_response(response)
        links=parse_links(response)
        
        if links:
            self.pool.cv.acquire()
            for link in links:
                self.pool.tasks.put(link)
            self.pool.cv.notify_all()
            self.pool.cv.release()
            time.sleep(0.02)
        ssock.close()
        
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

class MyThreadPool:
    cv=threading.Condition()
    stopped=False
    def __init__(self):
        self.threads=[FetchThread(self) for _ in range(os.cpu_count())]

        self.tasks=Queue()
        self.tasks.put('/')

        for th in self.threads:
            th.start()

    def close_all_threads(self):
        self.cv.acquire()
        self.stopped=True
        self.cv.notify()
        self.cv.release()
        time.sleep(0.02)

        for th in self.threads:
            th.join()

if __name__=="__main__":
    tp=MyThreadPool()
