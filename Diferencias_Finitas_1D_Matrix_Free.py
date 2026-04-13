import numpy as np
import matplotlib.pyplot as plt
from coefficients_kth_derivative import coefficients_kth_derivative as coeff


#definiendo variables

#parametros iniciales

x_start = 0.0
x_end = 20
paso = 0.1
order_derivative = 4
n_points = int(round((x_end - x_start)/paso)) + 1 #numero de puntos a aproximar
malla = np.linspace(x_start, x_end, n_points)     #dominio de nuestra funcion

#funcion que diferencias finitas

def finite_difference(x_start, x_end, paso, order_derivative, funcion):
    n_points = int(round((x_end - x_start)/paso)) + 1 #numero de puntos a aproximar
    malla = np.linspace(x_start, x_end, n_points)     #dominio de nuestra funcion
    U = funcion(malla)    #evaluamos nuestra funcion sobre el dominio

    stencil_size = order_derivative + 1

    if order_derivative % 2 != 0:
        stencil_size += 1

    boundary_margin = stencil_size // 2
    U_prime = np.zeros_like(U)

    intern_coefficients = coeff(order_derivative, malla[boundary_margin], malla)

    for i in range(stencil_size):
        start_slice = i
        end_slice = -stencil_size + 1 + i

        if end_slice == 0:
                end_slice = None
            
        U_prime[boundary_margin: -boundary_margin] += intern_coefficients[i] * U[start_slice:end_slice]

    for i in range(boundary_margin):
        start_coefficients = coeff(order_derivative, malla[i], malla)
        U_prime[i] = np.dot(start_coefficients, U[:stencil_size])

    for i in range(1, boundary_margin + 1):
        idx = n_points - i
        end_coefficients = coeff(order_derivative, malla[idx], malla)
        U_prime[idx] = np.dot(end_coefficients, U[-stencil_size:])
        
    return U_prime


'''
def funcion(malla):
    return malla**4

derivada_calculada = finite_difference(x_start, x_end, paso, order_derivative, funcion)

plt.plot(malla, derivada_calculada, label = "derivada aproximada")
plt.title("Derivada aproximada")
plt.xlabel("eje x")
plt.ylabel("eje y")
plt.legend()
plt.show()
'''
#solucion analitica
'''
pasos = [0.1, 0.05, 0.01, 0.001]
for i in range(len(pasos)):
    n_puntos = int(round((x_end - x_start)/pasos[i])) + 1
    grid = np.linspace(x_start, x_end, n_puntos)
    u_exact = -np.cos(grid)
    u_aproxx = finite_difference(x_start, x_end, pasos[i], order_derivative)
    error = u_aproxx - u_exact
    L_inf = np.max(np.abs(error))
    print(L_inf)
'''

'''
#Extraer el error
error = U_prime - u_exact
L_inf = np.max(np.abs(error))
L_sqrd = np.sqrt(paso*np.sum(error**2))

print(L_inf)
print(L_sqrd)
'''