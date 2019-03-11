from abc import ABCMeta, abstractmethod
import socket

class FDManager:
	reader=None
# dependency injection using constructor
	"""
	def __init__(self, filename, reader):
        self.f=open(filename, 'wt')
        FDManager.reader=reader 
        self.buf=''
	"""
	def __init__(self, filename):
		self.f=open(filename, 'wt')
		self.buf=''

	def set_reader(self, reader):
		FDManager.reader=reader
	
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
		self.sock.sendall('message starting'.encode())

	def read(self):
		buf=self.sock.recv(1024)
		self.buf=buf.decode()
		self.sock.sendall('done'.encode())
		return self.buf

class STDFDReader(FDReader):
	def read(self):
		buf=input('# ')
		if not buf:
			return ''
		buf+='\n'
		return buf

        
