import numpy as np
import matplotlib.pyplot as plt

# Parámetros del modelo de Monod
μmax = 1   # Tasa máxima de crecimiento microbiano
Ks = 0.1  # Constante de saturación

# Rango de concentración del sustrato
S = np.linspace(0, 1, 100)

# Cálculo de la tasa de crecimiento según el modelo de Monod
μ = μmax * (S / (Ks + S))

# Gráfico de la tasa de crecimiento en función de la concentración del sustrato
plt.plot(S, μ, label='μ = μmax * (S / (Ks + S))')
plt.xlabel('Concentración del sustrato (S)')
plt.ylabel('Tasa de crecimiento específica (μ)')
plt.title('Modelo de Monod')
plt.grid(True)

# Punto clave (Ks, mu_max/2)
plt.scatter(Ks, μmax/2, color='red', label='(Ks, μ(Ks)=μmax/2 )')
#plt.annotate(f'({Ks}, {μmax/2})', (Ks, μmax/2), textcoords="offset points", xytext=(-10, 10), ha='center')

# Línea de la asíntota
plt.axhline(y=1, color='green', linestyle='--', label='μ = μmax')

# Leyenda
plt.legend()

plt.show()


