# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 10:14:27 2023

@author: justi
"""

import numpy as np
import matplotlib.pyplot as plt
import random
import math

states = np.arange(0,4)
policy = np.array([0,0,0,1])
values = np.zeros(4, dtype=np.float16)
prob = np.array([[0, 7/8, 1/16, 1/16],
                 [0, 3/4, 1/8 , 1/8 ],
                 [0,   0, 1/2 , 1/2 ],
                 [0,   0,    0, 1   ]])
gamma = 0.95

rewards = np.array([[0, -1000, -3000,     0],
                    [0,     0, -2000, -6000]])

def possibleActions(state):
    if state == 2:
        actions = [0,1]
    elif state == 3:
        actions = [1]
    else:
        actions = [0]
    return actions

def sprimes(state, action):
    if state == 2 and action == 1:
        statePrimes = [1]
    elif state == 3 and action == 1:
        statePrimes = [0]
    else:
        statePrimes = [0,1,2,3]
        
    return statePrimes 
    
"""
def evalVal(state, action):
    value = 0
    r = rewards[action, state]
    for i in range(4):
        p = prob[state, i]
        value += p * (r + gamma * values[i])
        
    return value
"""

def evalVal(state, action):
    value = 0
    psa = sprimes(state, action)

    r = rewards[action, state]
    for sp in range(len(psa)):
        p = prob[state, psa[sp]]
        nv = values[psa[sp]]
        value +=  p *( r + gamma * nv )
    return value

theta = 1E-2
maxIte = 10000
ite = 0
print("Init Values")
print(values)
print("Init Policy")
print(policy)

def policyEvaluation():
    while True:
        print(values)
        delta = 0
        for s in range(len(states)):
            v = values[s]
            values[s] = evalVal(states[s], policy[s])
            delta = max(delta, abs(v - values[s]))
        if delta < theta:
            break
        
#policyEvaluation()

while True:
    print(f"ite: {ite}")
    print(f"policy: {policy}")
    ite += 1
    policyEvaluation()
    print(f"values: {values}")

    policy_stable = True    
    for s in range(len(states)):
        old = policy[s].copy()
        vvalues = {a: evalVal(s,a) for a in possibleActions(s)}
        bestActions = [a for a,value in vvalues.items() if value == np.max(list(vvalues.values()))]
        policy[s] = np.random.choice(bestActions)
        
        if old != policy[s]:
            policy_stable = False    
    if policy_stable:
        break
    
print("Final Values")
print(values)
print("Final Policy")
print(policy)

