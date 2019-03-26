import random

def merge_sort_recursion(li, merged, start, end):
    if start >= end:
        return

    mid=(start+end)//2
    merge_sort_recursion(li, merged, start, mid)
    merge_sort_recursion(li, merged, mid+1, end)

    left_idx=start; right_idx=mid+1; temp_idx=start
    while left_idx<=mid and right_idx<=end:
        if li[left_idx]<li[right_idx]:
            merged[temp_idx]=li[left_idx]
            left_idx+=1
            temp_idx+=1
        else:
            merged[temp_idx]=li[right_idx]
            right_idx+=1
            temp_idx+=1
    while left_idx<=mid:
        merged[temp_idx]=li[left_idx]
        left_idx+=1
        temp_idx+=1
    while right_idx<=end:
        merged[temp_idx]=li[right_idx]
        right_idx+=1
        temp_idx+=1
    for i in range(start, end+1):
        li[i]=merged[i]


def merge_sort(li):
    n=len(li)
    merged=[None for _ in range(n)]
    start=0
    end=n-1
    merge_sort_recursion(li, merged, start, end)

if __name__=="__main__":
    while True:
        num_data=int(input('데이터 개수(종료:0):'))
        if not num_data:
            break
        data=[random.randint(1, 100) for _ in range(num_data)]
        print(data)
        merge_sort(data)
        print(data)
