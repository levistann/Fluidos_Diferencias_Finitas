import numpy as np
import matplotlib.pyplot as plt

#definiendo variables

#funtos de inicio y final
x_start = 0.0
x_final = 20
n_points = 50 #numero de puntos a aproximar


#condiciones de frontera
a = np.cos(x_start)
b = np.cos(x_final)

step = (x_final - x_start)/(n_points - 1)    #paso
x = np.linspace(x_start, x_final, n_points)     #dominio de nuestra funcion
def u(x):       #definimos la funcion de la cual aproximaremos du/dx
    return np.sin(x)

U = u(x)    #evaluamos nuestra funcion sobre el dominio


#Operador hacia atras
#matriz de coeficientes
D_left = np.diag(np.ones(n_points)/step) + np.diag(-np.ones(n_points - 1)/step, k = -1)
#ajustamos la matriz para las condiciones iniciales
D_left[0, :] = 0
D_left[-1, :] = 0
#calculamos la derivada aproximada e inyectamos las condiciones iniciales
u_prime_left = D_left @ U
u_prime_left[0] = a
u_prime_left[-1] = b



#Operador hacia adelante
#matriz de coeficientes
D_right = np.diag(np.ones(n_points - 1)/step, k = 1) + np.diag(-np.ones(n_points)/step)
#ajustamos la matriz para las condiciones iniciales
D_right[0, :] = 0
D_right[-1, :] = 0
#calculamos la derivada aproximada e inyectamos las condiciones iniciales
u_prime_right = D_right @ U
u_prime_right[0] = a
u_prime_right[-1] = b



#Operador central
#matriz de coeficientes
D_0 = np.diag(np.ones(n_points - 1)/(2*step), k = 1) + np.diag(-np.ones(n_points - 1)/(2*step), k = -1)
#ajustamos la matriz para las condiciones iniciales
D_0[0, :] = 0
D_0[-1, :] = 0
#calculamos la derivada aproximada e inyectamos las condiciones iniciales
u_prime_central = D_0 @ U
u_prime_central[0] = a
u_prime_central[-1] = b




#solucion analitica
u_exact = np.cos(x)

fig1, (ax1, ax2) = plt.subplots(1, 2, figsize = (14, 5))
ax1.plot(x, u_exact, 'k-', label = 'Solucion Analitica')
ax1.plot(x, u_prime_left, 'bo-', label = r'Solucion aproximada por  $D_{-u(x)}$')
ax1.set_xlabel('valor de x')
ax1.set_ylabel('valor de la funcion')
ax1.set_title(r"Comparacion solucion analitica vs aproximada de:   $\frac{dsin(x)}{dx}$  con  $D_{-u(x)}$")
ax1.legend()
ax1.grid(True)

ax2.plot(x, u_exact, 'k-', label = 'Solucion Analitica')
ax2.plot(x, u_prime_right, 'bo-', label = r'Solucion aproximada por  $D_{+u(x)}$')
ax2.set_xlabel('valor de x')
#ax2.ylabel('valor de la funcion')
ax2.set_title(r"Comparacion solucion analitica vs aproximada de:   $\frac{dsin(x)}{dx}$  con  $D_{+u(x)}$")
ax2.legend()
ax2.grid(True)
plt.tight_layout()

fig2, ax3 = plt.subplots(figsize = (8, 5))
ax3.plot(x, u_exact, 'k-', label = 'Solucion Analitica')
ax3.plot(x, u_prime_central, 'bo-', label = r'Solucion aproximada por  $D_{0u(x)}$')
ax3.set_xlabel('valor de x')
ax3.set_ylabel('valor de la funcion')
ax3.set_title(r"Comparacion solucion analitica vs aproximada de:   $\frac{dsin(x)}{dx}$  con  $D_{0u(x)}$")
ax3.legend()
ax3.grid(True)
plt.show()