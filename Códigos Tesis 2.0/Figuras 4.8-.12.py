#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 20:56:55 2023

@author: gonzalo
"""


'''Simulación del modelo con odeint'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import integrate
import ipywidgets as ipw
#Parámetros

d = 0.1     # /h
mmax= 0.18 # /h
nmax= 0.65
KGm = 0.1
KOm = 0.1
KGn= 0.005
KOn= 0.005
Gin = 10  #g/L
YGC = 0.7
YGD = 0.1
YOC = 0.1
YOD = 0.7
k = 1.2
Osat = 10   #mg/L
a=0.05


D0=1
C0=1
G0=1
O0=1

def ode_model(X, t, d, mmax, nmax, KGm, KOm, KGn, KOn, Gin, YGC, YGD, YOC, YOD, k, Osat, a):
    
    C, D, G, O = X
  
    dC = nmax*(G/(G + KGn))*(O/(O + KOn))*C*D-d*C
    dD = mmax*(G/(G + KGm))*(O/(O + KOm))*D-a*C*D-d*D
    dG = (Gin-G)*d-(mmax*(G/(G + KGm))*(O/(O + KOm))/YGD)*D -(nmax*(G/(G + KGn))*(O/(O + KOn))/YGC)*C
    dO = (Osat-O)*k-(mmax*(G/(G + KGm))*(O/(O + KOm))/YOD)*D -(nmax*(G/(G + KGn))*(O/(O + KOn))/YOC)*C
    
    return np.array([dC,dD,dG,dO])
    
Nt = 1000
tmax = 1000
t = np.linspace(0,tmax, Nt)
X0 = [C0, D0, G0, O0]
res = integrate.odeint(ode_model, X0, t, args = (d, mmax, nmax, KGm, KOm, KGn, KOn, Gin, YGC, YGD, YOC, YOD, k, Osat, a))
C, D, G, O = res.T

#(2, 1000)

plt.figure()
plt.grid()
plt.title("Oscilaciones biomasa y oxígeno disuelto")
plt.plot(t, C, 'r', label = "Compromiso")
plt.plot(t, D, 'b', label = 'Desarrollo')
plt.plot(t, O, 'g', label= 'Oxígeno disuelto')
plt.xlabel('Tiempo, [Minutos]')
plt.ylabel('Concentración [g/L]')
plt.legend()

plt.show()


'''Variación de la tasa de transferencia a'''

import random
import matplotlib.cm as cm


aes = np.arange(0.04, 0.07, 0.01)

nums=np.random.random((10,len(aes)))
colors = cm.rainbow(np.linspace(0, 1, nums.shape[0]))  # generate the colors for each data set

fig, ax = plt.subplots(2,1)

for a, i in zip(aes, range(len(aes))):
    res = integrate.odeint(ode_model, X0, t, args = (d, mmax, nmax, KGm, KOm, KGn, KOn, Gin, YGC, YGD, YOC, YOD, k, Osat, a))
    ax[0].plot(t, res[:,0], color = colors[i],  linestyle = '-', label = r"$ a = $" + "{0:.2f}".format(a))
    ax[1].plot(t, res[:,1], color = colors[i], linestyle = '-', label = r"$ a = $" + "{0:.2f}".format(a))
    ax[0].legend()
    ax[1].legend()

ax[0].grid()
ax[1].grid()
ax[0].set_xlabel('Tiempo t, [minutos]')
ax[0].set_ylabel('Compromiso, [g/L]')
ax[1].set_xlabel('Tiempo t, [minutos]')
ax[1].set_ylabel('Desarrollo, [g/L]');



aes = np.arange(0.04, 0.07, 0.01)

nums=np.random.random((10,len(aes)))
colors = cm.rainbow(np.linspace(0, 1, nums.shape[0]))  # generate the colors for each data set

fig, ax = plt.subplots(2,1)

for a, i in zip(aes, range(len(aes))):
    res = integrate.odeint(ode_model, X0, t, args = (d, mmax, nmax, KGm, KOm, KGn, KOn, Gin, YGC, YGD, YOC, YOD, k, Osat, a))
    ax[0].plot(t, res[:,2], color = colors[i],  linestyle = '-', label = r"$ a = $" + "{0:.2f}".format(a))
    ax[1].plot(t, res[:,3], color = colors[i], linestyle = '-', label = r"$ a = $" + "{0:.2f}".format(a))
    ax[0].legend()
    ax[1].legend()

ax[0].grid()
ax[1].grid()
ax[0].set_xlabel('Tiempo t, [minutos]')
ax[0].set_ylabel('Glucosa, [g/L]')
ax[1].set_xlabel('Tiempo t, [minutos]')
ax[1].set_ylabel('Oxígeno disuelto, [mg/L] ');



''' VARIACIÓN DE LA TASA DE DILUCIÓN d'''

import random
import matplotlib.cm as cm


des = np.arange(0.1, 0.14, 0.01)

nums=np.random.random((10,len(des)))
colors = cm.rainbow(np.linspace(0, 1, nums.shape[0]))  # generate the colors for each data set

fig, ax = plt.subplots(2,1)

for d, i in zip(des, range(len(aes))):
    res = integrate.odeint(ode_model, X0, t, args = (d, mmax, nmax, KGm, KOm, KGn, KOn, Gin, YGC, YGD, YOC, YOD, k, Osat, a))
    ax[0].plot(t, res[:,0], color = colors[i],  linestyle = '-', label = r"$ d = $" + "{0:.2f}".format(d))
    ax[1].plot(t, res[:,1], color = colors[i], linestyle = '-', label = r"$ d = $" + "{0:.2f}".format(d))
    ax[0].legend()
    ax[1].legend()

#ax[0].grid()
#ax[1].grid()
ax[0].set_xlabel('Tiempo t, [minutos]')
ax[0].set_ylabel('Compromiso, [g/L] ')
ax[1].set_xlabel('Tiempo t, [minutos]')
ax[1].set_ylabel('Desarrollo, [g/L]');



des = np.arange(0.14, 0.17, 0.01)

nums=np.random.random((10,len(des)))
colors = cm.rainbow(np.linspace(0, 1, nums.shape[0]))  # generate the colors for each data set

fig, ax = plt.subplots(2,1)

for d, i in zip(des, range(len(des))):
    res = integrate.odeint(ode_model, X0, t, args = (d, mmax, nmax, KGm, KOm, KGn, KOn, Gin, YGC, YGD, YOC, YOD, k, Osat, a))
    ax[0].plot(t, res[:,2], color = colors[i],  linestyle = '-', label = r"$ d = $" + "{0:.2f}".format(d))
    ax[1].plot(t, res[:,3], color = colors[i], linestyle = '-', label = r"$ d = $" + "{0:.2f}".format(d))
    ax[0].legend()
    ax[1].legend()

#ax[0].grid()
#ax[1].grid()
ax[0].set_xlabel('Tiempo t, [minutos]')
ax[0].set_ylabel('Glucosa, [g/L]')
ax[1].set_xlabel('Tiempo t, [minutos]')
ax[1].set_ylabel('Oxígeno disuelto, [mg/L]');




''' Oxígeno disuelto en función de la tasa de dilución'''

des = np.arange(0.1, 0.25, 0.1)

nums=np.random.random((10,len(des)))
colors = cm.rainbow(np.linspace(0, 1, nums.shape[0]))  # generate the colors for each data set

plt.figure()

for d, i in zip(des, range(len(des))):
    res = integrate.odeint(ode_model, X0, t, args = (d, mmax, nmax, KGm, KOm, KGn, KOn, Gin, YGC, YGD, YOC, YOD, k, Osat, a))
    plt.plot(t, res[:,3], color = colors[i],  linestyle = '-', label = r"$ d = $" + "{0:.2f}".format(d))
    plt.ylim(5,8)
    plt.xlim(200, 250)
    plt.legend()
   
plt.title("dO2 en función de d")
plt.xlabel('Time t, [Minutos]')
plt.ylabel('Concentración, [g/L]');
   

plt.plot(t, O)
plt.plot(t, C)
plt.ylim(0,10)
plt.xlim(200, 270)








