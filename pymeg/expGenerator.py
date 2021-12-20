import random

from pymeg.expStruct import ExpStruct


class ExpGenerator:
    @staticmethod
    def get_problem(problem: ExpStruct):
        rows = problem.get_op()
        eq = ''
        op_dict = problem.op_dict

        if rows:
            random.shuffle(rows)

            operator_cnt = int(problem.oper_cnt)
            min_n = int(problem.plus_min)
            max_n = int(problem.plus_max)

            for i in range(operator_cnt-1):
                op_name = random.choice(rows)
                op = op_dict[op_name]

                if op_name == ExpStruct.PLUS:
                    min_n = ExpStruct.plus_min
                    max_n = ExpStruct.plus_max
                elif op_name == ExpStruct.MINUS:
                    min_n = ExpStruct.minus_min
                    max_n = ExpStruct.minus_max
                elif op_name == ExpStruct.MULTIPLY:
                    min_n = ExpStruct.multiply_min
                    max_n = ExpStruct.multiply_max
                elif op_name == ExpStruct.DIVIDE:
                    min_n = ExpStruct.divide_min
                    max_n = ExpStruct.divide_max

                suffix = op + str(random.randint(min_n, max_n))

                if eq:
                    eq += suffix
                else:
                    eq += str(random.randint(min_n, max_n))+suffix

        return eq