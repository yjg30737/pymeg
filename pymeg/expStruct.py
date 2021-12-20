from pymeg.abstractExpStruct import AbstractExpStruct


class ExpStruct(AbstractExpStruct):
    def __init__(self):
        self.__op_lst = [AbstractExpStruct.PLUS,
                         AbstractExpStruct.MINUS,
                         AbstractExpStruct.MULTIPLY,
                         AbstractExpStruct.DIVIDE]

    def set_op(self, lst):
        self.__op_lst = lst

    def get_op(self):
        return self.__op_lst

    def set_oper_cnt(self, cnt):
        ExpStruct.oper_cnt = cnt

    def set_range(self, min_, max_, types: list):
        for type in types:
            if type == ExpStruct.PLUS:
                ExpStruct.plus_min = min_
                ExpStruct.plus_max = max_
            elif type == ExpStruct.MINUS:
                ExpStruct.minus_min = min_
                ExpStruct.minus_max = max_
            elif type == ExpStruct.MULTIPLY:
                ExpStruct.multiply_min = min_
                ExpStruct.multiply_max = max_
            elif type == ExpStruct.DIVIDE:
                ExpStruct.divide_min = min_
                ExpStruct.divide_max = max_
            else:
                continue