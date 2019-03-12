from Crypto.Cipher import AES
import sys

encrypted_f=open(sys.argv[1], 'rb')
lack_of_bytes=encrypted_f.readline()[:-1][0]

obj=AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')

b_initial_content=obj.decrypt(encrypted_f.readline())
content=b_initial_content[:-lack_of_bytes]
content=content.decode()


encrypted_f.close()

new_file=open(sys.argv[2], 'wt')
new_file.write(content)
new_file.close()
