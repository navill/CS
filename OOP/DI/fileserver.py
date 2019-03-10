import socket

f=open('filecontent.txt', 'rt')

sendbuf=b''

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock.bind(('127.0.0.1', 62525))
sock.listen()

data_sock, data_addr=sock.accept()
while True:
	data_sock.recv(1024)
	sendbuf=f.readline().encode()
	if not sendbuf:
		break
	data_sock.sendall(sendbuf)
	sendbuf=b''

f.close()
data_sock.close()
sock.close()

    
