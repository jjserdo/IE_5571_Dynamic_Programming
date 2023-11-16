# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 23:12:10 2023

@author: justi
"""

import numpy as np
import matplotlib.pyplot as plt
import random
import math

states = np.arange(3)
policy = np.array([2,2,2])
values = np.zeros(3, dtype=np.float16)

gamma = 0.95

actions = np.array([0,1,2])
    
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
    sprime = state + action
    cost = action * 5 #+ 10*np.sign(action) 
    
    for i in range(3):
        nv = sprime-i
        
        if nv >= 0 and nv <= 2:
            r = -4 * nv 
            nvalue = values[nv]
        elif nv == -1:
            r = -8
            nvalue = 0
        elif nv == -2:
            r = -40
            nvalue = 0
        elif nv > 2:
            r = -8 
            nvalue = values[2]
    
        value +=  -cost + 1/3 *( r + gamma * nvalue )
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
        vvalues = {a: evalVal(s,a) for a in [0,1,2]}
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
