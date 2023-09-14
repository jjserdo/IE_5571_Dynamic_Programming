'''
Justine Serdoncillo
EE 5571 - Dynamic Programming
Lecture 3 
September 13, 2023
'''

import numpy as np
def epsilon_greedy(T,RewardVector,eps):
    k = len(RewardVector)
    r = 0
    avgReturn = np.zeros(T)
    q = np.zeros(k)
    rv = np.copy(RewardVector)
    n = np.zeros(k)

    for t in range(1,T):
        u = np.random.rand()
        if u < eps:
            a = np.random.randint(0,k)
        else:
            m = np.max(q)
            maxInd = np.where(Q==0)[0]
            if len(maxInd)>1:
                i = np.random.randint(0,len(maxInd))
                a = maxInd[i]
            else:
                a = maxInd[0]
        reward = np.random.randn()+rv[a]
        r += reward
        q[a] += 1/n[a] * (reward-q[a])


def run():
    pass

if __name__ == "__main__":
    run()