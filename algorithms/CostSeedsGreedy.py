
from math import ceil

# f da massimizzare
def f1(V, N, Sd):
    result = 0
    for v in V:
        result += min(len(N[v].intersection(Sd)),ceil(len(N[v]) / 2))
    return result

# delta_v f(D) = f(D unito v) - f(D) and f is f1
def delta_v_f1(v,Sd,N,V):
    x = f1(V,N,Sd)
    Sd.add(v)
    return f1(V,N,Sd) - x

# controlla se c'è qualche altro nodo che rientra nel dubget rimanente
def there_is_node_cost_min(G, remaining_cost, c):
    for v in G.nodes():
        if c[v] <= remaining_cost:
            return True
    return False

def cost_seeds_greedy(G, k, c):
    #seed set, insieme nodi, vicini, costo seed set, nodi con costo maggiore del budget restante
    Sp = set()
    Sd = set()
    V = set(G.nodes())
    N = {v: set(G.neighbors(v)) for v in G.nodes}
    Sd_cost = 0
    nodi_esclusi = set()

    while True:
        #prendo il nodo che massimizza f1 escludo quelli già presi e quelli che non rientrano nel budget
        argmax = 0
        u = 0
        for v in V.difference(Sd).difference(nodi_esclusi):
            delta = delta_v_f1(v,Sd,N,V)/c[v]
            if u < delta:
                u = delta
                argmax = v

        #prima c'era anche argmax==0 or
        if  Sd_cost + c[argmax] > k:
            #controllo se c'è ancora qualche nodo che rientra nel budget
            if there_is_node_cost_min(G, k-Sd_cost,c):
                nodi_esclusi.add(argmax) #escludo il nodo che massimizza f perche supera il budget disponibile
            else:#stop se non c'è nessun altro nodo che rientra nel budget
                print("costo: "+str(Sd_cost))
                return Sp

        #prima c'era anche argmax!=0 and
        if Sd_cost + c[argmax] <= k: #il nodo che massimizza la fun ha costo minore del budget rimanente
            Sd_cost += c[argmax]
            Sp.add(argmax)
       # elif argmax != 0 and Sd_cost + c[argmax] > k:
        #    nodi_esclusi.add(argmax)

        Sd =Sp.copy()