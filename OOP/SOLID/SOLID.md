# SOLID
  - Single responsibility principle
  - Open-closed principle
  - Liskov substitution principle
  - Interface segregation principle
  - Dependency inversion principle

---
## Single responsibility principle
  - class should have A responsibility
  - "A class should have only one reason to change"
---
---
## Single responsibility principle
```python
class Stat: # only one for statistics
	pass
class DataHandler: # only one for data 
	pass
```
---
---
## Open-closed principle
  - classes should be open for extension, but closed for modification
---
---
## Open-closed principle
```python
class Stat:
    # add some functions
class DataHandler:
    # NO CHANGES
```
---
## Liskov substitution principle
  - objects of subtype S can be replaced with objects type P
  - if f(x) is ok when objects x of type P then f(y) must be ok when objects y of subtype S  
---
---
## Interface segregation principle
  - A client should depend on methods it does use
  - keep a system decoupled->easier to refactor, change
---
---
## Dependency inversion principle
  - decoupling modules
  - High-level modules should not depend on low-level modules
  - Both should depend on abstractions
  - Abstraction should not depend on details
  - Details should depend on abstractions
---
  