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
