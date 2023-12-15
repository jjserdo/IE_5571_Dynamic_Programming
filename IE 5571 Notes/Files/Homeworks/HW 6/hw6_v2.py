'''
Justine Serdoncillo
IE 5571 - Dynamic Programming
HW 4 Exercise 6.10
December 5, 2023
'''

"""
Consider the distance matrix provided in the file HW6Data. 
Your goal is to find a route of the Traveling Salesperson for this matrix assuming you start and finish your tour at node 1. 
In a tour you can only visit each city once, and the tour is complete once you have visited all cities. 
Your goal is to minimize your total distance traveled. 
You will use rollout with a base policy of nearest neighbor to find your route.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import math

# %% Inputs and Functions
filePath = 'HW6Data.csv'
    
def evalTravel(evalTravel):
    evalTravel.append(0)
    totDist = 0
    for i in range(21):
        totDist += dist_matrix[evalTravel[i], evalTravel[i+1]]
    return totDist

def nearNeigh(numNodes, posNodes, currNode, currList, totDist):
    
    for j in range(numNodes):
        currMin = 1E5 # current minimum
        currNodeMin = 0
        for i in posNodes:
            if dist_matrix[currNode, i] <= currMin:
                currMin = dist_matrix[currNode, i]
                currNodeMin = i
        currList.append(currNodeMin)
        totDist += currMin
        posNodes = np.setdiff1d(np.copy(posNodes),[currNodeMin])
        currNode = np.copy(currNodeMin)
    
    return totDist

def rollOut(numNodes, posNodes, currNode, currList, totDist):
    
    for j in range(numNodes):
        score = np.zeros(len(posNodes))
        num = 0
        for i in posNodes:
            posCopy = np.setdiff1d(np.copy(posNodes),[i])
            currCopy = currList + [i]
            totCopy = totDist + dist_matrix[currNode, i]
            score[num] = nearNeigh(numNodes-1, posCopy, i, currCopy, totCopy)
            num += 1
            
        currNodeMin = posNodes[np.argmin(score)]
        currList.append(currNodeMin)
        totDist += dist_matrix[currNode, currNodeMin]
        posNodes = np.setdiff1d(np.copy(posNodes),[currNodeMin])
        currNode = np.copy(currNodeMin)
        print(f"Current totDist = {totDist}")
        
    return totDist

# %% 
df = pd.read_csv(filePath)
dist_matrix = df.values
baseScores = np.zeros(20)
posNodes = np.arange(21) #list of possible nodes initially available
posNodes = np.setdiff1d(posNodes,[0]) #remove 0
currNode = 0 # updating node location
currList = [0] # updating list
totDist = 0 # total distance
base = 0

totDist += rollOut(20, posNodes, currNode, currList, totDist)

for i in range(21):
    currList[i] += 1

totDist += dist_matrix[currNode, 0]

print(f"This is the distance traveled: {totDist}")
print(f"This is the salesman path: {currList}")
    
