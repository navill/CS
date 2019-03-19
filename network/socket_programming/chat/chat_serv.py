import socket
import selectors
import sys

sel=selectors.DefaultSelector()
data_sock_list=[]
clnt_addr_list=[]

def serv_accept(sock):
    data_sock, clnt_addr=sock.accept()
    data_sock_list.append(data_sock)
    clnt_addr_list.append(clnt_addr)
    print('connection from {}:{}'.format(clnt_addr[0], clnt_addr[1]))
    data_sock.setblocking(False)
    sel.register(data_sock, selectors.EVENT_READ, read)


def data_sock_close(data_sock):
		clnt_addr_list.pop(data_sock_list.index(data_sock))
		data_sock_list.remove(data_sock)
		sel.unregister(data_sock)
		data_sock.close()


def on_client_out(data_sock, received):
	if received.decode().split('$$')[1]=='0':
		print('connection from {}:{} closing'.format(
			clnt_addr_list[data_sock_list.index(data_sock)][0],
			clnt_addr_list[data_sock_list.index(data_sock)][1]))
		data_sock_close(data_sock)

def on_clnt_conn_cut(data_sock):
	print('ERROR[connection from {}:{} cut without notice]'.format(
		clnt_addr_list[data_sock_list.index(data_sock)][0],
		clnt_addr_list[data_sock_list.index(data_sock)][1]))  
	data_sock_close(data_sock)	

def read(data_sock, mask):
	if mask & selectors.EVENT_READ:
		received=data_sock.recv(1024)
		if received:
			on_client_out(data_sock, received)
			for sock in data_sock_list:
				sock.sendall(received)
		else:
			on_clnt_conn_cut(data_sock)

if len(sys.argv) < 3:
    print('usage : <host> <port>')
    exit()

serv_sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_sock.bind((sys.argv[1], int(sys.argv[2])))
serv_sock.listen(32)
serv_sock.setblocking(False)
sel.register(serv_sock, selectors.EVENT_READ, serv_accept)

while True:
    events=sel.select()
    for key, mask in events:
        if key.fileobj is serv_sock:
            callback=key.data
            callback(key.fileobj)
        else:
            callback=key.data
            callback(key.fileobj, mask)
