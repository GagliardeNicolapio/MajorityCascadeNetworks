
def check_neighbors(G,v,stato_dei_nodi):
    num_neigh = len(set(G.neighbors(v)))
    count = 0
    for n in G.neighbors(v):
        if stato_dei_nodi[n] == 1:
            count+=1

    return True if count>=(num_neigh/2) else False


def influence_diffusion(G, seed_set):
    # stato 0 = non influenzato, 1 = influenzato
    stato_dei_nodi = {}
    for v in G.nodes():
        stato_dei_nodi[v] = 0

    for v in seed_set:
        stato_dei_nodi[v] = 1

    print("stato dei nodi")
    print(stato_dei_nodi)

    count=0
    while True:
        flag = False
        for v in G.nodes():
            if check_neighbors(G, v, stato_dei_nodi) and stato_dei_nodi[v]==0:
                stato_dei_nodi[v] = 1
                flag = True
                count+=1
                print("setto "+str(v)+" a 1")

        if not flag:
            break

    return stato_dei_nodi, count