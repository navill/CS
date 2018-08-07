def make_fibo_array(n):
    ret=[]
    a=0
    b=1
    for i in range(n):
        ret.append(a)
        a, b=b, a+b
    return ret

def make_fibo_gen(n):
    a=0
    b=1
    for i in range(n):
        yield a
        a, b=b, a+b

if __name__=="__main__":
    # result=make_fibo_array(10)
    # for elem in result:
    #     print(elem, end="  ")
    # print()

    g=make_fibo_gen(10)
    for i in range(11):
        print(next(g), end="  ")
        


