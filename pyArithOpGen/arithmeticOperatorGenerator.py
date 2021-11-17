import random

from pyArithOpGen.arithmeticOperatorStruct import ArithmeticOperatorStruct


class ArithmeticOperatorGenerator:
    @staticmethod
    def get_problem(problem: ArithmeticOperatorStruct):
        rows = problem.get_op()
        eq = ''
        op_dict = problem.op_dict

        if rows:
            random.shuffle(rows)

            operator_cnt = int(problem.oper_cnt)
            min_n = int(problem.min)
            max_n = int(problem.max)

            for i in range(operator_cnt-1):
                op = op_dict[random.choice(rows)]
                suffix = op + str(random.randint(min_n, max_n))
                if eq:
                    eq += suffix
                else:
                    eq += str(random.randint(min_n, max_n))+suffix

        return eq