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

set_range(min_, max_, types: list) # set min, max number to use of types(plus, minus ...).

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
pip3 install git+https://github.com/yjg30737/pymeg.git --upgrade
```

## Example
```python

from pymeg.expGenerator import ExpGenerator
from pymeg.expStruct import ExpStruct

problem = ExpStruct()
problem.set_oper_cnt(4)
problem.set_range(20, 100, [ExpStruct.PLUS, ExpStruct.MINUS])
problem.set_range(2, 10, [ExpStruct.MULTIPLY])
problem.set_range(2, 4, [ExpStruct.DIVIDE])
print(ExpGenerator.get_problem(problem))
print(ExpGenerator.get_problem(problem))
print(ExpGenerator.get_problem(problem))
ext = ExpGenerator.get_problem(problem)
print(ext)
print(eval(ext))
```

## Result
Note: Problem will be generated randomly depending on operation count set by user or anything like that.
```python
54+25-54*9
6*6-31/3
2/4*8/3
9*3*6/2
81.0
```
