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
