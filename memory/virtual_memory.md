## MMU
  - Memory Management Unit
  - run-time mapping 
  - from logical address to physical address
---
## virtual memory
  - original idea
    - to expand the physical memory
    - main memory + page file
---

## page
- page size : typically between 1KB and 8KB
- 4096 bytes(2^12)  
- in Virtual Address Space
---

## paging
  - the number of pages
  - 2^32 / 2^12 = 2^20
  - page number -> 20 bit
  - offset -> 12 bit
  - page number + offset -> address in VAS
---

## page frame
  - 4096 bytes(2^12)
  - in main memory
  - frame number
---

---
## page table
  - page number, frame number , valid bit
  - PTBR(page table base register)
    - points to PTBA(page table base address)
---

## page table
  - page table is essentially the Virtual Memory 
---

## from logical address to physical address
  - MMU references PTBR
  - page # from PC
  - frame # from page table
  - physical addr = frame # + offset
  - physical addr in MAR(memory address register)
---

## demand paging
  - 프로세스 실행할 때 필요한 페이지만 메모리에 올린다

---
## page fault
  - CPU가 요청한 페이지가 메인 메모리에 없을 때
  - victime page
    - the page from main memory to page file
  - page out
    - main memory -> page file
  - page in
    - page file -> main memory
---

## Translation Lookaside Buffer(TLB)
  - cache to store the recently used pages of the page table
  - MMU tries to read the frame number from the TLB
  - TLB hit
    - page found in the TLB
  - TLB miss
    - page not found
    - insert the item into TLB from page table
---

