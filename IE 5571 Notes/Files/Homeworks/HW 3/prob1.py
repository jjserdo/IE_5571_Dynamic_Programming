# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 09:06:23 2023

@author: justi
"""

import numpy as np
import matplotlib.pyplot as plt
import random

# Value Iteration for the Gambler's problem

# %% Gambler function

class Gambler:
    def __init__(self, ph):
        self.ph = ph
        self.S = np.arange(1, 100)
        self.V = np.zeros(101)
        self.V[0] = 0
        self.V[100] = 1
        self.Vs = []
        self.pi = None
        self.sweep_count = None

    def valueIteration(self):
        self.sweep_count = 0
        while True:
            delta = 0
            for s in self.S:
                v = self.V[s]
                self.V[s] = np.max([self.V_eval(s, a) for a in self.A(s)])
                delta = np.maximum(delta, abs(v - self.V[s]))
            if self.sweep_count < 3:
                self.Vs.append(self.V.copy())
            self.sweep_count += 1
            if delta < 1E-10:
                break
        print('Sweeps needed:', self.sweep_count)
        self.Vs.append(self.V.copy())
        self.pi = [self.A(s)[np.argmax([self.V_eval(s, a) for a in self.A(s)])] for s in self.S]
        plt.figure()
        plt.plot(self.Vs[0])
        plt.plot(self.Vs[1])
        plt.plot(self.Vs[2])
        plt.plot(self.Vs[3])
        plt.figure()
        plt.step(self.S, self.pi)

    def A(self, s):
        return np.arange(1, np.minimum(s, 100 - s) + 1)

    def V_eval(self, s, a):
        return 1 * self.V[s + a] * self.ph + 1 * self.V[s - a] * (1 - self.ph)

Orig = Gambler(0.4)
Orig.valueIteration()

Low = Gambler(0.25)
Low.valueIteration()

High = Gambler(0.55)
High.valueIteration()
        
    
        

