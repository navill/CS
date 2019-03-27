import random

def insertion_sort(li):
    n=len(li)
    temp=None
    for i in range(1, n):
        temp=li[i]
        for j in range(i-1, -2, -1):
            if j==-1:
                break
            if li[j] > temp:
                li[j+1]=li[j]
            else:
                break
        li[j+1]=temp

if __name__=="__main__":
    while True:
        num_data=int(input('데이터 개수(종료:0):'))
        if not num_data:
            break
        data=[random.randint(1, 100) for _ in range(num_data)]
        print(data)
        insertion_sort(data)
        print(data)
