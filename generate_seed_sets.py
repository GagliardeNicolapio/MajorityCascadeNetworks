import networkx as nx
import sys
from algorithms.WTSS import wtss
from algorithms.CostMajorityCascadeProblem import  costMajorityCascadeProblem
from algorithms.CostSeedsGreedy import cost_seeds_greedy
from cost_functions.set_degree_costs import set_degree_costs
from cost_functions.set_random_costs import set_random_costs
from cost_functions.set_inverse_degree_costs import set_inverse_degree_costs
import csv, json

def save_in_file(dizionario,nome_file):
    with open(nome_file, 'w') as file:
        for v in dizionario:
            file.write(v+" ")

def read_file(nome_file):
  dizionario = {}
  with open(nome_file, 'r') as file:
    reader = csv.reader(file, delimiter=' ')
    for riga in reader:
      chiave, valore = riga
      dizionario[chiave] = int(valore)
  return dizionario


if __name__ == '__main__':
    g = nx.read_adjlist('insecta-ant-trophallaxis-colony2.edges_without_timestamp.txt')
    V = set(g.nodes())
    N = {v: set(g.neighbors(v)) for v in g.nodes}
    k = 50
    c = read_file("costi/degree_costs.txt")
    print("costi: ")
    print(c)

    print("seed set costMajorityCascadeProblem")
    d = costMajorityCascadeProblem(g, c, k)
    print(d)
    save_in_file(d,"seed_sets/degree_costs/costMajCasProb_budget"+str(k)+"_seedset_degreecost.txt")

    g = nx.read_adjlist('insecta-ant-trophallaxis-colony2.edges_without_timestamp.txt')
    V = set(g.nodes())
    N = {v: set(g.neighbors(v)) for v in g.nodes}
    c = read_file("costi/degree_costs.txt")
    print("seed set costseedsgredy")
    d = cost_seeds_greedy(g, k, c)
    print(d)
    save_in_file(d,"seed_sets/degree_costs/costSeedsGreedy"+str(k)+"_seedset.txt")

    g = nx.read_adjlist('insecta-ant-trophallaxis-colony2.edges_without_timestamp.txt')
    V = set(g.nodes())
    N = {v: set(g.neighbors(v)) for v in g.nodes}
    c = read_file("costi/degree_costs.txt")
    print("seed set wtss")
    d = wtss(g,c,k)
    print(d)
    save_in_file(d, "seed_sets/degree_costs/wtss" + str(k) + "_seedset.txt")




