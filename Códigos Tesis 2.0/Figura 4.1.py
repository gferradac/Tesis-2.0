#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 20:22:48 2023

@author: gonzalo
"""
import matplotlib.pyplot as plt
import numpy as np

d = 0.6   # /h
mmax = 0.18 # /h
nmax = 0.65
KGm = 0.1
KOm = 0.1
KGn = 0.005
KOn = 0.005
Gin = 10  # g/L
YGC = 0.7
YGR = 0.1
YOC = 0.1
YOR = 0.7
k = 1.2
Osat = 10   # mg/L
a=0.05

def m(G, O):
    return mmax*(G/(G + KGm))*(O/(O + KOm))

def n(G, O):
    return nmax*(G/(G + KGn))*(O/(O + KOn))

def ode_model(X, t):
    C, R, G, O = X
    dC = n(G, O)*C*R - d*C
    dR = m(G, O)*R - a*C*R - d*R
    dG = (Gin - G)*d - (m(G, O)/YGR)*R - (n(G, O)/YGC)*C
    dO = (Osat - O)*k - (m(G, O)/YOR)*R - (n(G, O)/YOC)*C
    return [dC, dR, dG, dO]

IC = [1, 1, 1, 1]

# Definir la malla de valores en el plano (C, O)
C = np.linspace(0, 4, 10)
O = np.linspace(0, 10, 10)
CC, OO = np.meshgrid(C, O)

# Evaluar las derivadas en cada punto de la malla
dC = n(Gin, OO)*CC*IC[1] - d*CC
dO = (Osat - OO)*k - (m(Gin, OO)/YOR)*IC[1] - (n(Gin, OO)/YOC)*CC

# Graficar las nullclinas
plt.plot(C, m(Gin, O)/n(Gin, O), 'b-', label='Nullclina de C')
plt.plot(n(Gin, O)/m(Gin, O), O, 'r-', label='Nullclina de O')

# Graficar el campo vectorial
mag = np.sqrt(dC**2 + dO**2)
plt.quiver(CC, OO, dC/mag, dO/mag, scale=30, width=0.005, alpha=0.8)

# Agregar un mapa de color para el campo vectorial
plt.quiverkey(plt.quiver(0, 0, 0.1, 0.1, scale=30, width=0.005, alpha=0.8), 0.9, 1.05, 
              0.1, '0.1 cm/s', labelpos='E', fontproperties={'size': 'large'})
plt.colorbar()


# Evaluar la magnitud del campo vectorial en cada punto de la malla
mag = np.sqrt(dC**2 + dO**2)

# Graficar el campo vectorial con mapa de color
plt.figure(figsize=(8, 8))
plt.streamplot(CC, OO, dC, dO, color=mag, cmap='plasma', linewidth=1, density=2)
plt.colorbar(label='Magnitud del vector')
plt.xlabel('Concentración de Células Comprometidas')
plt.ylabel('Concentración de Oxígeno Disuelto')

# Agregar una leyenda para el campo vectorial
plt.quiverkey(plt.quiver(0, 0, 0.1, 0.1, scale=30, width=0.005, alpha=0.8), 0.9, 1.05, 
              0.1, '0.1 cm/s', labelpos='E', fontproperties={'size': 'large'})

plt.show()
