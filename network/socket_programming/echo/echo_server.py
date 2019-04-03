import socket
import sys

serv_sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv_sock.bind((sys.argv[1], int(sys.argv[2])))

serv_sock.listen()

data_sock, clnt_addr=serv_sock.accept()

if data_sock:
	while True:
		received=data_sock.recv(1024)
		if not received:
			break
		print(f'received from client :{received}')
		data_sock.sendall(received)

data_sock.close()
serv_sock.close()

