#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 19:52:31 2023

@author: gonzalo
"""

import matplotlib.pyplot as plt
import numpy as np

# Parámetros del modelo
mu_values = np.linspace(0, 1, 100)  # Valores de la tasa de crecimiento microbiano

# Función que calcula la amplitud de las oscilaciones en función de la tasa de crecimiento microbiano
def calculate_amplitude(mu):
    # Cálculos del modelo
    # ...

    # Supongamos que la amplitud se calcula de la siguiente manera:
    amplitude = -4*(mu-0.5)**2 + 1

    return amplitude

# Calcular la amplitud de las oscilaciones para cada valor de la tasa de crecimiento microbiano
amplitudes = [calculate_amplitude(mu) for mu in mu_values]

# Graficar el diagrama de bifurcaciones
plt.plot(mu_values, amplitudes)
plt.xlabel('Tasa específica de crecimiento microbiano (mu)')
plt.ylabel('Amplitud de las oscilaciones')
plt.title('Diagrama de bifurcaciones')
plt.grid(True)
plt.show()
