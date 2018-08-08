## CPU 
  - CU(control unit)
  - ALU(arithmetic logic unit)
  - registers
    - instruction register
      - 현재 실행 중인 인스트럭션
    - program counter
      - 다음에 실행할 인스트럭션이 저장된 메모리의 주소값
    - general purpose registers
---
## instruction cycle
  - fetch
  - decode
  - execute
---
## fetch
  - PC -> MAR(memory address register)
  - instruction to MDR(memory data register)
  - MDR -> IR
  - PC increments
---

## decode
  - the instruction is decoded in CU
---

## execute
  - arithmetic or logic in ALU
  - writing back to a register
---

## clock
  - clock pulse
  - cpi(clocks per instruction)
    : 한 인스트럭션이 실행되는데 걸리는 클럭
---


