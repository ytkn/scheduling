# coding: utf-8

import pulp
import random
import numpy as np


def main():
    problem = pulp.LpProblem(name='test', sense=pulp.LpMinimize)

    # 変数の宣言
    x = pulp.LpVariable(name='x', cat=pulp.LpContinuous)
    t = pulp.LpVariable(name='t', cat=pulp.LpContinuous)

    # 目的関数
    problem.objective += t

    problem.addConstraint(t >= x)
    problem.addConstraint(t >= 2-x)

    status = problem.solve()
    print(pulp.LpStatus[status])
    print("目的関数値 = {}".format(pulp.value(problem.objective)))

    print(problem.constraints)
    print(f'x : {pulp.value(x)}')


if __name__ == '__main__':
    main()
