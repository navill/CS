def change_value(x, val):
    x=val
    print('x : {} in change_value'.format(x))

if __name__=="__main__":
    x=(1, 2)
    change_value(x, (3, 4))
    print('x : {} in main'.format(x))
