def change_value(li, new_li):
    li=new_li
    print('{} in change_value'.format(li))

if __name__=="__main__":
    li=[1, 2 ,3, 4]
    new_li=['I am your father!', 2, 3, 4]
    change_value(li, new_li)
    print('{} in main'.format(li))