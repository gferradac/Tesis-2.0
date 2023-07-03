#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 20:08:09 2023

@author: gonzalo
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parámetros del sistema
mu = 0.1  # Tasa de crecimiento microbiano
d = 0.05  # Tasa de muerte microbiana
Sin = 2.0  # Concentración de sustrato de entrada
Y = 1  # Rendimiento de masa celular respecto al sustrato

# Definición del sistema de ecuaciones diferenciales
def quimiostato(y, t):
    X, S = y
    dXdt = (mu - d) * X
    dSdt = d * (Sin - S) - (mu / Y) * X
    return [dXdt, dSdt]

# Condiciones iniciales
X0 = 1.0  # Población inicial de microorganismos
S0 = 10  # Concentración inicial de sustrato
y0 = [X0, S0]

# Tiempo de integración
t = np.linspace(0, 25, 100)  # Intervalo de tiempo de 0 a 25 con 100 puntos

# Integración del sistema de ecuaciones diferenciales
sol = odeint(quimiostato, y0, t)

# Extraer las soluciones
X = sol[:, 0]
S = sol[:, 1]

# Restringir las soluciones a dominios positivos
X[X < 0] = 0
S[S < 0] = 0

# Graficar el diagrama de fase X-S
plt.plot(S, X)
plt.xlabel('Sustrato (S)')
plt.ylabel('Población (X)')
plt.title('Diagrama de fase del quimiostato')
plt.grid(True)
plt.show()
