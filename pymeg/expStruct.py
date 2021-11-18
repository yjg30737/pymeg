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

    def set_min(self, min_):
        ExpStruct.min = min_

    def set_max(self, max_):
        ExpStruct.max = max_
