#we achieved "concurrency" here, but not what is traditionally called "parallelism"

import socket
from selectors import DefaultSelector, EVENT_WRITE

selector=DefaultSelector()

sock=socket.socket()
sock.setblocking(False)

try:
    sock.connect(('xkcd.com', 80))
except BlockingIOError:
    pass

def connected():
    #sock.fileno --> fild descriptor
    selector.unregister(sock.fileno())

#To be notified when the connection is established
#want to know when the socket is "writable"
selector.register(sock.fileno(), EVENT_WRITE, connected)

#we process I/O notifications as the selector receives them in a loop
def loop():
    while True:
        events=selector.select()
        for key, mask in events:
            #connected is stored as key.data
            #retrieve and execute once the non-blocking socket is connected
            callback=key.data
            callback(key, mask)

loop()