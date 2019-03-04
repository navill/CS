import time

n=60000000

li=[i for i in range(n+1)]


start=time.time()
for i in range(len(li))):
	li[i]*=2

elapsed=time.time()-start
print(f'elapsed time : {elapsed:0.2f}')

