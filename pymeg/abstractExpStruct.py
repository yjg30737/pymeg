from abc import ABCMeta


class AbstractExpStruct(metaclass=ABCMeta):
    PLUS = 0
    MINUS = 1
    MULTIPLY = 2
    DIVIDE = 3

    oper_min_cnt = 2
    oper_max_cnt = 8
    oper_cnt = 2

    plus_min = 1
    plus_max = 10

    minus_min = 1
    minus_max = 10

    multiply_min = 1
    multiply_max = 10

    divide_min = 1
    divide_max = 10

    op_dict = {PLUS: '+', MINUS: '-', MULTIPLY: '*', DIVIDE: '/'}

    def __init__(self):
        raise NotImplementedError('abstract base class')