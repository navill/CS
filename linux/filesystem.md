---
# linux file system
  - ext2
    - 2TB
  - ext3
    - journaling - log for restoring
  - ext4
    - compatible with ext2, ext3
---
# another file system
  - iso9660 : CD-ROM
  - vfat : window 98, NT
---
# special file system
  - swap : for swap area
  - tmpfs : to store in memory
---
# check supported file systems
```
$ cat /proc/filesystems
```
---
# swap partition - 1
```
$ swapon -s # check swap partition
$ sudo fdisk /dev/sdb # create swap partition
$ sudo mkswap /dev/sdb1 # format swap partition
$ sudo swapon /dev/sdb1 # activate swap partition
$ swapon -s # check swap partition
```
---
# mount point
  - mount : connect a file system to a directory
  - mount point : the directory to which a file system is connected to
---
# /etc/fstab
  - file system table
```
$ cat /etc/fstab
UUID=826b6036-4e99-...  /  ext4  errors=remount-ro  0  1
# dev-name  mount-point fs-type  option dumf-conf fsck-op
```
---
# mount 
```
$ mount -t ext4
$ mount -t ext4 /dev/sdb6 /
$ mount -t iso9660 /dev/cdrom /mnt/cdrom
$ mount -t vfat /dev/sdb1 /mnt
# mount [op]  dev  mnt
```
---
# umount
```
$ umount /dev/sdb6
$ umount /mnt
# umount dev or mnt
```
---
# /etc/mtab
  - mount table
```
$ cat /etc/mtab
```
---
# USB memory
```
$ umount /dev/sdc1 # unmount
$ sudo fdisk -l # partition manager
$ sudo fdisk /dev/sdc1 
Command (m for help): m # check menu
Command (m for help): n # create a new partition
partition type
   p   primary
   e   extended
Select (default e): p
Partition number(1-4, default 1): 1
...
Created a new partition 1 of type 'Linux' and ...
Command (m for help): w
```
---
# USB memory
```
# create a file system
$ sudo mke2fs -t ext4 /dev/sdc1
# mount
$ sudo mount /dev/sdc1 /mnt
# unmount
$ sudo umount /mnt
```
---
# USB memory - windows
```
$ umount /dev/sdc1
$ sudo fdisk -l
$ sudo mount -t vfat /dev/sdc1 /mnt
$ sudo umount /mnt
```
---



