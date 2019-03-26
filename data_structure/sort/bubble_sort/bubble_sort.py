import random
import time

def bubble_sort(li):
    n=len(li)
    for i in range(n-1):
        for j in range(n-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1]=li[j+1], li[j]

if __name__=="__main__":
    while True:
        num_data=int(input('데이터 개수(종료:0):'))
        if not num_data:
            break
        data=[random.randint(1, 1000) for _ in range(num_data)]
        start=time.time()
        bubble_sort(data)
        elapsed=time.time()-start
        print('elapsed time : {} sec.'.format(elapsed))
        #print(data)