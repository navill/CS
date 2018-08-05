class Base:
    @staticmethod
    def f():
        print('static method')

    @classmethod
    def g(cls):
        print(cls.__name__)

if __name__=="__main__":
    Base.f()
    Base.g()
    