# css
## interpreter
---
## compiler
  - lexer
    - characters -> lexer -> tokens
  - parser
    - tokens -> parser -> parse tree(implicit)

---
## python compiler 
  - source code -> parse tree
  - parse tree ->AST(Abstract syntax tree)
  - build a symbol table
  - AST -> bytecode

---
## token 

```python
#token
>>> import token
>>> token.tok_name
```
---
## example code

```python
#test.py
def func(a, b):
    return a + b

a = 10
b = 20

c = func(a, b)
print(c)
```
---
## tokenize 

```python
#tokenize
>>> from tokenize import tokenize
>>> from io import BytesIO
>>> s = open('test.py').read()
>>> g = tokenize(BytesIO(s.encode('utf-8')).readline)
>>> for token in g:
	print(token)
```
---
## ast 

```python
#ast
>>> import ast
#node 생성
>>> node = ast.parse(s, 'test.py', 'exec')
# yield all descendant nodes
>>> g = ast.walk(node)
#a formatted dump - show the names and the values for fields
>>> ast.dump(node)
```
---
## symtable

```python
#symtable
>>> import symtable
>>> sym = symtable.symtable(s, 'test.py', 'exec')
>>> sym.get_name()
'top'#global table
>>> sym.get_symbols()
[<symbol 'func'>, <symbol 'a'>, <symbol 'b'>, <symbol 'c'>, <symbol 'print'>]

>>> func_sym = sym.get_children()[0]
>>> func_sym.get_symbols()
[<symbol 'a'>, <symbol 'b'>]
```
---
## bytecode

```python
#bytecode
>>> import dis
>>> g = dis.get_instructions(s)
>>> for inst in g:
	print(inst.opname.ljust(20), end = ' ')
	print(inst.argval)
```
---
## PVM
  - stack machine
  - a big loop 

---
## PVM

```python
#dis
>>> dis.dis(s)
```

---
## dis exam

```python
>>> code = compile(s, 'test.py', 'exec')

#in dis.dis(s)
4         8 LOAD_CONST    2 (10)
#4 : line number
#8 : offset from co_code
#2 : co_consts[2]
         10 STORE_NAME    1 (a)

>>> code.co_consts
>>> code.co_names
```







