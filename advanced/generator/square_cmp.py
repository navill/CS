def make_square(li):
    ret=[]
    for elem in li:
        ret.append(elem*elem)
    return ret

def make_square_gen(li):
    idx=0
    while idx < len(li):
        yield li[idx]**2
        idx+=1

if __name__=="__main__":
    li=[1, 2, 3, 4]
    result=make_square(li)
    #print(result)

    g=make_square_gen(li)
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
