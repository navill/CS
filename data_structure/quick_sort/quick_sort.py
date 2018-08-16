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
    data=[2, 4, 5, 7, 9, 5, 11, 3, 8, 1]
    quick_sort(data, 0, len(data)-1)
    print(data)

