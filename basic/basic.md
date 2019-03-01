# why python
```python
>>> import this
```
--- 
# what can we do with python
  - web-application
  - database programming
  - data science (especially machine learning)
  - science related
  - hacking!!
---
# data type - numbers
```python
>>> a=10
>>> b=2.718 
```
---

---
# data type - boolean
```python
>>> c=True
>>> d=False
```
---
---
# data type - string
```python
>>> e="abcde"
```
---
---
# data structure - list
```python
>>> li=[1, 2, 3, 4]
>>> li2=[]
```
---

---
# data structure - tuple
```python
>>> tu=(1, 2, 3, 4)
>>> tu2=()
```
---

---
# data structure - set
```python
>>> s=set([1, 2, 2, 2, 3])
>>> s
{1, 2, 3}
>>> s=set()
>>> s
set()
```
---
---
# data structure - dictionary
```python
>>> dic={'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}
>>> dic2={}
```
---
---
# operator 
```python
>>> 10/3
3.3333333333333335
>>> 10//3
3
>>> 2**2
4
>>> 2**4
16
```
---

---
# operator
## objects as False
  - None, [], {}, (), set(), "", 0
```python
>>> not [1, 2]
False
>>> not []
True
>>> [] and [3, 4]
[]
>>> (1,) and [2, 3]
[2, 3]
```

---

---
# if else
```python
a=int(input("number : "))

if a > 10:
    print("a is greater than 10")
else:
    print("a is less than or equal to 10")
```
---

---
# ternary operator
```python
>>> 10 if a == 10 else -10
```
---
---
# for
```python
li=[1, 2, 3, 4]

for e in li:
    print(e)
```
---

---
# while
```python
a= 10

while a > 5:
    print(a)
    a-=1
```
---

---
# function
```python
def func(a, b):
    c=a+b
    return c

func(1, 2)
```