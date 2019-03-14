---
# booting
  - BIOS
    - check hardwares
    - load 512 bytes(master boot record) : where is the boot loader?
---
# GRUB
```
$ sudo vim /etc/default/grub
# GRUB_TIMEOUT_STYLE=hidden
$ sudo update-grub
```
---
# check boot message
```
$ dmesg | more
```
---
# run level
  - 0 : system close
  - 1 : single user mode
  - 2 : multiple user mode
  - 3, 4, 5 : the same as 2
  - 6 : system restart
---
# /etc/rc*.d
```
$ runlevel
$ ls -l /etc/rc2.d
```
---
# shutdown
```
$ sudo shutdown -h now
$ sudo shutdown -h +2
$ sudo shutdown -r +3
$ sudo shutdown -c
```
---
# single user mode
```
ro quiet splash $vt_handoff ->
rw init=/bin/bash

#all done
reboot -f
```

