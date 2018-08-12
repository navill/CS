def linear_search(li, target):
    for idx in range(len(li)):
        if target==li[idx]:
            return idx
    return None

if __name__=="__main__":
    data=[i**2 for i in range(1, 10)]

    target=9
    idx=linear_search(data, target)

    if idx:
        print('index : {}, data : {}'.format(idx, data[idx]))
    else:
        print('Failed to find the data of {}'.format(target))