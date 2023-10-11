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
      
def exercise7(extraRules = False):
    def poisson(lam, n):
        return lam**n * math.exp(-lam) / math.factorial(n)
    def possibleActions(state):
        # Get the state of the cars
        firLoc = state[0]
        secLoc = state[1]
        #breakpoint()
        # list all possible & impossible actions
        allActions = [x for x in range(-maxMove, maxMove+1)]
        possibleActions = []
        
        for action in allActions:
            if firLoc + action > maxCar or firLoc + action < 0 or secLoc - action > maxCar or secLoc - action < 0:
                pass
            else:
                possibleActions.append(action)
        
        return possibleActions
    
    def evalVal(state, action):
        # Initialize
        value = 0
        sum_prob_i = 0
        
        # Get the state of the cars
        firLoc = state[0] + action
        breakpoint()
        secLoc = state[1] - action
        
        # Compute the cost
        cost = creditCar * abs(action) # Original Problem
        
        ps1req = 1
        ps2req = 1
        ps1ret = 1
        ps2ret = 1
        
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
                        
                        pTot = p1 * p2 * p3 * p4       
                        reward = r1 + r2 - cost + gamma*values[firLoc-reqs1+rets1, secLoc-reqs2+rets2]
                        value += pTot * reward
        
        #print(ps1req)
        #print(ps2req)
        #print(ps1ret)
        #print(ps2ret)

        return value


    def policyPrediction(theta, policy):
        values = np.zeros((maxCar+1, maxCar+1))
        while True:
            delta = 0 
            for s in states:
                v = values[s]
                values[s] = evalVal(s, policy[s])
                delta = np.max(delta, abs(v - values[s]))
            if delta < theta:
                break
        return values
    
    # Problem parameters
    maxCar = 20
    maxMove = 5  
    creditCar = 10 
    costCar = 2 
    
    # Learning Parameters
    gamma = 0.9
    theta = 1E-9
    maxIte = 1
    ite = 0
    stay = True
    
    # list comprehension for the states
    states = [(x,y) for x in range(maxCar+1) for y in range(maxCar+1)]
    policy = np.zeros((maxCar+1, maxCar+1), dtype=np.int8)
    
    # extra rules to make Jack's Car Rental harder
    if extraRules == True:
        limCar = 10
        overCost = 4
    else:
        # Iteration
        while ite < maxIte and stay == True:
            # Policy Evaluation
            values = policyPrediction(theta, policy)
            # Policy Improvement     
            stable = True
            for s in states:
                # copy policy to become old policy
                old_action = policy[s].copy()
                
                # create values dictionary based on chosen action
                vvalues = {a: evalVal(s,a) for a in possibleActions[s]}
                # random choose an action from the actions that map to the max values
                bestActions = [a for a,value in vvalues.items() if value == np.max(list(vvalues.values()))]
                policy[s] = np.random.choice(bestActions)
                
                # compare if old action is same as current action
                if np.array_equal(old_action, policy[s]):
                    policy_stable = False
        
            if policy_stable:
                stay = False
            else:
                ite += 1
                # Visualize current policy
                fig, ax = plt.subplots()
                ax.imshow(policy)
                ax.set_title(f"Jack's Problem Iteration: {ite}")
                fig.tight_layout()
                ax.set_xlabel("Cars at Location 1")
                ax.set_ylabel("Cars at Location 2")
        
if __name__ == "__main__" :
    exercise7()
    #exercise7(extraRules = True)
    
    
