import socket

url='xkcd.com'

sock=socket.socket()
sock.setblocking(False)

try:
    sock.connect(('xkcd.com', 80))
except BlockingIOError:
    pass

request='GET {} HTTP/1.0\r\nHost: xkcd.com\r\n'.format(url)
encoded=request.encode('ascii')

#a way to know when the connection is established
#so keep looping until the connection is set
while True:
    try:
        sock.send(encoded)
        break
    except OSError as e:
        pass

print('sent')