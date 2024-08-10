#G = graph, t = tresholds, c = costs
import networkx as nx

def exist_node_t0(U, t):
    for v in U:
        if t[v]==0:
            return v
    return False

def exist_node_degree_min_k(G, k):
    for v in G.nodes():
        if G.degree(v) < k[v] or G.degree(v) == 0:
            return v
    return False

def remove_nodes_over_cost_limit(G,U,c,total_cost,k):
    V = set(G.nodes())
    for v in V:
        if c[v] > (k - total_cost):
            G.remove_node(v)
            U.remove(v)
    return G,U

def wtss(G, c, k):
    S = set()
    U = set(G.nodes)
    t = {v: G.degree(v) // 2 for v in G.nodes}
    k_t = t.copy()
    total_cost = 0
    while U != set():

        v = exist_node_t0(U, t)
        if v:
            for u in G.neighbors(v):
                k_t[u] = max(0, k_t[u]-1)
        else:
            v = exist_node_degree_min_k(G, k_t)
            if v:
                if total_cost + c[v] > k:
                    break
                total_cost += c[v]
                S.add(v)
                for u in G.neighbors(v):
                    k_t[u] = k_t[u]-1
            else:
                v = False
                prec_x = 0
                for u in U:

                    x = (c[u]*k_t[u])/(G.degree(u)*(G.degree(u)+1))
                    if prec_x < x:
                        v = u
                        prec_x = x


        G.remove_node(v)
        U.remove(v)
        G, U = remove_nodes_over_cost_limit(G,U,c,total_cost,k)
    print("costo totale")
    print(total_cost)
    return S
