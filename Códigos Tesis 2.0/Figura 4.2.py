#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 20:27:05 2023

@author: gonzalo
"""


import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Definición de parámetros
d = 0.1     
mmax= 0.18 
nmax= 0.65
KGm = 0.1
KOm = 0.1
KGn= 0.005
KOn= 0.005
Gin = 10  
YGC = 0.7
YGD = 0.1
YOC = 0.1
YOD = 0.7
k = 1.2
Osat = 10 
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

# Definición de condiciones iniciales y tiempo de integración
X0 = [1, 1, 1, 1]
t = np.linspace(0, 1000, 10000)

# Resolución de las ecuaciones diferenciales
sol = odeint(ode_model, X0, t)

# Graficación de la solución numérica en el espacio de fases
fig, ax = plt.subplots(figsize=(8,8))
ax.plot(sol[:,0], sol[:,1])
ax.set_xlabel('Células Comprometidas, [g/L]')
ax.set_ylabel('Células en Desarrollo, [g/L]')
ax.set_title('Diagrama de Fase: Comprometidas vs En Desarrollo')
plt.xlim(0,2)
plt.ylim(0,0.5)
plt.show()