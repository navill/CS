import random
import time
def quick_sort(li, start, end):
    if start >= end:
        return
    left=start
    right=end
    pivot=li[(left+right)//2]
    while left <= right:
        while li[left] < pivot:
            left+=1
        while li[right] > pivot:
            right-=1
        
        if left <= right:
            li[left], li[right]=li[right], li[left]
            left+=1
            right-=1

    quick_sort(li, start, right)
    quick_sort(li, left, end)

if __name__=="__main__":
    while True:
        num_data=int(input('데이터 개수(종료:0):'))
        if not num_data:
            break
        data=[random.randint(1, 1000) for _ in range(num_data)]
        start=time.time()
        quick_sort(data, 0, len(data)-1)
        elapsed=time.time()-start
        print('elapsed time : {} sec.'.format(elapsed))
        #print(data)

