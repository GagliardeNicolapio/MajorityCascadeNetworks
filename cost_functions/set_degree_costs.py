def set_degree_costs(N,V):
    costs={}
    for v in V:
        cost = round(len(N[v])/2)   #round(1/2) == 0
        if cost!=0:
            costs[v] = cost
        else:
            costs[v] = 1    #arrotondo 0.5 a 1, per problema si divisione per zero
    return costs