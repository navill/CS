---
# user info
```
# loginID:X:UID:GID:DESCRIPTION:home_directory:shell
$ cat /etc/passwd
```
---
# passwd info
```
# loginID:passwd:last_modified:....
$ sudo cat /etc/shadow
```
---
# group info
```
# group:x:GID: member
$ cat /etc/group
```
---
# group passwd info
```
$ sudo cat /etc/gshadow
```
---
# useradd
```
# add user and create home directory
$ sudo useradd -s /bin/sh -m -d /home/john john
```
---
# passwd
```
$ sudo passwd john
```
---
# useradd
```
# print default setting
$ useradd -D
```
---
# userdel
```
# remove home directory and mail directory
$ userdel -r john
```
---
# groupadd
```
$ sudo groupadd cs10
```
---
# groupmod
```
# modify GID
$ sudo groupmod -g 2000 cs10
```
---
# groupmod
```
# modify group name
$ sudo groupmod -n wps10 cs10
```
---
# groupdel
```
$ groupdel wps10
```
---
# gpasswd
```
# add member
$ sudo gpasswd -a john wps10
```
---
# gpasswd
```
# delete member
$ sudo gpasswd -d john wps10
```
---
# gpasswd
```
# set a passwd
$ sudo gpasswd wps10
```
---
# newgrp
```
# switch to group
$ id
$ newgrp wps10
```
---
# gpasswd
```
# remove passwd
$ sudo gpasswd -r wps10
```
---
# EUID - effective UID
## when UID and EUID are different
  1. setuid in an executable file
  2. su command
---
# id
```
#EUID
$ id
#EUID
$ whoami
#UID
$ who
```
---
# groups
```
$ groups
$ groups john
```
---
# chown
```
# change owner
$ sudo chown john test
$ sudo chown james -R test
```


