import networkx as nx
import sys
from influence_diffusion import influence_diffusion

if __name__ == '__main__':
    g = nx.read_adjlist('insecta-ant-trophallaxis-colony2.edges_without_timestamp.txt')

    seed_set=set()
    with open("seed_sets/degree_costs/wtss60_seedset.txt", 'r') as file:
        for linea in file:
            numeri = linea.split()
            for numero in numeri:
                seed_set.add(numero)

    print("seed set")
    print(seed_set)
    print("inf")
    inf, count = influence_diffusion(g,seed_set)
    print(inf)
    print(count)
    print("end")
    with open("influence_results/degree_costs/wtss60_seedset.txt",'w') as file:
        file.write("Num nodi: "+str(count)+"\n")
        file.write(str(inf))
        file.flush()