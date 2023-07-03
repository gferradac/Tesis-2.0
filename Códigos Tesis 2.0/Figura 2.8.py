#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 20:09:47 2023

@author: gonzalo
"""

import numpy as np
import matplotlib.pyplot as plt

# Definir las ecuaciones diferenciales del modelo mínimo de quimiostato
def dx_dt(X, S, d):
    mu = 0.5  # Tasa de crecimiento específico
    return (mu - d) * X

def ds_dt(X, S, d):
    mu = 0.5  # Tasa de crecimiento específico
    Sin = 1.0  # Concentración de sustrato en la entrada
    Y = 0.8    # Rendimiento de biomasa respecto al sustrato
    return d * (Sin - S) - (mu / Y) * X

# Definir el rango de valores para el parámetro de dilución (d)
d_values = np.linspace(0, 1, 100)

# Definir los valores iniciales de biomasa y sustrato
X0 = 1.0
S0 = 0.5

# Lista para almacenar los puntos de equilibrio
equilibrium_points = []

# Calcular los puntos de equilibrio para cada valor de dilución (d)
for d in d_values:
    # Resolver el sistema de ecuaciones diferenciales en el equilibrio
    equilibrium_X = X0
    equilibrium_S = ((1 / d) - 1) * (1 / X0)
    
    # Agregar el punto de equilibrio a la lista
    equilibrium_points.append((equilibrium_X, equilibrium_S))

# Convertir la lista de puntos de equilibrio en un arreglo de NumPy
equilibrium_points = np.array(equilibrium_points)

# Graficar el diagrama de bifurcación
plt.plot(d_values, equilibrium_points[:, 0], label='Biomasa (X)')
plt.plot(d_values, equilibrium_points[:, 1], label='Sustrato (S)')
plt.xlabel('Dilución (d)')
plt.ylabel('Concentración de equilibrio')
plt.title('Diagrama de bifurcación del modelo mínimo de quimiostato')
plt.legend()
plt.grid(True)
plt.show()

