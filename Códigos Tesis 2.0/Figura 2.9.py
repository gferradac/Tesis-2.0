#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 20:10:48 2023

@author: gonzalo
"""
import numpy as np
import matplotlib.pyplot as plt

# Parámetros del modelo
mu = 0.3
d = 0.2
Sin = 1.0
Y = 0.5

# Paso de tiempo
dt = 0.1

# Valores iniciales
X0 = 1.0

# Número de iteraciones
num_iterations = 200

# Inicializar arreglos para almacenar los valores de X
X_current = np.zeros(num_iterations)
X_future = np.zeros(num_iterations)

# Calcular los valores de X en diferentes instantes de tiempo
X_current[0] = X0

for i in range(1, num_iterations):
    # Calcular X adelantado una unidad de tiempo
    X_future[i] = X_current[i-1] + dt * ((mu - d) * X_current[i-1])
    # Calcular el siguiente valor de X actual
    X_current[i] = X_future[i]

# Graficar el diagrama de retorno
plt.plot(X_current[:-1], X_future[:-1], 'p', markersize=2, label='Puntos de retorno')
plt.plot(X_current[:-1], X_current[1:], 'r--', label='Línea de identidad')

plt.xlabel('X(t)')
plt.ylabel('X(t+1)')
plt.ylim(1,7)
plt.title('Diagrama de Retorno de la Variable de Estado X')
plt.legend()
plt.grid(True)
plt.show()

