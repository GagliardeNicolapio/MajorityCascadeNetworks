# INPUT: network file, numAlgo (1=costseedsgreedy, 2=wtss, 3=costmajcascadeprob), numAlgoCosti (1=random, 2=degree)
import networkx as nx
import sys
from algorithms.WTSS import wtss
from algorithms.CostMajorityCascadeProblem import  costMajorityCascadeProblem
from algorithms.CostSeedsGreedy import cost_seeds_greedy
from cost_functions.set_degree_costs import set_degree_costs
from cost_functions.set_inverse_degree_costs import set_inverse_degree_costs
from cost_functions.set_random_costs import set_random_costs

if __name__ == '__main__':
    # remove weight and timestamp from dataset
    with open('insecta-ant-trophallaxis-colony2.edges', 'r') as f_in, open('insecta-ant-trophallaxis-colony2.edges_without_timestamp.txt', 'w') as f_out:
        for line in f_in:
            parole = line.split()
            parole.pop()
            parole.pop()
            riga_modificata = ' '.join(parole) + '\n'
            f_out.write(riga_modificata)

    #load graph
    g = nx.read_adjlist('insecta-ant-trophallaxis-colony2.edges_without_timestamp.txt')
    #nodes
    V = set(g.nodes())
    print("Nodes: ")
    print(V)
    #neighbors
    N = {v: set(g.neighbors(v)) for v in g.nodes}
    print("Neighbors: ")
    print(N)

    k = int(sys.argv[3])
    print("Costs: ")
    if(sys.argv[2]=="1"):
        c = set_random_costs(V,1,20)
        print(c)
    elif(sys.argv[2]=="2"):
        c = set_degree_costs(N,V)
        print(c)
    elif(sys.argv[2]=="3"):
        c = set_inverse_degree_costs(N,V)
        print(c)

    print("seed set:")
    if sys.argv[1] == "1":
        print(cost_seeds_greedy(g, k, c))
    elif sys.argv[1] == "2":
        print(wtss(g,c,k))
    elif sys.argv[1] == "3":
        print(costMajorityCascadeProblem(g,c,k))