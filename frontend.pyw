import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Importar la función modificada
from Diferencias_Finitas_1D_Matrix_Free import finite_difference

def plot_results():
    try:
        # Extraer parámetros numéricos
        x_start = float(entry_start.get())
        x_end = float(entry_end.get())
        paso = float(entry_paso.get())
        order = int(entry_order.get())
        func_str = entry_func.get()

        if paso <= 0 or x_end <= x_start or order < 1:
            raise ValueError("Los parámetros ingresados no tienen sentido físico o matemático.")

        # ----- INTERPRETACIÓN CON SYMPY -----
        x = sp.Symbol('x')
        # Parsear el string ingresado por el usuario a una expresión matemática
        expr = sp.sympify(func_str)
        
        # Calcular la derivada analítica exacta para comparar
        exact_deriv_expr = sp.diff(expr, x, order)
        
        # Convertir las expresiones de SymPy a funciones evaluables por NumPy
        u_func = sp.lambdify(x, expr, modules=['numpy'])
        u_prime_exact_func = sp.lambdify(x, exact_deriv_expr, modules=['numpy'])
        # ------------------------------------

        # Calcular la solución aproximada pasando la función vectorizada
        u_prime_aprox = finite_difference(x_start, x_end, paso, order, u_func)

        # Reconstruir la malla
        n_points = int(round((x_end - x_start) / paso)) + 1
        malla = np.linspace(x_start, x_end, n_points)
        
        # Evaluar la derivada exacta
        u_prime_exact = u_prime_exact_func(malla)
        
        # Manejo de casos donde la derivada exacta es una constante (lambdify devuelve un escalar)
        if isinstance(u_prime_exact, (int, float)):
            u_prime_exact = np.full_like(malla, u_prime_exact)

        # Graficar
        plt.figure(figsize=(10, 6))
        plt.plot(malla, u_prime_exact, label=f'Exacta (Orden {order})', color='black', linewidth=2)
        plt.plot(malla, u_prime_aprox, '--', label='Aproximación Matrix-Free', color='red', linewidth=2)
        
        plt.xlabel('x')
        plt.ylabel(f'Derivada de orden {order}')
        plt.title(f'Diferencias Finitas vs Solución Exacta: {func_str}')
        plt.grid(True, linestyle=":", alpha=0.7)
        plt.legend()
        plt.show()

    except sp.SympifyError:
        messagebox.showerror("Error de Sintaxis", "La función introducida no es una expresión matemática válida para SymPy.")
    except Exception as e:
        messagebox.showerror("Error de Ejecución", f"Fallo al procesar:\n{str(e)}")

# Configuración de la interfaz
root = tk.Tk()
root.title("Configuración - Diferencias Finitas")
root.resizable(False, False)

# Campos de entrada
tk.Label(root, text="Función u(x):").grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_func = tk.Entry(root, width=25)
entry_func.insert(0, "sin(x)") # Por defecto
entry_func.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Inicio del intervalo (x_start):").grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_start = tk.Entry(root, width=25)
entry_start.insert(0, "0.0")
entry_start.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Final del intervalo (x_end):").grid(row=2, column=0, padx=10, pady=10, sticky="e")
entry_end = tk.Entry(root, width=25)
entry_end.insert(0, "20.0")
entry_end.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Paso de la malla (h):").grid(row=3, column=0, padx=10, pady=10, sticky="e")
entry_paso = tk.Entry(root, width=25)
entry_paso.insert(0, "0.1")
entry_paso.grid(row=3, column=1, padx=10, pady=10)

tk.Label(root, text="Orden de la derivada (k):").grid(row=4, column=0, padx=10, pady=10, sticky="e")
entry_order = tk.Entry(root, width=25)
entry_order.insert(0, "1")
entry_order.grid(row=4, column=1, padx=10, pady=10)

# Botón
btn_plot = tk.Button(root, text="Calcular y Graficar", command=plot_results, width=20)
btn_plot.grid(row=5, column=0, columnspan=2, pady=20)

root.mainloop()