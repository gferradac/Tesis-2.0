#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 20:49:33 2023

@author: gonzalo
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Parámetros
mmax = 0.18
nmax = 0.65
KGm = 0.1
KOm = 0.1
KGn = 0.005
KOn = 0.005
Gin = 10
YGC = 0.7
YGD = 0.1
YOC = 0.1
YOD = 0.7
k = 1.2
Osat = 10
a=0.05

# Ecuaciones
def m(G,O):
    return mmax*(G/(G + KGm))*(O/(O + KOm))

def n(G,O):
    return nmax*(G/(G + KGn))*(O/(O + KOn))

def ode_model(X, t, d):
    C, D, G, O = X

    dC = n(G,O)*C*D-d*C
    dD = m(G,O)*D-a*C*D-d*D
    dG = (Gin-G)*d-(m(G,O)/YGD)*D -(n(G,O)/YGC)*C
    dO = (Osat-O)*k-(m(G,O)/YOD)*D -(n(G,O)/YOC)*C

    return [dC, dD, dG, dO]

# Condiciones iniciales
IC = [1, 1, 1, 1]

# Rango de valores del parámetro variable d
d_values = np.linspace(0.1, 0.4, 100)

# Listas para almacenar los valores de O y G en cada iteración
O_values = []
G_values = []

# Iteración sobre los valores de d
for d in d_values:
    # Solución del sistema de ecuaciones para un valor de d
    sol = odeint(ode_model, IC, np.linspace(0, 500, 10000), args=(d,))
    # Almacenamiento del valor final de O y G
    O_values.append(sol[-1, 3])
    G_values.append(sol[-1, 2])

# Gráfico del diagrama de bifurcación con ramas
plt.plot(d_values, O_values, '.', markersize=8)
plt.xlabel('Tasa de Dilución d')
plt.ylabel('Valor estable de O')
plt.title('Diagrama de bifurcación')
plt.ylim(0,11)
plt.xlim(0.1, 0.4)
plt.show()
