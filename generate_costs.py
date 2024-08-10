import networkx as nx
import sys
from algorithms.WTSS import wtss
from algorithms.CostMajorityCascadeProblem import  costMajorityCascadeProblem
from algorithms.CostSeedsGreedy import cost_seeds_greedy
from cost_functions.set_degree_costs import set_degree_costs
from cost_functions.set_random_costs import set_random_costs
from cost_functions.set_inverse_degree_costs import set_inverse_degree_costs

if __name__ == '__main__':
    # remove weight and timestamp from dataset
    with open('insecta-ant-trophallaxis-colony2.edges', 'r') as f_in, open(
            'insecta-ant-trophallaxis-colony2.edges_without_timestamp.txt', 'w') as f_out:
        for line in f_in:
            parole = line.split()
            parole.pop()
            parole.pop()
            riga_modificata = ' '.join(parole) + '\n'
            f_out.write(riga_modificata)

    # load graph
    g = nx.read_adjlist('insecta-ant-trophallaxis-colony2.edges_without_timestamp.txt')
    # nodes
    V = set(g.nodes())
    print("Nodes: ")
    print(V)
    # neighbors
    N = {v: set(g.neighbors(v)) for v in g.nodes}
    print("Neighbors: ")
    print(N)

    c = set_random_costs(V, 1, 10)
    print(c)

    # Apri il file in modalità scrittura
    with open('costi/random_costs.txt', 'w') as file:
        # Iteriamo su ogni coppia chiave-valore del dizionario
        for chiave, valore in c.items():
            # Scriviamo la chiave e il valore su una nuova riga, separati da uno spazio
            file.write(f"{chiave} {valore}\n")

    c = set_degree_costs(N, V)
    print(c)
 # Apri il file in modalità scrittura
    with open('costi/degree_costs.txt', 'w') as file:
        # Iteriamo su ogni coppia chiave-valore del dizionario
        for chiave, valore in c.items():
            # Scriviamo la chiave e il valore su una nuova riga, separati da uno spazio
            file.write(f"{chiave} {valore}\n")

    c = set_inverse_degree_costs(N, V)
    print(c)
    with open('costi/inverse_degree_costs.txt', 'w') as file:
        # Iteriamo su ogni coppia chiave-valore del dizionario
        for chiave, valore in c.items():
            # Scriviamo la chiave e il valore su una nuova riga, separati da uno spazio
            file.write(f"{chiave} {valore}\n")
