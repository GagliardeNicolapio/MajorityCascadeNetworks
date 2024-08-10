# Data una network G=(V,E)
# Dati i costi c:V->N
# Dato budget k
# Trovare seed set S massimale t.c. c(S)<=k e valutare |Inf[S]|
import networkx
#
#
#
#

#cerca il nodo con il valore massimo e con costo <= di quanto posso ancora spendere
def trova_nodo_ottimale(val_no_neighbors, c, totale):
    nodo_ottimale = None
    valore_max = -float('inf')  # Inizializza con un valore molto piccolo

    for nodo, valore in val_no_neighbors.items():
        if valore > valore_max and c[nodo] <= totale:
            nodo_ottimale = nodo
            valore_max = valore

    return nodo_ottimale

# true se c'è un nodo che posso ancora comprare
def there_is_node_cost_min(G, remaining_cost, c):
    for v in G.nodes():
        if c[v] <= remaining_cost:
            return True
    return False

def costMajorityCascadeProblem(G,c,k):

    total_cost = 0
    S = set()

    val = {v: len(set(G.neighbors(v))) for v in G.nodes} #ogni nodo ha un valore = al num di adiacenti

    nodo_precedente = False
    while there_is_node_cost_min(G,k-total_cost,c): # finche c'è un nodo il cui costo è minore di k-total_cost
        if nodo_precedente:
            neighbors_nodo_prec = set(G.neighbors(nodo_precedente))  # per la scelta del nuovo nodo

            G.remove_node(nodo_precedente)  # rimuovo da G e ricalcolo val
            val = {v: len(set(G.neighbors(v))) for v in G.nodes}

            val_no_neighbors = val.copy()

            for chiave in neighbors_nodo_prec:                  #non considero i vicini del nodo precedente
                if chiave in val_no_neighbors:
                    val_no_neighbors.pop(chiave)

            # prendo il nodo con il val massimo e che non si trova nel vicinato del nodo
            # precedente e il cui costo <= k-total cost
            nodo_val_max = trova_nodo_ottimale(val_no_neighbors, c, k-total_cost)

        else:
           nodo_val_max = trova_nodo_ottimale(val, c, k-total_cost)
           # nodo_val_max = max(val, key=val.get)           #prendo il nodo con il val massimo

        if nodo_val_max is None:
            break

        nodo_precedente = nodo_val_max

        if c[nodo_val_max] + total_cost <= k:
            S.add(nodo_val_max)
            total_cost+=c[nodo_val_max]
        else:
            break
    print("costo")
    print(total_cost)
    return S