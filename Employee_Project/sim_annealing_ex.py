from random import random

e = 2.71828

def anneal(solution):
    old_cost = cost(solution)
    T = 1.0
    T_min = 0.00001
    alpha = 0.9
    while T > T_min:
        i = 1
        while i <= 100:
            new_solution = neighbor(solution)
            new_cost = cost(new_solution)
            ap = acceptance_probability(old_cost, new_cost, T)
            if ap > random():
                solution = new_solution
                old_cost = new_cost
            i += 1
        T = T*alpha
    return solution, old_cost

"""Where neighbor(solution), cost(solution), and acceptance_probability(old, new, T) must be defined separately"""

def acceptance_probability(old_cost, new_cost, T):
    ap = e**((old_cost - new_cost)/T)
    return ap