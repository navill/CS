def change_value(li, idx, val):
    li[idx]=val
    print('{} in change_value'.format(li))

if __name__=="__main__":
    li=[1, 2 ,3, 4]
    change_value(li, 0, 'I am your father!')
    print('{} in main'.format(li))