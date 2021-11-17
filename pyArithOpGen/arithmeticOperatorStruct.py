from pyArithOpGen.abstractArithmeticOperatorStruct import AbstractArithmeticOperatorStruct


class ArithmeticOperatorStruct(AbstractArithmeticOperatorStruct):
    def __init__(self):
        self.__op_lst = [AbstractArithmeticOperatorStruct.PLUS,
                         AbstractArithmeticOperatorStruct.MINUS,
                         AbstractArithmeticOperatorStruct.MULTIPLY,
                         AbstractArithmeticOperatorStruct.DIVIDE]

    def set_title(self, title):
        self.__title = title

    def set_type(self, type):
        self.__type = type

    def get_title(self):
        return self.__title

    def get_type(self):
        return self.__type

    def set_op(self, lst):
        self.__op_lst = lst

    def get_op(self):
        return self.__op_lst

    def set_oper_cnt(self, cnt):
        ArithmeticOperatorStruct.oper_cnt = cnt

    def set_min(self, min_):
        ArithmeticOperatorStruct.min = min_

    def set_max(self, max_):
        ArithmeticOperatorStruct.max = max_
