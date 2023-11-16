# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 10:14:27 2023

@author: justi
"""

import numpy as np
import matplotlib.pyplot as plt
import random
import math

states = [(x,y) for x in range(2) for y in range(5)]
policy = np.zeros((2,5), dtype=np.int8)
values = np.zeros((2,5), dtype=np.float16)
reward = np.array([500, 600, 700, 800, 1000])
prob = np.array([1/4, 1/4, 1/6, 1/6, 1/6])
gamma = 0.97

def sprimes(state, action):
    bought = state[0]
    price = state[1]
    
    if bought == 0:
        if action == 0:
            sprimes = [(0,y) for y in range(5)]
        elif action == 1:
            sprimes = [(1,y) for y in range(5)]
    elif bought == 1:
        sprimes = [(1,y) for y in range(5)]
    
    return sprimes
    
def probs(sprime, state, action):
    bought = state[0]
    price =  state[1]
    bought2 = sprime[0]
    
    if bought + action == bought2:
        probs = prob[price]
    else:
        probs = 0
        
    return probs

def rewards(state, action):
    bought = state[0]
    price = state[1]
    
    if bought == 0:
        if action == 0:
            rewards = -60
        elif action == 1:
            rewards = reward[price]
    elif bought == 1:
        rewards = 0
    
    return rewards

def possibleActions(state):
    bought = state[0]
    price = state[1]
    
    if bought == 0:
        actions = [0,1]
    else:
        actions = [0]
        
    return actions


def evalVal(state, action):
    value = 0
    psa = sprimes(state, action)

    r = rewards(state,action)
    for sp in range(len(psa)):
        p = probs(psa[sp], state, action)
        nv = values[psa[sp]]
        value +=  p *( r + gamma * nv )
    return value

theta = 1E-5
maxIte = 10000
ite = 0
print("Init Values")
print(values)
print("Init Policy")
print(policy)

def policyEvaluation():
    while True:
        delta = 0
        for s in range(len(states)):
            b, p = states[s]
            v = values[b,p]
            #breakpoint()
            values[b,p] = evalVal(states[s], policy[b,p])
            delta = max(delta, abs(v - values[b,p]))
        if delta < theta:
            break
        
def policyImprovement():
    vvalues = {a: evalVal(s,a) for a in possibleActions(s)}
    bestActions = [a for a,value in vvalues.items() if value == np.max(list(vvalues.values()))]
    #print(bestActions)
    policy[s] = np.random.choice(bestActions)

while True:
    print(f"ite: {ite}")
    print(f"policy: {policy[0]}")
    ite += 1
    policyEvaluation()
    print(f"values: {values[0]}")

    policy_stable = True    
    for s in range(len(states)):
        b, p = states[s]
        old = policy[b,p].copy()
        vvalues = {a: evalVal([b,p],a) for a in possibleActions([b,p])}
        bestActions = [a for a,value in vvalues.items() if value == np.max(list(vvalues.values()))]
        #print(bestActions)
        policy[b,p] = np.random.choice(bestActions)
        
        if old != policy[b,p]:
            policy_stable = False    
    if policy_stable:
        break
    
    
print("Final Values")
print(values)
print("Final Policy")
print(policy)
