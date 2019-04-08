# regular expression
---
# re
```
>>> import re
```
---
# [ ]
```python 
# [] : one character
>>> m=re.match(r'[a-zA-Z]+', 'cat123')
>>> m.group()
```
---
# ^
```
# ^ : start of string
>>> re.search(r'^get', 'get donut')
>>> re.search(r'^get', 'donut get')
>>> re.search(r'get', 'donut get')
```
---
# $
```
# $ : end of string
>>> re.search('donut$', 'get donut')
>>> re.search('donut$', 'donut get')
>>> re.search('donut', 'donut get')
```
---
# how many characters 
```
# * : more than 0
>>> re.match(r'a*', 'bc')
```
---
# how many characters
```
# + : more than once
>>> re.match(r'a+', 'bc')
>>> re.match(r'a+', 'abc')
>>> re.match(r'a+', 'aaab')
```
---
# how many characters
```
# ? : 0 or 1
>>> re.match(r'a?', 'bc')
>>> re.match(r'a?', 'abc')
>>> re.match(r'a?', 'aaaabc')
```
---
# how many characters
```
>>> re.match(r'a{2,3}', 'a')
>>> re.match(r'a{2,3}', 'aa')
>>> re.match(r'a{2,3}', 'aaa')
>>> re.match(r'a{2,3}', 'aba')
```
---
# special character
```
# \\ : \
# \d : [0-9]
# \D : [^0-9]
# \s : white space
# \S : not white space
# \w : [a-zA-Z0-9]
# \W : [^a-zA-Z0-9]
```
---
# cell number 
```
>>> pattern=r'\d{3}-?\d{3,4}-?\d{4}'
>>> re.search(pattern, '010-1111-2222')
>>> re.search(pattern, '01011112222')
```
---
# email
```
>>>pattern=\
r'([a-zA-Z0-9_]+)@([a-zA-Z0-9]+)\.([a-zA-Z0-9]+)' 
>>>string=\
"my email address is abcde@gmail.com"
>>>re.search(pattern, string)
```