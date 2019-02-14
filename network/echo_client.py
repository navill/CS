import socket

serv_ip, serv_port='127.0.0.1', 3030

clnt_sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clnt_sock.connect((serv_ip, serv_port))

clnt_sock.send(b'hello, you should learn computer science')
received=clnt_sock.recv(1024)
print(received)