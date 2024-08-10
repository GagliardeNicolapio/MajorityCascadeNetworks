import random


def set_random_costs(V, start, end):
    costs = {}
    for v in V:
        costs[v] = random.randrange(start,end)
    return costs
