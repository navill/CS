import random


def selection_sort(li):
    n=len(li)

    for i in range(n-1):
        min_idx=i
        for j in range(i+1, n):
            if li[j] < li[min_idx]:
                min_idx=j
        li[i], li[min_idx]=li[min_idx], li[i]

if __name__=="__main__":
    while True:
        num_data=int(input('데이터 개수(종료:0):'))
        if not num_data:
            break
        data=[random.randint(1, 100) for _ in range(num_data)]
        print(data)
        selection_sort(data)
        print(data)
