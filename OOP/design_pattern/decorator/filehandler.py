
from abc import ABCMeta, abstractmethod
from shutil import copyfile
# add functionality to the method that I make.

# abstract class for inteface
class FileCopier(metaclass=ABCMeta):
	@abstractmethod
	def copy(self, src, dst):
		pass

# implementation
class RealFileCopier(FileCopier):
	def copy(self, src, dst):
		copyfile(src, dst)	

class FileDecorator(FileCopier):
	def __init__(self, delegate):
		self.delegate=delegate

	def real_copy(self, src, dst):
		self.delegate.copy(src, dst)	

class ZipFileCopier(FileCopier):
	def __init__(self, delegate):
		super().__init__(delegate)

	def copy(self, src, dst):
#zip
		self.real_copy(src, dst)
	
	

	

	
