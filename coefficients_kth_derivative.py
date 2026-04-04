import numpy as np
import math

def coefficients_kth_derivative(order_derivative, xbar, malla):
    '''
    k (int) = orden de la derivada la cual que queremos obtener sus coeficientes
    xbar (float) = punto donde queremos calcular la derivada
    malla (array) = malla de puntos donde queremos calcular la derivada
    '''
    coefficients_needed = order_derivative + 1

    #mantener un stencil impar para usar el operador central simetrico
    if order_derivative % 2 != 0:
        coefficients_needed += 1

    malla = np.asarray(malla)
    indices = np.where(np.isclose(malla, xbar))[0]

    if len(indices) == 0:
        raise ValueError("El valor xbar no forma parte de ningun nodo de la mala")
    
    central_idx = indices[0]

    #si es la frontera inicial:
    if central_idx - coefficients_needed//2 < 0:
        stencil = malla[:coefficients_needed]

    #si es la frontera final:
    elif central_idx + (coefficients_needed//2) >= len(malla):
        stencil = malla[-coefficients_needed:]
    
    #si estamos en el centro de la malla:
    else:
        start_idx = central_idx - (coefficients_needed//2)
        end_idx = central_idx + (coefficients_needed//2) + 1
        stencil = malla[start_idx : end_idx]
    

    xrow = stencil - xbar

    coefficients_matrix = np.ones((coefficients_needed, coefficients_needed))
    for i in range(1, coefficients_needed):
        coefficients_matrix[i, :] = xrow**i/math.factorial(i)
    
    index_matrix = np.zeros(coefficients_needed)
    index_matrix[order_derivative] = 1.0

    coefficients = np.linalg.solve(coefficients_matrix, index_matrix)

    return coefficients

'''
paso = 0.1
x_start = 1.0
x_end = 2.0
points = int(round((x_end - x_start)/paso)) + 1
malla = np.linspace(x_start, x_end, points)
orden_derivada = 4

c = coefficients_kth_derivative(orden_derivada, 1.5, malla)
print(c)
'''