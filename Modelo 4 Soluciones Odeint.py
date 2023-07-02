#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 13:20:07 2023

@author: gonzalo
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

#Parámetros

d = 0.1     # /h
mmax= 0.18 # /h
nmax= 0.65
KGm = 0.1
KOm = 0.1
KGn= 0.005
KOn= 0.005
Gin = 10  #g/L
YGC = 0.7
YGD = 0.1
YOC = 0.1
YOD = 0.7
k = 1.2
Osat = 7.5   #mg/L
a=0.05


def m(G,O):
    return mmax*(G/(G + KGm))*(O/(O + KOm))

def n(G,O):
    return nmax*(G/(G + KGn))*(O/(O + KOn))



def ode_model(X, t):
    
    C, D, G, O = X

    dC = n(G,O)*C*D-d*C
    dD = m(G,O)*D-a*C*D-d*D
    dG = (Gin-G)*d-(m(G,O)/YGD)*D -(n(G,O)/YGC)*C
    dO = (Osat-O)*k-(m(G,O)/YOD)*D -(n(G,O)/YOC)*C
    
    return [dC, dD, dG, dO]


IC = [1, 1, 1, 1]

t = np.linspace(0, 1000, 1000)
sol = odeint(ode_model, IC, t)
C, D, G, O = sol.transpose()

plt.plot(t, C) 
plt.plot(t, D)
plt.plot(t, G)
plt.plot(t, O)

plt.ylim(0, 10)
plt.xlim(0, 1000)

plt.xlabel('Time [min]')
plt.ylabel('Concentration [g/liter]')
plt.legend(['C',
            'D', 'G', 'O'])