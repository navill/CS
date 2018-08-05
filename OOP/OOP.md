# Computer Science School
## OOP
---
## Procedural vs Object-Oriented
  - procedural
    - 이 프로그램은 어떤 일을 하는가?
    - 함수를 이용
  - Object-Oriented
    - 현실 세계에 존재하는 객체(object)를 어떻게 모델링(modeling)할 것인가?
    - 객체를 이용
---
## Object-oriented
  - 객체(Object)
    - attribute(속성)
      - member(변수)
        - 각각의 객체가 가지는 값
      - method(함수)
        - 객체가 할 수 있는 행동, 기능
---

## attribute
```python
class Person:
    #모든 사람은 이름과 나이, 돈을 갖는다.
    def __init__(self, name, age, money):
        self.name=name
        self.age=age
        self.money=money
```
---
## attribute
```python
class Person:
    #__init__ 생략
	
    #모든 사람은 음식을 먹는 행동을 할 수 있다.
    def eat(self, food):
        print('{} eats {}'.format(self.name, food))

    def get_age(self):
        self.age+=1
    
    def earn_money(self, money):
        self.money+=money
```
---
## attribute
```python
if __name__=="__main__":
    #모든 사람은 각자 다른 이름, 나이, 돈을 가진다.
    greg=Person('greg', 36, 4000)
    mark=Person('mark', 24, 1000)
```
---

## Encapsulation
  - 멤버(변수)와 메서드(함수)를 하나의 단위(대부분 클래스)로 묶는 것
  - the bundling of data with methods
  - 정보 은닉을 포함 
---

## message passing
```python
class Person:
    def __init__(self, name, money):
        self.name=name
        self.money=money

    def give_money(self, other, money):
        self.money-=money
        #message passing
        other.get_money(money)

    def get_money(self, money):
        self.money+=money
```
---

## message passing
```python
if __name__=="__main__":
    greg=Person('greg', 5000)
    mark=Person('mark', 2000)

    #message passing
    greg.give_money(mark, 2000)	
```
---

## difference between functions and methods
```python
>>> type(Person.give_money)
<class 'function'>
>>> type(greg.give_money)
<class 'method'>
```
---

## method
```python
>>> greg.give_money.__func__ is Person.give_money
True
>>> greg.give_money.__self__ is greg
True
```
---

## account - class member and class method
```python
class Account:
    #class member
    num_acnt=0

    @classmethod
    def get_num_acnt(cls):
        return cls.num_acnt
```
---
## account - instance member
```python
def __init__(self, name, money):
        #instance member
        self.user=name
        self.balance=money
        Account.num_acnt+=1
```
---

## account - instance method
```python
def deposit(self, money):
        if money < 0:
            return
        self.balance+=money
```
---

## static method and class method
```python
class Base:
    @staticmethod
    def f():
        print('static method')

    @classmethod
    def g(cls):
        print(cls.__name__)
```
---

## static method and class method
```python
>>> type(Base.f)
<class 'function'>
>>> type(Base.g)
<class 'method'>
```
---

## alternative constructor
```python
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    @classmethod
    def init_from_string(cls, string):
        """
        string format:<name>_<age>
        """
        name, age=string.split('_')
        return cls(name, int(age))
```
---

## alternative constructor
```python
p=Person.init_from_string('greg_30')
```
---

## information hiding
  - restrict direct access to member or method
  - hide a member from user
  - allow access by access functions
```python
>>> class Base:
	def __init__(self, data):
		self.__data = data
	def get_data(self):
		return self.__data
	def set_data(self, data):
		self.__data = data
```
---
## information hiding
  - access modifiers
    - public, protected, private in C++
```C++
class Base{
private:
	int x;
public:
	int get_x() { return x; }
	void set_x(int n) { x = n; }
};
```  
---
---
## information hiding
  - python DO NOT support Information hiding
```python
>>> class Base:
	def __init__(self, n):
        #looks like information hiding......
		self.__x = n	
>>> b = Base(5)
>>> b.__x
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    b.__x
AttributeError: 'Base' object has no attribute '__x'
```
---
## information hiding
```python
# it is not information hiding
>>> b.__dict__
{'_Base__x': 5}
>>> b._Base__x
5
```
---
## information hiding
```python
>>> class Base:
	def __f(self):
		print('__f executed')		
>>> b = Base()
>>> b.__f()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    b.__f()
AttributeError: 'Base' object has no attribute '__f'
```
---
## information hiding
```python
>>> dir(b)
['_Base__f', '__class__', ...]
>>> b._Base__f()
__f executed
```