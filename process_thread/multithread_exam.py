import threading
import time

def thread_main(li, n):
    for i in range(offset * n + 1, offset *(n + 1) + 1):
        li[i] *= 2

n = 1000 
#n = 60000000

offset = n // 4

li = [i for i in range(n+1)]
threads = []

# start=time.time()
for i in range(4):
    th = threading.Thread(target = thread_main,
                          args = (li, i))
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()

# elapsed=time.time()-start
# print(f'elapsed time : {elapsed:0.2f})
print(li)

