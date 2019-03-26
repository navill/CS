import threading

def thread_main(li, n):
	for i in range(offset * n, offset *(n + 1)):
		li[i] *= 2

n = 1000 

offset = n // 4

li = [i+1 for i in range(n)]
threads = []

for i in range(4):
	th = threading.Thread(target = thread_main,
                          args = (li, i))
	threads.append(th)

for th in threads:
	th.start()

for th in threads:
	th.join()

print(li)

