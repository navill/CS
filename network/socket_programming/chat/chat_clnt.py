import socket
import threading
import sys


# handle stdin
def get_sendmsg(msg):
	send_msg=sys.argv[3]+ "$$" + msg
	buffer=send_msg.encode()
	return buffer

def input_handler(sock):
    while True:
        msg = input()
        buffer=get_sendmsg(msg)
        sent=sock.send(buffer)
        while sent < len(buffer):
            buffer=buffer[sent:]
            sent+=sock.send(buffer)
        if msg=='0':
            break

def process_recvmsg(buffer):
	msg=buffer.decode()
        
	if msg.startswith('$$ENTER$$'):
		if msg[9:] != sys.argv[3]:
			print("{} enter the chat room!".format(msg[9:]))
		return 
	name, msg=msg.split('$$')
	if name != sys.argv[3]:
		if msg=='0':
			print("{} left the chat room!!".format(name))
		else:
			print('[{}] : {}'.format(name, msg))

def output_handler(sock):
	while True:     
		buffer=sock.recv(1024)
		if not buffer:
			break
		process_recvmsg(buffer)

if len(sys.argv) < 4:
    print('usage : <host> <port> <name>')
    exit()

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect_ex((sys.argv[1], int(sys.argv[2])))

first_msg='$$ENTER$$'+sys.argv[3]
sock.sendall(first_msg.encode())

threads=[]

threads.append(threading.Thread(target=input_handler, args=(sock,)))
threads.append(threading.Thread(target=output_handler, args=(sock,)))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

sock.close()




