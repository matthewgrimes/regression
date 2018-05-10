
# bayesian calculation of probability of a fair coin
from random import randrange

# number of possible values for P(H)
n = 10 
# possible values for P(H)=p_H
possible_ph = [i/n for i in range(0, n+1)]

# assume all are equally likely
ph_probability = {}
for p in possible_ph:
    ph_probability[p] = 1/n

# calculate prior P(H):
ph_prior = sum([p*ph_probability[p] for p in possible_ph])

experiments = []

def keywithmaxval(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

for j in [2, 5, 10, 100, 1000, 10000]:
    for i in range(0, j):
        # generate an experiment
        # 0=H 1=T
        experiment = randrange(0, 2)
        experiments.append(experiment)

        # update probabilities
        for p in possible_ph:
            ph_probability[p] = ph_probability[p] * \
                    ((1-experiment)*p + experiment*(1-p)) / ph_prior
        # recalculate ph_prior:
        ph_prior = sum([p*ph_probability[p] for p in possible_ph])
    #print("Estimate of P(H): "+str(ph_prior))
    #print("Observed P(H): "+str(1-sum(experiments)/len(experiments)))
    #for p in possible_ph:
    #    print(str(p)+": "+str(ph_probability[p]))
    print("Number of experiments: "+str(j))
    print("Estimate of P(H): "+str(ph_prior)+"  Predicted P(H): "+str(keywithmaxval(ph_probability)))
    print("")
