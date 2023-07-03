#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 21:04:21 2023

@author: gonzalo
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Parámetros óptimos obtenidos

d = 0.1807374751457474
mmax = 0.20548586838031846
nmax = 0.6526810854084177
KGm = 0.07260300735821919
KOm = 0.1790816660873027
KGn = 0.0006424876011861735
KOn = 0.007982766975082496
Gin = 8.247066445285308
YGC = 0.6846031769375902
YGD = 0.14251062658004346
YOC = 0.13009208450224555
YOD = 0.8129092388703709
k = 1.4155688331196261
Osat = 7.008163310784721
a = 0.04259659799686465

def m(G, O):
    return mmax * (G / (G + KGm)) * (O / (O + KOm))

def n(G, O):
    return nmax * (G / (G + KGn)) * (O / (O + KOn))

def ode_model(X, t):
    C, D, G, O = X

    dC = n(G, O) * C * D - d * C
    dD = m(G, O) * D - a * C * D - d * D
    dG = (Gin - G) * d - (m(G, O) / YGD) * D - (n(G, O) / YGC) * C
    dO = (Osat - O) * k - (m(G, O) / YOD) * D - (n(G, O) / YOC) * C

    return [dC, dD, dG, dO]

# Condiciones iniciales
IC = [1, 1, 1, 1]

# Tiempo de integración
t = np.linspace(0, 1000, 1000)

# Resolver el sistema de ecuaciones diferenciales
sol = odeint(ode_model, IC, t)

# Extraer las soluciones de las variables
C = sol[:, 0]
D = sol[:, 1]
G = sol[:, 2]
O = sol[:, 3]

# Graficar las soluciones
plt.plot(t, C, label='C')
#plt.plot(t, D, label='D')
#plt.plot(t, G, label='G')
plt.plot(t, O, label='O')
plt.xlabel('Tiempo')
plt.ylabel('Concentración')
plt.title('Soluciones para O y C con parámetros depurados')
plt.xlim(0, 400)
plt.legend()
plt.grid(True)
plt.show()
