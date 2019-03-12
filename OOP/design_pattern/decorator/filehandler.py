
from abc import ABCMeta, abstractmethod
from shutil import copyfile
import os
import zipfile
import sys
from Crypto.Cipher import AES

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

class EncryptCopier(FileDecorator):
	def __init__(slf, delegate):
		super().__init__(delegate)

	def encrypt(self, content):
		obj=AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
		len_of_content=len(content)
		lack_bytes=16-(len_of_content%16)
		new_content=content+'*'*lack_bytes
		ciphertext=obj.encrypt(new_content)

		return ciphertext, lack_bytes
	
	def encrypt_file(self, src, dst):
		# read from the src file	
		org_f=open(src, 'r')
		content=org_f.read()
		org_f.close()

		# encrypt
		ciphertext, lack_bytes=self.encrypt(content)

		# write to the new_src file	
		new_src='new_'+os.path.split(src)[1]	
		new_file=open(new_src, 'wb')
		new_file.write(lack_bytes.to_bytes(1, 'little', signed=False))
		new_file.write('\n'.encode())
		new_file.write(ciphertext)
		new_file.close()

		return new_src

	def copy(self, src, dst):
		# added functionality
		new_src=self.encrypt_file(src, dst)	
		# delegate copy
		self.real_copy(new_src, dst)
		os.remove(new_src)

if __name__=="__main__":
	rfc=RealFileCopier()
#	zfc=ZipFileCopier(rfc)
#	zfc.copy(sys.argv[1], sys.argv[2])
	
	efc=EncryptCopier(rfc)
	efc.copy(sys.argv[1], sys.argv[2])

	

	
