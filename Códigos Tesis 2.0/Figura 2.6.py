#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 20:05:03 2023

@author: gonzalo
"""
import numpy as np
import matplotlib.pyplot as plt

# Definir las ecuaciones diferenciales del modelo mínimo de quimiostato
def dx_dt(X, S):
    mu = 0.5  # Tasa de crecimiento específico
    d = 0.2   # Tasa de dilución
    return (mu - d) * X

def ds_dt(X, S):
    mu = 0.5  # Tasa de crecimiento específico
    d = 0.2   # Tasa de dilución
    Sin = 1.0  # Concentración de sustrato en la entrada
    Y = 0.8    # Rendimiento de biomasa respecto al sustrato
    return d * (Sin - S) - (mu / Y) * X

# Definir el rango de valores para X y S
X = np.linspace(0, 5, 20)
S = np.linspace(0, 2, 20)

# Crear una malla de puntos para evaluar las derivadas en cada punto
X, S = np.meshgrid(X, S)

# Calcular las derivadas en cada punto de la malla
dX_dt = dx_dt(X, S)
dS_dt = ds_dt(X, S)

# Graficar el campo de vectores
plt.quiver(X, S, dX_dt, dS_dt)
plt.xlabel('Concentración de biomasa (X)')
plt.ylabel('Concentración de sustrato (S)')
plt.title('Campo de vectores del modelo mínimo de quimiostato')
plt.grid(True)
plt.show()