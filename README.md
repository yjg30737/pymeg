# pymeg

## Table of Contents
* [General Info](#general-info)
* [Class Overview](#class-overview)
* [Setup](#setup)
* [Overall Example](#overall-example)

## General Info
Python mathematical expression generator

## Class Overview
* AbstractExpStruct

Abstract class of ExpStruct. 

This class has four constants.
```python
AbstractExpStruct.PLUS = 0
AbstractExpStruct.MINUS = 1
AbstractExpStruct.MULTIPLY = 2
AbstractExpStruct.DIVIDE = 3
```

* ExpStruct

Class which can store the rules of expression. inherits the AbstractExpStruct.

ExpStruct has methods like below.
```python
set_op(lst) # set the operators to be used to expression to generate as AbstractExpStruct's constant. 
# For example, if you want to use only plus and minus then write like this
# expStruct.set_op([AbstractExpStruct.PLUS, AbstractExpStruct.Minus])

get_op() -> self.__op_lst # get the operators to be used as list of AbstractExpStruct's constant.

set_oper_cnt(cnt) # set the number of operands of expression to be generated.

set_min(min_) # set minimal operand's integer to used.

set_max(max_) # set maximum
```

* ExpGenerator

Class which generate the randomized expression with given ExpStruct instance
Using `get_problem` static method to generate the expression. Argument is `ExpStruct`.
Result is string-typed mathematical expression.
```
problem = ExpStruct()
ExpGenerator.get_problem(problem)
```

## Setup
```
$ pip install git+https://github.com/yjg30737/pymeg.git
```

## Overall Example
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

