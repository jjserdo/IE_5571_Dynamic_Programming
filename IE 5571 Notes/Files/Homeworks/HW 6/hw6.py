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
import matplotlib.pyplot as plt
import random
import math

# %%
wind = [0, 0, 0, 1, 1, 1, 2, 2, 1, 0]

class Grid:
    def __init__(self, w, h, wind):
        self.w = w
        self.h = h
        self.wind = wind
        self.actions = list(range(9))
        self.states = [tuple([i, j]) for j in range(self.h) for i in range(self.w)]
        self.starting_state = tuple([0, 3])
        self.terminal_states = [tuple([7, 3])]
    
    def take_action(self, state, action):
        #locations are x, y
        x = state[0]
        y = state[1]
        win_rand = random.random()
        if win_rand <= 1/3:
            y += wind[x]
        elif win_rand <= 2/3:
            y += wind[x] + 1
        else:
            y += wind[x] - 1
        if action == 0: # up
            x += 0
            y += 1
        if action == 1: # up, right
            x += 1
            y += 1
        if action == 2: # right
            x += 1
            y += 0
        if action == 3: # right, down
            x += 1
            y += -1
        if action == 4: # down
            x += 0
            y += -1
        if action == 5: # left, down
            x += -1
            y += -1
        if action == 6: # left
            x += -1
            y += 0
        if action == 7: # up, left
            x += -1
            y += 1
        if action == 8: # No move
            x += 0
            y += 0
        if x>= self.w:
            x = self.w - 1
        if y >= self.h:
            y = self.h - 1
        if y < 0:
            y = 0
        if x < 0:
            x = 0
        r = -1
        return tuple([x, y]), r
   
# %% SARSA
class TDAlg:
    def __init__(self, problem, qs=None, policy=None, eps=.05, gamma=1, alpha=1, max_time=None, special=False):
        self.problem = problem
        if qs is None:
            self.qs = {s: {a: 0 for a in problem.actions} for s in problem.states}
        else:
            self.qs = qs
        if policy is None:
            self.policy = {s: random.choice(problem.actions) for s in problem.states}
        else:
            self.policy = policy
        self.eps = eps
        self.gamma = gamma
        self.alpha = alpha
        self.max_time = max_time
        self.state = None
        self.ep = 1
        self.time = 0
        self.ep_log = []
        self.r_log = []
        self.special = special
    
    def get_action(self, state):
        if self.special is not False:
            self.eps = self.special/self.ep
        if random.random() < self.eps:
            choice = random.choice(self.problem.actions)
        else:
            choice = self.best_action(state)
        return choice
        
    def best_action(self, state):
        choices = [a for a in self.problem.actions if self.qs[state][a] == max(self.qs[state].values())]
        best_action = random.choice(choices)
        return best_action
    
    def run_episode(self):
        if (self.max_time is not None and self.time <= self.max_time) or self.max_time is None:
            old_count = self.time
            cum_reward = self.update()
            self.ep_log.extend([self.ep for _ in range(self.time - old_count)])
            self.ep += 1
            if len(self.r_log) > 0:
                self.r_log.append(self.r_log[-1] + cum_reward)
            else:
                self.r_log.append(cum_reward)
        else:
            pass
        
    def run(self, episodes):
        i = 0
        while i <= episodes:
            self.run_episode()
            i += 1
        
class Sarsa(TDAlg):
    def update(self):
        cum_reward = 0
        state = self.problem.starting_state
        action = self.get_action(state)
        while state not in self.problem.terminal_states:
            self.time += 1
            new_state, reward = self.problem.take_action(state, action)
            new_action = self.get_action(new_state)
            target = reward + self.gamma*self.qs[new_state][new_action] - self.qs[state][action]
            cum_reward += reward
            self.qs[state][action] += self.alpha*target
            action = new_action
            state = new_state        
        return cum_reward

# %% Q-Learning

class QLearn(TDAlg):
    def update(self):
        cum_reward = 0
        state = self.problem.starting_state
        while state not in self.problem.terminal_states:
            self.time += 1
            action = self.get_action(state)
            new_state, reward = self.problem.take_action(state, action)
            cum_reward += reward
            best = self.best_action(new_state)
            target = reward + self.gamma*self.qs[new_state][best] - self.qs[state][action]
            self.qs[state][action] += self.alpha*target
            state = new_state
        return cum_reward
    
    def update_from_model(self, s, a, s_, r):
        best = self.best_action(s_)
        target = r + self.gamma*self.qs[s_][best] - self.qs[s][a]
        self.qs[s][a] += self.alpha*target

# %% Ex-pected SARSA

class ESarsa(TDAlg):
    def update(self):
        cum_reward = 0
        state = self.problem.starting_state
        while state not in self.problem.terminal_states:
            self.time += 1
            action = self.get_action(state)
            new_state, reward = self.problem.take_action(state, action)
            val = reward - self.qs[state][action]
            best = self.best_action(new_state)
            for a in self.problem.actions:
                if a == best:
                    val += (1-self.eps)*self.gamma*self.qs[new_state][a]
                val += (self.eps/len(self.problem.actions))*self.gamma*self.qs[new_state][a]
            target = val
            cum_reward += reward
            self.qs[state][action] += self.alpha*target
            state = new_state        
        return cum_reward

# %% Fixed Epsilon
fig, ax = plt.subplots(figsize=(8,6), dpi=150)
ax.set_title("King's Problem fixed epsilon")
ax.set_xlabel("Time Steps")
ax.set_ylabel("Episodes")

grid = Grid(w=len(wind), h=7, wind=wind)
grid.actions = list(range(8))

sarsaFixed = Sarsa(grid, alpha=0.5, eps=.1)
sarsaFixed.run(10000)
ax.plot(sarsaFixed.ep_log, label='Sarsa')

QFixed = QLearn(grid, alpha=0.5, eps=.1)
QFixed.run(10000)
ax.plot(QFixed.ep_log, label='Qlearn')

EFixed = ESarsa(grid, alpha=0.5, eps=.1)
EFixed.run(10000)
ax.plot(EFixed.ep_log, label='Expected Sarsa')
ax.legend()

# %% Variable Epsilon
fig, ax = plt.subplots(figsize=(8,6), dpi=150)
ax.set_title("King's Problem variable epsilon")
ax.set_xlabel("Time Steps")
ax.set_ylabel("Episodes")

grid = Grid(w=len(wind), h=7, wind=wind)
grid.actions = list(range(8))

sarsaFixed = Sarsa(grid, alpha=0.5, eps=.3, special=.3)
sarsaFixed.run(10000)
ax.plot(sarsaFixed.ep_log, label='Sarsa')

QFixed = QLearn(grid, alpha=0.5, eps=.3, special=.3)
QFixed.run(10000)
ax.plot(QFixed.ep_log, label='Qlearn')

EFixed = ESarsa(grid, alpha=0.5, eps=.3, special=.3)
EFixed.run(10000)
ax.plot(EFixed.ep_log, label='Expected Sarsa')
ax.legend()

