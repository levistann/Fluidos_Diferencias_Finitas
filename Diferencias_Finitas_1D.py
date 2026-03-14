import numpy as np
import matplotlib.pyplot as plt

#definiendo variables
step = 0.1
n_points = 10
def u(x):
    y = x**2
    return y

#definiendo operadores
#operador sesgado hacia adelante

u_x_vector = np.zeros((1, n_points))  #generamos el vector de la funcion evaluada en el conjunto de puntos
print(u_x_vector)
coefficients_matrix = np.zeros((n_points, n_points))
print(coefficients_matrix)