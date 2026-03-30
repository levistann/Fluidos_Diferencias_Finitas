import numpy as np
import math

def coefficients_kth_derivative(k, xbar, malla):
    '''
    k (int) = orden de la derivada la cual que queremos obtener sus coeficientes
    xbar (float) = punto donde queremos calcular la derivada
    malla (array) = malla de puntos donde queremos calcular la derivada
    '''

    malla = np.asarray(malla)
    indices = np.where(np.isclose(malla, xbar))[0]

    if len(indices) == 0:
        raise ValueError("El valor xbar no forma parte de ningun nodo de la mala")
    
    central_idx =  indices[0]
    start_idx = central_idx - k//2
    end_idx = central_idx + k//2 + 1

    stencil = malla[start_idx : end_idx]
    n = len(stencil)
    xrow = stencil - xbar

    coefficients_matrix = np.ones((n, n))
    for i in range(1, n):
        coefficients_matrix[i, :] = xrow**i/math.factorial(i)
    
    index_matrix = np.zeros(n)
    index_matrix[k] = 1.0

    c = np.linalg.solve(coefficients_matrix, index_matrix)

    return c

paso = 0.1
x_start = 1.0
x_end = 2.0
points = int(round((x_end - x_start)/paso)) + 1
malla = np.linspace(x_start, x_end, points)
orden_derivada = 4

c = coefficients_kth_derivative(orden_derivada, 1.5, malla)
print(c)

