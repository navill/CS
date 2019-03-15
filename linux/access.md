---
# file attributes
```
$ ls -l
-rwxr--r-x 1 greg greg 400 3월 15 22:10 hello.c
```
---
# chmod
```
# user add read
$ chmod u+r hello.c
# group add excecute
$ chmod g+x main
# other minus write
$ chmod o-w test.txt
```
---
# chmod
```
# rwxrwxrwx
$ chmod 777 hello.c
# rw-r-xr--
$ chmod 654 hello.c
```
---
# SetUID
  - when executing, the access changes 
  - from user who executes the file
  - to user who owns
---
# SetUID
```
$ ls -l main
-rwxr-xr-x 1 greg greg 8322 3월 15 01:02 main
# SetUID
$ chmod 4755 main
$ ls -l main
-rwsr-xr-x 1 greg greg 8322 3월 15 01:10 main
```
---
# SetUID
```
$ ls -l /usr/bin/passwd
-rwsr-xr-x 1 root root 59640 1월 26 2018  /usr/bin/passwd
```
---
# SetGID
  - when executing, access changes
  - to group which owns
---
# SetGID
```
$ chmod 2755 main
$ ls -l main
-rwxr-sr-x 1 greg greg 8322 3월 15 01:10 main
```
---
# sticky bit
  - only directory
  - everyone can make a file in the directory
  - owner of the file is set to the one who created 
  - another one can not remove the file
---
# sticky bit
```
$ ls -l / | grep tmp
drwxrwxrwt 16 root root   4096 3월 15 12:56 tmp
```
---
# sticky bit
```
$ chmod 1775 sticky_test 
$ ls -l | grep sticky_test
drwxrwxr-t 2 greg greg 4096 3월 16 00:12 sticky_test
```