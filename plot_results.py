import matplotlib.pyplot as plt 
import numpy as np 
  
# create data 
costMajCas = [2,3,31,28,25,25,22,21] 
seedsGreedy = [1,0,0,2,0,23,22,22] 
wtss =[1,1,0,0,2,29,29,29] 
  
# plot lines 
plt.plot(costMajCas, label = "CostMajorityCascadeProblem", linestyle="-") 
plt.plot(seedsGreedy, label = "CostSeedsGreedy", linestyle="-") 
plt.plot(wtss, label = "WTSS", linestyle="-") 
plt.xlabel("Budget")
plt.ylabel("Numero di nodi influenzati")
x = np.array([0,1,2,3,4,5,6,7])
my_xticks = ['20', '30','40','50', '60', '70','80','90']
plt.xticks(x, my_xticks)
plt.grid(True)
plt.title("Random Costs")
plt.legend() 
plt.show()
