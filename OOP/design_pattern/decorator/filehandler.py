
from abc import ABCMeta, abstractmethod
from shutil import copyfile
import os
import zipfile
import sys


# add functionality to the method that I make.


# abstract class for inteface
class FileCopier(metaclass=ABCMeta):
	@abstractmethod
	def copy(self, src, dst):
		pass



# implementation
class RealFileCopier(FileCopier):
	def copy(self, src, dst):
		if os.path.exists(src) and os.path.exists(os.path.split(dst)[0]): 
			copyfile(src, dst)	
		else:
			raise Exception("There is no path!")



#decorator
class FileDecorator(FileCopier):
	def __init__(self, delegate):
		self.delegate=delegate

	def real_copy(self, src, dst):
		self.delegate.copy(src, dst)	



# inherit from decorator
class ZipFileCopier(FileDecorator):
	def __init__(self, delegate):
		super().__init__(delegate)

	def zip_file(self, src, dst):
		try:	
			if os.path.exists(src):
				dst=os.path.split(dst)[1]
				with zipfile.ZipFile(dst, 'w') as myzip:
					myzip.write(src)
				return dst
		except:
			raise Exception("There is no file!")

	def copy(self, src, dst):
		# added functionality
		new_src=self.zip_file(src, dst)
		# delegate copy	
		self.real_copy(new_src, dst)
		os.remove(new_src)		

class EncryptedCopier(FileDecorator):
	def __init__(slf, delegate):
		super().__init__(delegate)

	def encrypt_file(src, dst):
		pass

	def copy(self, src, dst):
		# added functionality
		new_src=self.encrypt_file(src, dst)	
		# delegate copy
		self.real_copy(new_src, dst)
		os.remove(new_src)

if __name__=="__main__":
	rfc=RealFileCopier()
	zfc=ZipFileCopier(rfc)
	zfc.copy(sys.argv[1], sys.argv[2])

	

	
