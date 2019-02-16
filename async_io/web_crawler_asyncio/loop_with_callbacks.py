#async programming with callbacks
#THERE IS NO PREEMTIVE MULTITASKING
#no mutex around changes to shared data like seen_urls

# with a callback-based async framework,
# saving its state explicitly, 
#because the function returns and loses its stack frame 
#before I/O completes

#the loss of context is called "stack ripping"

import socket
from selectors import (DefaultSelector, EVENT_WRITE,
EVENT_READ)

urls_todo=set(['/'])
seen_urls=set(['/'])

#control the event loop
stopped=False
selector=DefaultSelector()

class Fetcher:
    def __init__(self, url):
        self.response=b''
        self.url=url
        self.sock=None

    def fetch(self):
        self.sock=socket.socket()
        self.sock.setblocking(False)
        try:
            self.sock.connect(('xkcd.com', 80))
        except BlockingIOError:
            pass
        #hand control to the event loop
        selector.register(self.sock.fileno(), EVENT_WRITE, self.connected)
    
    def connected(self, key, mask):
        print('connected')
        selector.unregister(key.fd)
        request='GET {} HTTP/1.0\r\nHost: xkcd.com\r\n\r\n'.format(self.url)
        self.sock.send(request.encode('ascii'))

        #register the next callback
        selector.register(key.fd, EVENT_READ, self.read_response)

    def read_response(self, key, mask):
        global stopped

        chunk=self.sock.recv(4096)

        if chunk:
            self.response+=chunk
        else:
            selector.unregister(key.fd)
            links=self.parse_links()

            for link in links.difference(seen_urls):
                urls_todo.add(link)
                Fetcher(link).fetch()

            seen_urls.update(links)
            urls_todo.remove(self.url)
            #all pages are downloaded 
            #the fetcher stops the global event loop
            if not urls_todo:
                stopped=True

    def parse_links(self):
        return set()

def loop():
    while not stopped:
        events=selector.select()
        for key, mask in events:
            #connected is stored as key.data
            #retrieve and execute once the non-blocking socket is connected
            callback=key.data
            callback(key, mask)

fetcher=Fetcher('/353/')
fetcher.fetch()

loop()