# 다형성을 도와주는 liskov substitution
# 사용자에게 인터페이스 명세를 제공

# 하위 클래스는 인터페이스 명세에 따라 구현해야 한다

def filemake(fr, fn):
    f=open(fn, 'wt')
    line=fr.read_line()
    while line!='eof':
        f.write('new_file['+line[:-1]+']\n')
        line=fr.read_line()
    f.close()

class FileReader:
    def __init__(self, filename):
        self.f=open(filename, 'rt')

    def read_line(self):
        """
        fr.read_line() -> string
        읽어온 문자열이 있다면 문자열을 반환
        없으면 'eof'을 반환
        반환값이 None이 아님을 유의하세요!
        """
        line=self.f.readline()
        if line:
            return line
        else:
            return 'eof'

#반드시 상위 클래스가 가지는 명세를 따른다!!
class NumberFileReader(FileReader):
    def read_line(self):
        line=self.f.readline()
        if line:
            line='num['+line[:-1]+']\n'
            return line
        else:
            return None

class NameFileReader(FileReader):
    def read_line(self):
        line=self.f.readline()
        if line:
            line='name['+line[:-1]+']\n'
            return line
        else:
            return 'eof'

if __name__=="__main__":
    #fr=FileReader('test.txt')
    #fr=NumberFileReader('numbers.txt')
    fr=NameFileReader('names.txt')
    filemake(fr, 'new_3.txt')
