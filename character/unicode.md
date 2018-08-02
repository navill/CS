# Computer Science School
## unicode
---

## ASCII
 - 7 bit (2의 7승 : 128 가지 문자)
 - 로마자 및 특수 기호(한글 포함 안됨)
---

## ASCII
```python
>>> ch='A'
>>> bch=ch.encode()
>>> bch
b'A'
>>>bch[0]
65
```
---

## unicode
  - BMP 
    - 기본 다국어 평면
    - U+0000 ~ U+FFFF
    - 한글 및 많은 언어 포함
---

## unicode exam
 - 'A' - U+0041 (ASCII 호환)
 - '가' - U+AC00
---

## unicode exam
```python
>>> '\u0041'
'A'
>>> '\uAC00'
'가'
```
---

## 한글의 범위
  - U+AC00 ~ U+D7AF
```python
>>> '\uAC00'
'가'
>>> '\uB098'
'나'
>>> '\uB2E4'
'다'
```
---

## Code Unit
  - 코드 유닛
  - 코드 포인트를 특정 방법으로 인코딩했을 때 얻어지는 비트의 나열
---

## Character Encoding Scheme(CES)
  - 문자 인코딩 방식
  - 코드 유닛을 옥텟으로 나열하여 변환하는 방법

---
## 유니코드의 부호화 방식
 - UTF-8 
   - 8bit 기반
   - 가변 길이 유니코드 인코딩 시스템 
---
## 유니코드의 부호화 방식
 - UTF-16 
   - BMP
       : 다국어 기본 평면
       : 16 bit
   - SMP 이상 
       : 다국어 보충 평면~
       : 32 bit
---
## 유니코드의 부호화 방식
 - UTF-32
   - 32 bit
---

## 유니코드의 부호화 방식
 - CP949
   - code page 949
   - 통합형 한글 코드( Unified Hangul Code)
   - 현대의 모든 한글 수용
---

## UTF-8 이란?
 - 1 byte ~ 4 byte 
 - U+0000 ~ U+007F(ASCII)
   - 1 byte로 나타낸다
 - 한글 
   - 3byte로 나타낸다
---

## in python
 - 부호화 방식이 UTF-8
```python
>>> coded = "abcde".encode()
>>> coded
b'abcde'
```
---

## in python
 - 부호화 방식이 UTF-8
```python
>>> coded_string = "abcde".encode()
>>> for ch in coded_string:
		print(ch)
97
98
99
100
101
```
---
## in python
 - 부호화 방식이 UTF-8
```python
>>> coded_string = "가".encode()
>>> coded_string
b'\xea\xb0\x80' #3byte
```
---

## '가'의 encoding 과정
 - UTF-8 구조 
   - 0800 - FFFF 
     ==> 1110XXXX 10XXXXXX 10XXXXXX
   - '가'의 유니코드 
     ==> U+AC00
     ==> 1010 1100 0000 0000
     ==> 1010 110000 000000
   - 11101010 10110000 10000000
   - 0xEAB080
   - 즉, 3 바이트로 인코딩
---

## '가'의 encoding 과정
  - 0xEAB080
 ```python
 >>> '가'.encode('UTF-8')
 b'\xea\xb0\x80'
 # EA B0 80
 ```
---


## in python
 - 부호화 방식이 UTF-8
```python
>>> string = coded_string.decode()
>>> string
"가"
```