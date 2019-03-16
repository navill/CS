---
# top
```
$ top
```
---
# %cpu 
  1. us : user 
  2. sy : system
  3. ni : nice
  4. id : idle
  5. wa : IO-wait
  6. hi : hardware interrupts
  7. si : software interrupts
  8. st : stolen by another VM
---
# Mem and Swap
  - Mem : physical memory, RAM
  - Swap : swap space, hard disk
  - buff/cache : to reduce disk access
      - buff : disk writes strored and eventually written later
      - cache : frequently used part of the disk strored
  - Avail Mem : can be allocated without swapping
---
# top
  - f : fields management
    - d : toggles display
  - W : write to ~/.toprc
  - o : add filter 
  - = : removes restrictions on which tasks are shown
---
# fields
  - VIRT
    - virtual image(KiB)
  - USED
    - Res+Swap (KiB)
  - RES
    - Resident(KiB)
  - SWAP
    - Swapped(KiB)
---
# VIRT
  - code + data + shared + pages swapped out + pages not used
  - the same as a virtual address space of a process
---
# example 
```
$ ./top_test &
$ pmap -x <pid>
```
---
# pmap
  - report memory map of a process
  - mem_addr, (4*page#)K, permission, file
---
# example
```
$ fg
# in another shell
$ top
o 
COMMAND=top_test
=
```
---
# RES
  - a subset of the virtual address space (VIRT)
  - the non-swapped physical memory
---
# SWAP
  - the formerly resident portion of a task's address space
---
# USED
  - the non-swapped physical memory (RES)
  - the swapped out portion of its address space(SWAP)
---
# CODE
  - the amount of physical memory devoted to executable code
---
# DATA
  - data + stack
  - the amount of private memory reserved by a process
---
