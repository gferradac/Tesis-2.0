#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 20:51:36 2023

@author: gonzalo
"""

import numpy as np
import matplotlib.pyplot as plt

def poincare_map(data):
    return data[1:]

# Parámetros del sistema
d = 0.1
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
a = 0.05

# Funciones del sistema
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
    return np.array([dC, dD, dG, dO])

# Condiciones iniciales
IC = np.array([1, 1, 1, 1])

# Parámetros del diagrama de Poincaré
num_iterations = 1000
skip = 1  # Desfase de una unidad de tiempo

# Simulación del sistema
t = np.arange(num_iterations + 1)
sol = np.zeros((num_iterations + 1, 4))
sol[0] = IC
for i in range(num_iterations):
    sol[i + 1] = sol[i] + ode_model(sol[i], t[i])

# Construcción del diagrama de Poincaré
poincare_data = poincare_map(sol[::skip, 3])  # Seleccionar la variable de oxígeno disuelto
poincare_x = poincare_data[:-1]
poincare_y = poincare_data[1:]

# Graficar el diagrama de Poincaré
plt.scatter(poincare_x, poincare_y, s=5)
plt.xlabel('Oxígeno disuelto en tiempo t')
plt.ylabel('Oxígeno disuelto en tiempo t + 1')
plt.title('Diagrama de Poincaré: Oxígeno disuelto')
plt.xlim([0, 11])  # Ajustar el límite del eje x
plt.ylim([0, 11])  # Ajustar el límite del eje y
plt.show()
