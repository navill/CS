import random

def merge(li,start,mid,end):
    merged=[]
    left_idx=start;right_idx=mid+1
    while left_idx<=mid and right_idx<=end:
        if li[left_idx]<li[right_idx]:
            merged.append(li[left_idx])
            left_idx+=1
        else:
            merged.append(li[right_idx])
            right_idx+=1
    while left_idx<=mid:
        merged.append(li[left_idx])
        left_idx+=1
    while right_idx<=end:
        merged.append(li[right_idx])
        right_idx+=1
    li[start:end+1]=merged

def merge_sort(li, start, end):
    if start>=end:
        return
    mid=(start+end)//2
    merge_sort(li,start,mid)
    merge_sort(li,mid+1,end)
    
    merge(li,start,mid,end)

if __name__=="__main__":
    while True:
        num_data=int(input('데이터 개수(종료:0):'))
        if not num_data:
            break
        data=[random.randint(1, 100) for _ in range(num_data)]
        print(data)
        merge_sort(data, 0, len(data)-1)
        print(data)
