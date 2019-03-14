---
# apt-get
```
# /etc/apt/sources.list sync
$ sudo apt-get update 
# upgrade packages installed
$ sudo apt-get upgrade 
$ sudo apt-get install
# leave conf files
$ sudo apt-get remove
# with all of conf files
$ sudo apt-get purge
```
---
# apt-get
```
# just download NO INSTALLATION
$ sudo apt-get download 
# download source code
$ sudo apt-get --download-only source 
$ sudo apt-get --compile source 
```
---
# dpkg
```
$ dpkg -l 
$ dpkg -s <package>
$ sudo dpkg -i *.deb
$ sudo dpkg -r <package>
# remove all confs
$ sudo dpkg -P <package>
```
---
# tar
```
# c : create 
# v : print info of files 
# f : consider the next name as the name of archive 
$ tar cvf exam.tar exam1.txt exam2.txt exam3.txt
```
---
# tar
```
# t : table of contents
$ tar tvf exam.tar
```
---
# tar
```
# x : extract
$ tar xvf exam.tar
```
---
# tar
```
# u : update 
# if the file exists then just update
# if the file doesn't exist then add the file
$ tar uvf exam.tar exam4.txt
```
---
# tar
```
# r : replace
# add the file to the tar file
# even though it has already
$ tar rvf exam.tar exam3.txt
```
---
# tar
```
# archiving and compression simultaneously
$ tar cvzf exam.tar exam1.txt exam2.txt exam3.txt
```
---
# gzip
```
$ gzip exam.txt
$ gzip -l exam.txt.gz
```
---
# zcat
```
$ zcat exam.txt.gz
```
---
# gunzip
```
$ gunzip exam.txt.gz
```



