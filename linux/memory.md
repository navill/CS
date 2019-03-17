# linux bit architecture
```
$ getconf LONG_BIT
$ arch
$ uname -m 
$ echo $HOSTTYPE
```
---
# python executable bit
```python
>>> import platform
>>> platform.architecture()
('64bit', '')
```
---
# canocical address space
  - 256TB
  - 0x00000000'00000000~0x00007FFF'FFFFFFFF : user space
  - 0xFFFF8000'00000000~0xFFFFFFFF'FFFFFFFF : kernel space
---
# page size 
```
$ getconf PAGE_SIZE
```
---
# page table size
```
$ cat /proc/meminfo | grep PageTables
PageTables:    66336 kB
```
---
# user space
  - user space mem = file-backed + anonymous
    - file-backed : code, data FROM a file
    - anonymous : data NOT FROM a file
---
# page cache 
  - when reading pages from a disk, keep these pages in a cache
  - when reading same pages again, give the pages from the cache
---
# dirty page
  - if CPU modifies a page, 
  - OS marks the page in pagecach as 'dirty page' 
---
# active, inactive
  - Least Recently Used(LRU)
    - active_list : pages that have been accessed 'recently'
    - inactive_list : pages that have not been accesed 'recently'
---
# Cached vs SwapCached
  - cached 
    - pagecache - swapcached
  - swapcached
    - even though swapped-in, still stayed in swap file
    - if swap-out is needed, it saves I/O