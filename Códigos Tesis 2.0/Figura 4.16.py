#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 21:17:47 2023

@author: gonzalo
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

# Datos experimentales

t_exp = np.array([240, 255, 270, 285, 300, 315, 330, 345, 360, 375, 390, 405, 420, 435, 450, 465, 480, 495, 510, 525, 540, 555, 570, 585, 600, 615, 630, 645, 660, 675])
C_exp = np.array([0.72, 0.648, 0.548, 0.484, 0.388, 0.316, 0.248, 0.172, 0.308, 0.572, 0.888, 0.832, 0.724, 0.68, 0.628, 0.656, 0.504, 0.452, 0.392, 0.324, 0.256, 0.192, 0.22, 0.212, 0.532, 0.752, 0.644, 0.508, 0.472, 0.408])
O_exp = np.array( [6.7905, 6.7703, 6.7501, 6.7602, 6.7602, 6.7891, 6.7804, 6.7508, 6.6042, 6.386, 6.6186, 6.8079, 6.8158, 6.8079, 6.779, 6.7652, 6.7587, 6.7385, 6.7226, 6.7385, 6.779, 6.779,  6.7587, 6.6656, 6.3022, 6.5146, 6.805, 6.8079, 6.7992, 6.7631 ])

def ode_model(t, X, d, mmax, nmax, KGm, KOm, KGn, KOn, YGC, YGD, YOC, YOD, Gin, k, Osat, a):
    
    C, D, G, O = X
    
    dC = nmax*(G/(G + KGn))*(O/(O + KOn))*C*D-d*C
    dD = mmax*(G/(G + KGm))*(O/(O + KOm))*D-a*C*D-d*D
    dG = (Gin-G)*d-(mmax*(G/(G + KGm))*(O/(O + KOm))/YGD)*D -(nmax*(G/(G + KGn))*(O/(O + KOn))/YGC)*C
    dO = (Osat-O)*k-(mmax*(G/(G + KGm))*(O/(O + KOm))/YOD)*D -(nmax*(G/(G + KGn))*(O/(O + KOn))/YOC)*C
   
    return [dC, dD, dG, dO]

# Parámetros

d = 0.1807374751457474
mmax = 0.20548586838031846
nmax = 0.6526810854084177
KGm = 0.07260300735821919
KOm = 0.1790816660873027
KGn = 0.0006424876011861735
KOn = 0.007982766975082496
Gin = 8.247066445285308
YGC = 0.6846031769375902
YGD = 0.14251062658004346
YOC = 0.13009208450224555
YOD = 0.8129092388703709
k = 1.4155688331196261
Osat = 7.008163310784721
a = 0.04259659799686465

# Condiciones iniciales arbitrarias
C0 = 1
D0 = 1
G0 = 1
O0 = 1

# Función para ajustar el modelo a los datos
def fit_model(params):
    d, mmax, nmax, KGm, KOm, KGn, KOn, YGC, YGD, YOC, YOD, Gin, k, Osat, a = params
    X0 = [C0, D0, G0, O0]
    sol = solve_ivp(lambda t, X: ode_model(t, X, d, mmax, nmax, KGm, KOm, KGn, KOn, YGC, YGD, YOC, YOD, Gin, k, Osat, a), [240, 675], X0, t_eval=t_exp)
    C, D, G, O = sol.y[0], sol.y[1], sol.y[2], sol.y[3]
    return C, O

# Función de error cuadrático medio
def mse(params):
    C, O = fit_model(params)
    mse_C = np.mean((C - C_exp)**2)
    mse_O = np.mean((O - O_exp)**2)
    return mse_C + mse_O

# Optimización de los parámetros
from scipy.optimize import minimize
params0 = [d, mmax, nmax, KGm, KOm, KGn, KOn, YGC, YGD, YOC, YOD, Gin, k, Osat, a]
res = minimize(mse, params0, method='Nelder-Mead')

# Parámetros optimizados

d_opt, mmax_opt, nmax_opt, KGm_opt, KOm_opt, KGn_opt, KOn_opt, YGC_opt, YGD_opt, YOC_opt, YOD_opt, Gin_opt, k_opt, Osat_opt, a_opt = res.x
print(f'Parámetros optimizados:\nd={d_opt}, mmax={mmax_opt}, nmax={nmax_opt}, KGm={KGm_opt}, KOm={KOm_opt}, KGn={KGn_opt}, KOn={KOn_opt}, YGC={YGC_opt}, YGD={YGD_opt}, YOC={YOC_opt}, YOD={YOD_opt}, Gin={Gin_opt}, k={k_opt}, Osat={Osat_opt}, a={a_opt}')

# Curva ajustada
t_fit = np.linspace(240, 675, 30)
C_fit, O_fit = fit_model(res.x)

# Gráfico
plt.plot(t_exp, C_exp, 'o', label='C experimental')
plt.plot(t_exp, O_exp, 'o', label='O experimental')
plt.plot(t_fit, C_fit, label='C ajustada')
plt.plot(t_fit, O_fit, label='O ajustada')
plt.xlabel('Tiempo')
plt.ylabel('Concentración')
plt.legend()
plt.show()
