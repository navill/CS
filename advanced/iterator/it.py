import random

class It:
    def __init__(self, *args):
        self.data=args
        self.idx=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= len(self.data):
            raise StopIteration
        ret=self.data[self.idx]
        self.idx+=1
        return ret

if __name__=="__main__":
    li=[random.randint(1, 100) for _ in range(10)]
    it=It(*li)
    it=iter(it)
    print(it)

    for _ in range(len(li)+1):
        print(next(it))
    
        
