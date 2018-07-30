# css
## lambda, map, filter, reduce
--- 
## lambda
  - 익명 함수
  - 자주 사용하지 않을 때 편리
  - return 문이 없다
  - body는 오직 expression<식>만 올 수 있다.

---
## lambda

```python
#일반 함수
def adder(a, b):
    return a + b
a = 10
b = 20
adder(a, b)
```
---
## lambda

```python
#return문이 없다
f = lambda a, b: a + b
a = 10
b = 20
f(a, b)
```
---
## lambda

```python
#주변에 있는 변수를 가져다 몸체에서 쓸 수 있다
li = [1, 2, 3, 4]
f = lambda idx: li[idx] ** 2

for i in range(4):
    print(f(i))
```
---
## lambda

```python
#몸체에 문이 오면 error가 난다
f = lambda idx, data: li[idx] = data

SyntaxError: can't assign to lambda
```

---
## lambda

```python
#lambda 사용 예제

li = [i for i in range(1, 11)]

# lambda 사용하지 않을 때

def pred(a):
    return a % 2 == 0
li.sort(key = pred)

```
---
## lambda

```python
#lambda를 사용할 때
#여러 줄 코딩을 할 필요 없고
#한번만 사용할 함수를 대체할 수 있다
li.sort(key = lambda a: a%2==0)
```

---
## map

```python
#Y = f(X)

#일반 함수 사용
li = [1, 2, 3, 4]
def square(x):
    return x ** 2
m = map(square, li)

for e in m:
    print(e)
```
---
## map

```python
#lambda 사용
li = [1, 2, 3, 4]
m = map(lambda x: x**2, li)
for e in m:
    print(e)
```

---
## filter

```python
#filter 함수
#조건에 True인 것만 골라낸다
li = [1, -2, 4, -6, 0, 8]
#filter 객체로 iterator이다
f = filter(lambda x: x > 0, li)
```

---
## why map & filter ?
  - 게으른 연산(Lazy evaluation)
    - 필요할 때만 연산을 수행
    - 성능 개선

---
## why map & filter ?
```python
def square(x):
    print('square executed')
    return x ** 2

li = [1, 2, 3, 4]

m = map(square, li)
```

---
## Quiz
```python
#양수만 제곱한 값으로 리스트를 만드시오.
li = [1, -2, 2, -6]
```
---
## Answer
```python
#양수만 제곱한 값으로 리스트를 만드시오.
li = [1, -2, 2, -6]
list(
    map(lambda x: x ** 2,
       filter(lambda x: x > 0, li)))
```
---
## reduce

```python
#reduce
from functools import reduce

```
---
## reduce

```python
#사용법 
#sequence 자료형을 하나의 값으로

#reduce(function, sequence[, initial]) -> value
#함수는 두 개의 인자를 받음
#sequence 자료형에서 두 개씩 가져온 후 연산해 
#한 개의 값으로 치환

li = [i for i in range(1, 101)]
reduce(lambda a, b: a + b, li)
```
---
## reduce

```python
#최대값 산출
li = [4, -6, 12, -7, 2, 7, 9]
reduce(
    lambda a, b:
        a if a > b
        else b,
    li)
```
---
## reduce

```python
li = ['a', 'b', 'a', 'c', 'a', 'b']
#{'a' : 3, 'b' : 2, 'c' : 1}
dic = reduce(
    lambda result, ch:
        result.update({ch : result.get(ch, 0)+1}) or result,
    li, {})
```





