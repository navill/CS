class FileReader:
    def __init__(self, filename):
        self.f=open(filename, 'rt')
    
    def __iter__(self):
        return self

    def __next__(self):
        line=self.f.readline()
        if not line:
            raise StopIteration
        return line

if __name__=='__main__':
    fr=FileReader('test.txt')
    print(next(fr), end="")
    print(next(fr), end="")
    print(next(fr), end="")
    print(next(fr), end="")
    print(next(fr), end="")
