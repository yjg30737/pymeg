# pymeg
Simple mathematical expression generator

## Usage
```python
from pymeg.expGenerator import ExpGenerator
from pymeg.expStruct import ExpStruct

problem = ExpStruct()
problem.set_oper_cnt(4)
problem.set_min(10)
problem.set_max(100)
print(ExpGenerator.get_problem(problem)) # 84-64-80*22
print(ExpGenerator.get_problem(problem)) # 31/32+36-66
print(ExpGenerator.get_problem(problem)) # 15/61/54/49
ext = ExpGenerator.get_problem(problem)
print(ext) # 39-80*26-55
print(eval(ext)) # -2096
```
Pretty self-explanatory, i suppose.
I will explain more about it later.
