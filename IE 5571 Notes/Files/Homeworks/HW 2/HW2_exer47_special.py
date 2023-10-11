'''
Justine Serdoncillo
IE 5571 - Dynamic Programming
HW 2 Exercise 4.7
October 9, 2023
'''

"""
Write a program for policy iteration and re-solve Jack’s car
rental problem with the following changes. One of Jack’s employees at the first location
rides a bus home each night and lives near the second location. She is happy to shuttle
one car to the second location for free. Each additional car still costs $2, as do all cars
moved in the other direction. In addition, Jack has limited parking space at each location.
If more than 10 cars are kept overnight at a location (after any moving of cars), then an
additional cost of $4 must be incurred to use a second parking lot (independent of how
many cars are kept there). These sorts of nonlinearities and arbitrary dynamics often
occur in real problems and cannot easily be handled by optimization methods other than
dynamic programming. To check your program, first replicate the results given for the
original problem.
"""

import numpy as np
import matplotlib.pyplot as plt
import random
import math
   
# %% Use the Poisson Equation for the probability
def poisson(lam, n):
    return lam**n * math.exp(-lam) / math.factorial(n)

# Return a list of all possible actions
def possibleActions(state):
    # Get the state of the cars
    firLoc = state[0]
    secLoc = state[1]
    #breakpoint()
    # list all possible & impossible actions
    allActions = [x for x in range(-maxMove, maxMove+1)]
    possibleActions = []
    
    for action in allActions:
        newFir = firLoc - action
        newSec = secLoc + action
        if  newFir > maxCar or newFir < 0 or newSec > maxCar or newSec < 0:
            pass
        else:
            possibleActions.append(action)
    
    return possibleActions

# %% Evaluate a state and action based on a policy
def evalVal(state, action):
    # Initialize
    value = 0
    
    # Get the new state of the cars and compute the cost
    firLoc = state[0] - action
    secLoc = state[1] + action
    if action > 0:
        action -= 1
        cost = costCar * abs(action)
    else:
        if firLoc > limCar or secLoc > limCar:
            sad = 1
        else:
            sad = 0
        cost = costCar * abs(action) + overCost * sad 
   
    # Summation over all the possible new states
    ps1req, ps2req, ps1ret, ps2ret = 1, 1, 1, 1
    for reqs1 in range(firLoc+1): 
        p1 = poisson(3, reqs1) if reqs1 != firLoc else ps1req
        ps1req -= p1
        g = maxCar + reqs1 - firLoc
        r1 = creditCar * p1
        for reqs2 in range(secLoc+1):
            p2 = poisson(4, reqs2) if reqs2 != secLoc else ps2req
            ps2req -= p2
            h = maxCar + reqs2 - secLoc
            r2 = creditCar * p2
            for rets1 in range(g + 1):
                p3 = poisson(3, rets1) if rets1 != g else ps1ret
                ps1ret -= p3
                for rets2 in range(h + 1):
                    p4 = poisson(2, rets2) if rets2 != h else ps2ret
                    ps2ret -= p4
                    
                    # Sum all over the possible rewards
                    pTot = p1 * p2 * p3 * p4       
                    reward = r1 + r2 - cost + gamma*values[firLoc-reqs1+rets1, secLoc-reqs2+rets2]
                    value += pTot * reward
    return value

# %% Evaluate the Value of the policy
def policyEvaluation():
    print("Policy Evaluation")
    print("=================")
    ite = 0
    maxIte = 10
    while ite < maxIte:
        ite += 1
        delta = 0
        #breakpoint()
        for s in states:
            v = values[s]
            values[s] = evalVal(s, policy[s])
            #breakpoint()
            delta = max(delta, abs(v - values[s]))
        print(f"Current Delta at Iteration {ite}: {delta}")
        if delta < theta:
            break

# %% Actual Problem statement
# Problem parameters
maxCar = 20
maxMove = 5  
creditCar = 10 
costCar = 2 

# Extra Rules
limCar = 10
overCost = 4

# Learning Parameters
gamma = 0.9
theta = 1E-2
maxIte = 0
ite = 0
stay = True

# list comprehension for the states
states = [(x,y) for x in range(maxCar+1) for y in range(maxCar+1)]
policy = np.zeros((maxCar+1, maxCar+1), dtype=np.int8)
values = np.zeros((maxCar+1, maxCar+1))
#policy[10,0] = 5

fig, ax = plt.subplots(figsize=(8,6), dpi=150)
ax.imshow(policy, origin="lower", interpolation='none', vmin=-maxMove, vmax=maxMove)
ax.set_title(f"Jack's Problem Iteration: {ite}")
fig.tight_layout()
ax.set_xlabel("Cars at Location 2")
ax.set_ylabel("Cars at Location 1")
ax.set_xticks(np.arange(0, maxCar+1, 5))
ax.set_yticks(np.arange(0, maxCar+1, 5))
for yy in range(policy.shape[1]):
    for xx in range(policy.shape[0]):
        text = ax.text(xx, yy, policy[yy, xx], ha="center", va="center", color="w")

while ite < maxIte:
    ite += 1
    print(f"Iteration: {ite}")
    print( "~~~~~~~~~~~~~~~~")
    
    # Policy Evaluation
    print("Policy Evaluation")
    print("=================")
    ite = 0
    maxIte = 50
    while ite < maxIte:
        ite += 1
        delta = 0
        #breakpoint()
        for s in states:
            v = values[s]
            values[s] = evalVal(s, policy[s])
            #breakpoint()
            delta = max(delta, abs(v - values[s]))
        print(f"Current Delta at Iteration {ite}: {delta}")
        if delta < theta:
            break
    
    # Policy Improvement 
    policy_stable = True    
    for s in states:
        # copy policy to become old policy
        old = policy[s].copy()
        
        # create values dictionary based on chosen action
        vvalues = {a: evalVal(s,a) for a in possibleActions(s)}
        # random choose an action from the actions that map to the max values
        bestActions = [a for a,value in vvalues.items() if value == np.max(list(vvalues.values()))]
        policy[s] = np.random.choice(bestActions)
        
        # compare if old action is same as current action
        if old != policy[s]:
            policy_stable = False
    if policy_stable:
        break
    
    # Visualize current policy
    fig, ax = plt.subplots(figsize=(8,6), dpi=150)
    ax.imshow(policy, origin="lower", interpolation='none', vmin=-maxMove, vmax=maxMove)
    ax.set_title(f"Jack's Special Problem Iteration: {ite}")
    fig.tight_layout()
    ax.set_xlabel("Cars at Location 1")
    ax.set_ylabel("Cars at Location 2")
    ax.set_xticks(np.arange(0, maxCar+1, 5))
    ax.set_yticks(np.arange(0, maxCar+1, 5))
    for yy in range(policy.shape[1]):
        for xx in range(policy.shape[0]):
            text = ax.text(xx, yy, policy[yy, xx], ha="center", va="center", color="w")
        
    
# Print the optimal value function
fig = plt.figure(figsize=(8,6), dpi=150)
ax = plt.axes(projection='3d')
X, Y = np.meshgrid(range(maxCar+1), range(maxCar+1))
ax.plot_wireframe(X, Y, values, rstride=1, cstride=1)
ax.set_xlabel("Cars at Location 2")
ax.set_ylabel("Cars at Location 1")
ax.set_zlabel("V", rotation=0)
ax.set_title("Value Function for Jack's Original Problem")
ax.set_xticks(np.arange(0, maxCar+1, 5))
ax.set_yticks(np.arange(0, maxCar+1, 5))
fig.savefig("values.png")
