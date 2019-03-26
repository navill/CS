from fdmanage import  FDManager, FileFDReader, SocketFDReader, STDFDReader
from locator import Locator, SingletonError


#fr=FileFDReader('filecontent.txt')
#fr=SocketFDReader(('localhost', 62525))
fr=STDFDReader()

locator=Locator(fr)

locator.init()

# if a Locator dobject is created again, it would raise a singletonerror
"""
try:
	locator2=Locator(fr)
except SingletonError as exc:
	print(exc)
	exit()
"""

#fm=FDManager('new_content_filereader.txt')
#fm=FDManager('new_content_socketreader.txt')
fm=FDManager('new_content_stdreader.txt')

while True:
    num_read=fm.read()
    if not num_read:
        break
    fm.write() 
    num_read=0

