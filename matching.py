import pulp
import numpy as np
import random
import itertools


def main():
    n = 5
    W = np.zeros([n, n])
    for i, j in itertools.product(range(5), range(5)):
        W[i, j] = random.randint(1, 10)

    problem = pulp.LpProblem(
        name='weighted_bipartite_matching', sense=pulp.LpMaximize)

    x = {(i, j): pulp.LpVariable(name='x_{}_{}'.format(i, j), cat='Binary')
         for i, j in itertools.product(range(n), range(n))}

    problem += pulp.lpSum([W[i, j]*x[i, j]
                           for i, j in itertools.product(range(n), range(n))])

    for i in range(n):
        problem.addConstraint(
            (pulp.lpSum([x[i, j] for j in range(n)]) == 1), "job_limitation_{}".format(i))

    for j in range(n):
        problem.addConstraint(
            (pulp.lpSum([x[i, j] for i in range(n)]) == 1), "employee_limitation_{}".format(j))

    status = problem.solve()
    print(pulp.LpStatus[status])
    print("objective value = {}".format(pulp.value(problem.objective)))
    print("====== problem instance =======")
    for i, j in itertools.product(range(n), range(n)):
        print(int(W[i, j]), end="\n" if j == n-1 else " ")

    print("====== solution =======")
    for i, j in itertools.product(range(n), range(n)):
        print(int(pulp.value(x[i, j])), end="\n" if j == n-1 else " ")


if __name__ == "__main__":
    main()
