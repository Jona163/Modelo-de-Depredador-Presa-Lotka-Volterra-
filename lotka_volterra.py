# Autor: Jonathan Hernández
# Fecha: 21 Septiembre 2024
# Descripción: Código para modelo de lotka.
# GitHub: https://github.com/Jona163

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Definición del sistema de ecuaciones diferenciales (modelo Lotka-Volterra)
def lotka_volterra(state, t, alpha, beta, delta, gamma):
    prey, predator = state
    dprey_dt = alpha * prey - beta * prey * predator
    dpredator_dt = delta * prey * predator - gamma * predator
    return [dprey_dt, dpredator_dt]


# Parámetros del modelo
alpha = 0.1  # Tasa de crecimiento de las presas
beta = 0.02  # Tasa de depredación
delta = 0.01  # Tasa de reproducción del depredador por depredación
gamma = 0.1   # Tasa de muerte de los depredadores

# Condiciones iniciales: [presas, depredadores]
initial_state = [40, 9]

# Espacio temporal
time = np.linspace(0, 200, 5000)


# Solución del sistema de ecuaciones diferenciales
solution = odeint(lotka_volterra, initial_state, time, args=(alpha, beta, delta, gamma))

# Graficar los resultados
prey, predator = solution.T

plt.figure(figsize=(10, 6))


# Graficar las presas y depredadores en función del tiempo
plt.plot(time, prey, label='Presas (Conejos)', color='blue')
plt.plot(time, predator, label='Depredadores (Lobos)', color='red')

