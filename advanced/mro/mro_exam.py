#mro - method resolution order
#act like DFS(depth first search)

class A:
    def func(self):
        print('A.func')

class B(A):
    def func(self):
        print('B.func')

class C:
    def func(self):
        print('C.func')

class D(B):
    def func(self):
        print('D.func')

class E(C):
    def func(self):
        print('E.func')

class F(D, E):
    def func(self):
        print('F.func')

if __name__ == "__main__":
    print(F.__mro__)
    f = F()
    f.func()


