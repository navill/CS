from abc import ABCMeta, abstractmethod
from locator import Locator
import socket

class FDManager:
    def __init__(self, filename):
        self.f=open(filename, 'wt')
        self.reader=Locator.get_instance().get_reader()
        self.buf=''

    def read(self):
        self.buf=self.reader.read()
        return len(self.buf)

    def write(self):
        if self.buf:
            self.f.write(self.buf)

    def close(self):
        self.f.close()

#추상 클래스
class FDReader(metaclass=ABCMeta):
    @abstractmethod
    def read(self):
        pass

class FileFDReader(FDReader):
    def __init__(self, filename):
        self.f=open(filename, 'rt')

    def read(self):
        return self.f.readline()

class SocketFDReader(FDReader):
    def __init__(self, addr):
        self.sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.sock.connect_ex(addr)
        self.buf=''

    def read(self):
        print('start read')
        buf=self.sock.recv(1024)
        while buf:
            print(buf, 'in while')
            self.buf+=buf.decode()
            buf=b''
            buf=self.sock.recv(1024)
        
        print(buf, 'in read')
        self.sock.sendall('done'.encode())
        return self.buf

class STDFDReader(FDReader):
    def read(self):
        pass
