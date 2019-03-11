from fdmanage import  FDManager, FileFDReader, SocketFDReader, STDFDReader


#fr=FileFDReader('filecontent.txt')
#fr=SocketFDReader(('localhost', 62525))
fr=STDFDReader()



# dependency injection using constructor

#fm=FDManager('new_content_filereader.txt', fr)
#fm=FDManager('new_content_socketreader.txt', fr)
#fm=FDManager('new_content_stdreader.txt', fr)



# dependency injection using method

#fm=FDManager('new_content_filereader.txt')
#fm=FDManager('new_content_socketreader.txt')
fm=FDManager('new_content_stdreader.txt')

fm.set_reader(fr)

while True:
    num_read=fm.read()
    if not num_read:
        break
    fm.write() 
    num_read=0

