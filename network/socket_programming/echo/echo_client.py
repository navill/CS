import sys
import socket

buf=None
serv_ip, serv_port=sys.argv[1], int(sys.argv[2])

clnt_sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clnt_sock.connect((serv_ip, serv_port))

while True:
	msg=input("# ")
	if msg=='0':
		break
	buf=msg.encode()
	clnt_sock.send(buf)
	b_received=clnt_sock.recv(1024)
	received=b_received.decode()
	print(f'received : {received}')	
	
