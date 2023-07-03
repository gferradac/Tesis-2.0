#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 20:02:45 2023

@author: gonzalo
"""

import numpy as np
import matplotlib.pyplot as plt

# Dimensiones del cultivo
rows = 100
cols = 100

# Inicialización del cultivo con estados aleatorios
cultivo = np.random.choice([0, 1], size=(rows, cols))

# Definición de los estados posibles
estados = {
    0: 'Ausencia de levadura',
    1: 'Presencia de levadura',
    2: 'Alto en nutrientes',
    3: 'Bajo en nutrientes'
}

# Función para actualizar el estado del cultivo en cada paso
def actualizar_cultivo(cultivo):
    nuevo_cultivo = np.zeros_like(cultivo)
    for i in range(rows):
        for j in range(cols):
            vecinos = obtener_vecinos(cultivo, i, j)
            estado_actual = cultivo[i, j]
            estado_vecinos = [cultivo[v[0], v[1]] for v in vecinos]
            nuevo_estado = regla_actualizacion(estado_actual, estado_vecinos)
            nuevo_cultivo[i, j] = nuevo_estado
    return nuevo_cultivo

# Función para obtener los vecinos de una celda
def obtener_vecinos(cultivo, i, j):
    vecinos = []
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if (x != i or y != j) and x >= 0 and x < rows and y >= 0 and y < cols:
                vecinos.append((x, y))
    return vecinos

# Función que define la regla de actualización
def regla_actualizacion(estado_actual, estado_vecinos):
    if estado_actual == 0:
        if 1 in estado_vecinos:
            return 1
        else:
            return 0
    elif estado_actual == 1:
        if 2 in estado_vecinos:
            return 2
        elif 3 in estado_vecinos:
            return 3
        else:
            return 1
    elif estado_actual == 2:
        if 3 in estado_vecinos:
            return 3
        else:
            return 2
    else:  # estado_actual == 3
        return 3

# Simulación temporal del consumo de oxígeno
steps = 100
cultivo_evolution = [cultivo]
for _ in range(steps):
    cultivo = actualizar_cultivo(cultivo)
    cultivo_evolution.append(cultivo)

# Creación de la animación
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xticks([])
ax.set_yticks([])

for i in range(len(cultivo_evolution)):
    ax.cla()
    ax.imshow(cultivo_evolution[i], cmap='viridis', vmin=0, vmax=3)
    ax.set_title(f'Paso {i}')
    plt.pause(0.1)

plt.show()
