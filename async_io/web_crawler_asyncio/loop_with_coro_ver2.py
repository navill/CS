import socket
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

selector=DefaultSelector()

# future result that a coroutine is waiting for
class Future:
    def __init__(self):
        self.result=None
        self._callbacks=[]

    def add_done_callback(self, fn):
        self._callbacks.append(fn)

    def set_result(self, result):
        self.result=result
        for fn in self._callbacks:
            fn(self)

    def __iter__(self):
        yield self
        return self.result

def read(sock):
    f=Future()

    def on_readable():
        f.set_result(sock.recv(4096))
    
    selector.register(sock.fileno(), EVENT_READ, on_readable)
    chunk=yield from f
    selector.unregister(sock.fileno())
    return chunk

def read_all(sock):
    reponse=[]
    chunk=yield from read(sock)
    while chunk:
        response.append(chunk)
        chunk=yield from read(sock)
    
    return b''.join(response)

class Fetcher:
    def __init__(self, url):
        self.url=url
        self.response=b''

    def fetch(self):
        sock=socket.socket()
        sock.setblocking(False)
        try:
            sock.connect(('xkcd.com', 80))
        except BlockingIOError:
            pass
        
        #a pending future
        f=Future()

        def on_connected():
            # resolve the future 
            # calls task's step
            f.set_result(None)

        selector.register(sock.fileno(), EVENT_WRITE, on_connected)

        # to pause fetch until the socket is ready
        yield from f
        
        selector.unregister(sock.fileno())
        print('connected')

        # socket is connected to the server
        # start sending the request
        request='GET {} HTTP/1.0\r\nHost: xkcd.com\r\n\r\n'.format(self.url)
        sock.send(request.encode('ascii'))

        self.response=yield from read_all(sock)

class CancelledError(Exception):
    def __init__(self):
        self.error='the coroutine is cancelled'

# coroutine DRIVER 
# which will let the future resolves,
# and resumes the generator
class Task:
    def __init__(self, coro):
        self.coro=coro
        f=Future()
        # resolves the future
        # it will start the coroutine
        f.set_result(None)
        self.step(f)

    def step(self, future):
        try:
            # start the fetch
            # resume fetch 
            next_future=self.coro.send(future.result)
        except CancelledError:
            self.cancelled=True
            return
        except StopIteration:
            return

        # callback
        next_future.add_done_callback(self.step)

    def cancel(self):
        self.coro.throw(CancelledError)

def loop():
    while True:
        events=selector.select()
        for key, mask in events:
            callback=key.data
            callback(key, mask)


fetcher=Fetcher('/353/')
Task(fetcher.fetch())

loop()
