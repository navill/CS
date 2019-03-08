import socket

f=open('filecontent.txt', 'rt')
buf=b''

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock.bind(('127.0.0.1', 62525))
sock.listen()
data_sock, data_addr=sock.accept()

while True:
    buf=f.readline().encode()
    if not buf:
        break
    
    data_sock.sendall(buf)
    data_sock.recv(1024)

data_sock.close()
sock.close()

    
