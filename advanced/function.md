# Computer Science Bootcamp
## functions

---
## * args

```python
# *args의 형태
# tuple의 형태로 받는다
def func1(*args):
	print(args)
a = [1, 2, 3]
#unpacking 안 했을 때
func1(a)
#unpacking
func1(*a)
```

---
## ** kwargs

```python
# **kwargs의 형태
# dictionary의 형태로 받는다
def func(**kwargs):
    print(kwargs)
    
func2(a = 10, b = 20)
```

---
## * args and **kwargs

```python
# *args, **kwargs를 함께 쓰는 형태
def func3(*args, **kwargs):
    print(args)
    print(kwargs)

a = [1, 2, 3]
func(*a, b = 10, c = 20)
```
---

## first class function
  - 함수를 인자로 전달
  - 함수를 반환
  - 변수에 저장 
---

## first case - argument
```python
#argument
def f(a, b):
    return a + b

#함수 f를 인자로 전달
def g(f, a, b):
    return f(a, b)
```
---

## second case - return
```python
#return 
def calculator(kind = 'add'):
    def add(a, b):
        return a + b
    def subtract(a, b):
        return a - b
    
    if kind == 'add':
        return add
    else:
        return subtract
```
---

## third case - variable 
```python
#variable
def adder(a, b):
    return a + b
    
#함수를 변수에 할당해 사용
func_var = adder
```
---

## closure
  - 함수 내 함수를 반환 받아 사용
  - free variable : 서로 다른 정보를 가진다
---

## closure

```python
def account(name, m):
    #account의 지역 변수 name, m
    def add(money):
    	#free variable을 변경하기 위해
        nonlocal m
        m += money
        #free variable name도 접근은 ok!
        return name, m
    #함수 내 함수 add를 반환
    return add
```
---

## closure

```python
#둘 모드 account 함수를 통해 add 함수를 받고 있지만
# f1은 내부 데이터 정보로 'yang'과 1000을
#f2는 내부 데이터 정보로 'kim'과 500을 
#각각 가지게 된다
f1 = account('yang', 1000)
f2 = account('kim', 500)
```
---

## closure

```python
#두 함수의 결과는 당연히 다르다.
f1(200)
f2(600)
```
---
## function object
```python
#code object
f1.__code__
#global table
f1.__globals__
```
---
## function object
```python
#두 함수는 다르다
>>> f1 == f2
False
```
---
## code object
```python
#두 함수의 코드 오브젝트는 같다
>>> f1.__code__ == f2.__code__
True
```
---
## closure  
```python
#f1 함수의 code object를 받아서
>>> code_obj = f1.__code__
#지역 변수를 확인해보면
>>> code_obj.co_varnames
('money',)
#free variable을 확인해보면
>>> code_obj.co_freevars
('m', 'name')
```
---
## closure  
```python
#함수의 클로저의 cell에
#free variable 값이 저장

>>> cells = f1.__closure__
>>> cells
(<cell at 0x04133970: int object at 0x04160EC0>, <cell at 0x037D0C30: str object at 0x04171320>)
```
---
## closure  
```python
#돈의 액수인 m과 계좌 주인인 이름이 있어야 한다.
>>> cells[0].cell_contents
1000
>>> cells[1].cell_contents
'greg'
```







