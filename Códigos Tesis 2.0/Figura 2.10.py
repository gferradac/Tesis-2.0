#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 20:13:07 2023

@author: gonzalo
"""

import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
mu = 0.1  # Tasa de crecimiento microbiano
d = 0.05  # Tasa de muerte microbiana
Sin = 2.0  # Concentración de sustrato de entrada
Y = 1  # Rendimiento de masa celular respecto al sustrato

# Paso de tiempo
dt = 0.5

# Valores iniciales
X0 = 1.0
S0 = 10

# Número de iteraciones
num_iterations = 50

# Inicializar arreglos para almacenar los valores de X y S
X = np.zeros(num_iterations)
S = np.zeros(num_iterations)

# Asignar los valores iniciales
X[0] = X0
S[0] = S0

# Implementar el algoritmo de Adams-Bashforth-Moulton
for i in range(1, num_iterations):
    # Predictor (Adams-Bashforth)
    X_predictor = X[i-1] + dt * ((mu - d) * X[i-1])
    S_predictor = S[i-1] + dt * (d * (Sin - S[i-1]) - (mu / Y) * X[i-1])
    
    # Corrector (Adams-Moulton)
    X[i] = X[i-1] + dt/2 * (((mu - d) * X[i-1]) + ((mu - d) * X_predictor))
    S[i] = S[i-1] + dt/2 * ((d * (Sin - S[i-1]) - (mu / Y) * X[i-1]) + (d * (Sin - S_predictor) - (mu / Y) * X_predictor))

# Graficar las soluciones numéricas
t = np.linspace(0, num_iterations*dt, num_iterations)
plt.plot(t, X,'o', markersize=2, label='Población (X)')
plt.plot(t, S,'o', markersize=2, label='Sustrato (S)')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.title('Soluciones numéricas del sistema quimiostato (Adams-Bashforth-Moulton)')
plt.legend()
plt.grid(True)
plt.show()
