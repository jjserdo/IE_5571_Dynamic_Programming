'''
Justine Serdoncillo
IE 5571 - Dynamic Programming
HW 1 Exercise 2.5
September 25, 2023
'''

"""
Design and conduct an experiment to demonstrate the
diculties that sample-average methods have for nonstationary problems. Use a modified
version of the 10-armed testbed in which all the q ⇤ ( a ) start out equal and then take
independent random walks (say by adding a normally distributed increment with mean 0
and standard deviation 0.01 to all the q ⇤ ( a ) on each step). Prepare plots like Figure 2.2
for an action-value method using sample averages, incrementally computed, and another
action-value method using a constant step-size parameter, ↵ = 0 . 1. Use " = 0 . 1 and
longer runs, say of 10,000 steps. 
"""

import numpy as np
import matplotlib.pyplot as plt
import random

def RandomWalk(x):
    dim=np.size(x)
    walk_set=[-1,1,0]
    for i in range(dim):
        x[i]=x[i]+np.random.choice(walk_set)
    return x
def eps_greedy(x, ep, k):
    r = random.uniform(0,1)
    i = np.argmax(x) 
    column_indexes = list(range(0,k))
    
    if r <= eps:
        column_indexes.remove(i)
        i = random.choice(column_indexes) 
        return i
    else:
        return i    
def exercise25(eps, maxIte, t, k, a):
    rows, cols = t, k
    q = np.array( [([0]*k) for i in range(rows)] ) 
    constQ = np.array( [([0]*cols) for i in range(rows)] )
    variabQ = np.array( [([0]*cols) for i in range(rows)] )
    constN = np.array( [([0]*cols) for i in range(rows)] )
    variabN = np.array( [([0]*cols) for i in range(rows)] )
    constR = np.zeros(maxIte)
    variabR = np.zeros(maxIte)
    
    for i in range(maxIte):
        
        for j in range(t):
            task_q = q[j, :]
            task_q = RandomWalk(task_q)
            q[j,:] = task_q
            
            task_constQ = constQ[j,:]
            task_constN = constN[j,:]
            
            action_index_c = eps_greedy(task_constQ, eps, k)
            
            reward_const = q[j,action_index_c]
            
            constR[i] = constR[i] + reward_const
            
            task_constQ[action_index_c] = task_constQ[action_index_c] + a*(reward_const-task_constQ[action_index_c])
            constQ[j,:] = task_constQ
            
            task_constN[action_index_c] = task_constN[action_index_c] + 1
            constN[j:] = task_constN

            task_variabQ = variabQ[j,:]
            task_variabN = variabN[j,:]
            
            action_index_v = eps_greedy(task_variabQ, eps, k)
            
            reward_variab = q[j,action_index_v]
            
            variabR[i] = variabR[i] + reward_variab
            
            task_variabN[action_index_v] = task_variabN[action_index_v] + 1
            variabN[j,:] = task_variabN

            if i == 0:
                beta = 1
            else:
                beta = (1/task_variabN[action_index_v])
            
            task_variabQ[action_index_v] = task_variabQ[action_index_v] +\
                                           beta*(reward_variab-task_variabQ[action_index_v])
            variabQ[j,:] = task_variabQ
        
        constR[i] = constR[i] / t
        variabR [i] = variabR[i] / t
        
      
    # calculate and plot
    R_c_step = np.copy(constR) 
    R_v_step = np.copy(variabR)
    
    fig, ax =  plt.subplots(figsize=(10,5))
    ax.set_xlabel('steps')
    ax.set_ylabel('average reward')
    ax.plot(R_c_step, 'r', label='constant stepsize')
    ax.plot(R_v_step, 'g', label='varying stepsize')
    ax.legend(loc='upper left') 
    
if __name__ == "__main__" :
    eps=0.1 
    maxIte=10000 
    t=500 
    k=10 
    a=0.1
    exercise25(eps, maxIte, t, k, a)