# Autor: Jonathan Hernández
# Fecha: 21 Septiembre 2024
# Descripción: Código para modelo de lotka.
# GitHub: https://github.com/Jona163

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Estilo para las gráficas
plt.style.use('seaborn-darkgrid')

# 🎯 Función que define el sistema de ecuaciones diferenciales de Lotka-Volterra
def lotka_volterra(state, t, alpha, beta, delta, gamma):
    prey, predator = state
    # Ecuaciones diferenciales:
    # dprey_dt = α*presa - β*presa*depredador
    # dpredator_dt = δ*presa*depredador - γ*depredador
    dprey_dt = alpha * prey - beta * prey * predator
    dpredator_dt = delta * prey * predator - gamma * predator
    return [dprey_dt, dpredator_dt]

# ⚙️ Parámetros del modelo (puedes ajustarlos):
alpha = 0.1  # Tasa de crecimiento de presas (ej: conejos)
beta = 0.02  # Tasa de depredación (cómo los lobos cazan conejos)
delta = 0.01 # Tasa de reproducción de depredadores al cazar
gamma = 0.1  # Tasa de muerte de depredadores (ej: lobos)

# 🐰🐺 Condiciones iniciales [presas, depredadores]:
initial_state = [40, 9]

# 📅 Espacio temporal para la simulación (200 unidades de tiempo, 5000 puntos):
time = np.linspace(0, 200, 5000)

# 🚀 Resolviendo el sistema de ecuaciones diferenciales
solution = odeint(lotka_volterra, initial_state, time, args=(alpha, beta, delta, gamma))

# 🐇 Presas y 🐺 depredadores a lo largo del tiempo
prey, predator = solution.T

# 🎨 Visualización: Graficar la evolución temporal de las poblaciones
plt.figure(figsize=(10, 6))
plt.plot(time, prey, label='🐰 Presas (Conejos)', color='dodgerblue', lw=2)
plt.plot(time, predator, label='🐺 Depredadores (Lobos)', color='crimson', lw=2)

plt.title('Modelo Depredador-Presa (Lotka-Volterra)', fontsize=16)
plt.xlabel('Tiempo', fontsize=12)
plt.ylabel('Población', fontsize=12)
plt.legend(loc='best', fontsize=10)
plt.grid(True)
plt.tight_layout()
plt.show()

# 🔄 Visualización: Diagrama de fase (presa vs depredador)
plt.figure(figsize=(8, 6))
plt.plot(prey, predator, color='darkgreen', lw=2)
plt.title('Diagrama de Fase: Presas vs Depredadores', fontsize=16)
plt.xlabel('Población de Presas (Conejos)', fontsize=12)
plt.ylabel('Población de Depredadores (Lobos)', fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()

# 🎯 Manejo de excepciones para evitar errores inesperados
try:
    if __name__ == "__main__":
        # Ejecuta la simulación y muestra las gráficas
        print("Simulación completada exitosamente. ¡Mira las gráficas para ver el ciclo depredador-presa en acción!")
except Exception as e:
    print(f"⚠️ Ocurrió un error durante la ejecución: {e}")
