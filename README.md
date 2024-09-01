# MajorityCascadeNetworks
### Esecuzione funzione di costo e algoritmo per selezionare un seed set
Per eseguire una funzione di costo e un algoritmo per la selezione del seed set: `python main.py <x> <y> <k>`. Il parametro `<x>` deve essere pari a `1` se si vuole eseguire `CostSeedsGreedy`, pari a `2` per `Weighted Target Set Selection` e pari a `3` per `CostMajorityCascadeProblem`. Il parametro `<y>` deve essere pari a `1` per selezionare la funzione dei costi `Random`, pari a 2 per la funzione `Degree` e pari a `3` per la `Inverse Degree`. Il parametro `<k>` indica il budget.

### Generazione costi e seed sets
Il file `generate_costs.py` permette la generazione e il salvataggio dei costi in file utilizzando le tre funzioni di costo. <br>
Il file `generate_seed_sets.py` permette l'esecuzione dei tre algoritmi per la generazione e il salvataggio in file dei seed set.

### Calcolo dell'influenza
Il file `influence_diffusion.py` contiene il codice necessario per il calcolo dell'influence diffusion, il file `start_influence_diffusion.py` permette la lettura di un file che contiene un seed set, l'esecuzione del'influence diffusion e il salvataggio in file dei risultati.

### Dataset
Il file `insecta-ant-trophallaxis-colony2.edges` è il dataset che rappresenta la rete sociale utilizzata, le prime due colonne rappresentano un arco, la terza il peso e la quarta il timestamp. <br>Il dataset è scaricabile al seguete link: [https://networkrepository.com/insecta-ant-trophallaxis-colony2.php](https://networkrepository.com/insecta-ant-trophallaxis-colony2.php).<br>
Il file `insecta-ant-trophallaxis-colony2.edges_without_timestamp.txt` è il dataset senza pesi e senza timestamp.

### Algoritmi, funzioni di costo, seed sets e risultati
In `algorithms` sono presenti gli algoritmi utilizzati per la selezione del seed set.<br> 
In `cost_functions` sono presenti le funzioni di costo. In `costi` sono presenti i costi utilizzati per gli esperimenti.<br>
In `influence_results` ci sono i risultati del processo di influence diffusion.<br>
In `seed_sets` ci sono i seed sets selezionati dagli algoritmi presenti in `algorithms`.

### Generazione grafici
Il file `plot_results` permette la creazione di grafici che rappresentano i numeri di nodi infettati.
