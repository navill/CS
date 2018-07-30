# css
## decorator
---
## decorator 

함수에 기존 함수의 기능을 추가하고 싶을 때 

---
## decorator 

```python
#overwrite되어 마지막에 정의된 func만 유효
def func(a, b):
    return a + b

def func(a, b):
    return a * b
```

---
## decorator

```python
#decorator
def outer(org_func):
    def inner(*args, **kwargs):
        print("Things")
        return org_func(*args, **kwargs)
    return inner

```
---
## decorator

```python
def func(a, b):
    return a + b

print(func.__name__)#func
func = outer(func)
print(func.__name__)#inner
```
---
## decorator 

```python
func = outer(func)

@outer
def func(a, b):
    return a + b
```
---
## decorator  

```python
#function call counter
def call_counter(org_func):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print('function call : {}'.format(cnt))
        return org_func(*args, **kwargs)
    return inner
```

---
## decorator 

```python
@call_counter
def func(a, b):
    return a + b

for i in range(1, 10):
    a = i + 1
    b = i + 2
    result = func(a, b)
    print('{} + {} = {}'.format(a, b, result))
```
---
## decorator 

```python
#timer
import time
def timer(org_func):
    @wraps(org_func)
    def inner(*args, **kwargs):
        start = time.time()
        result = org_func(*args, **kwargs)
        elapsed = time.time() - start
        print("elapsed time : {}".format(round(elapsed, 1)))
        return result
    return inner
```
---
## decorator 

```python
@timer
def func(a, b):
    #pause
    time.sleep(5)
    return a + b

func(1, 2)
```
---
## decorator 

```python
from functools import wraps
```
---
## decorator 

```python
def outer(org_func):
    @wraps(org_func)
    def inner(*args, **kwargs):
        print("Things")
        return org_func(*args, **kwargs)
    return inner
```








