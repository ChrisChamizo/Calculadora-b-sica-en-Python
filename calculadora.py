from tkinter import Tk, StringVar, W, E
from tkinter import ttk  # Para los widgets temáticos
import math  # Import para la raíz cuadrada

# Configuración de la ventana principal
root = Tk()
root.title("Calculadora")
root.geometry("400x400")  # Ajuste del tamaño de la ventana

# Crear el marco principal
mainframe = ttk.Frame(root, padding="10")
mainframe.grid(column=0, row=0, sticky=(W, E))

# Variable para manejar las entradas y operaciones
entrada = StringVar()
label_entrada = ttk.Entry(mainframe, textvariable=entrada, justify="right", font=("Arial", 16))
label_entrada.grid(column=0, row=0, columnspan=4, sticky=(W, E), padx=5, pady=5)

# Funciones de la calculadora
def insertar_caracter(caracter):
    entrada.set(entrada.get() + str(caracter))

def borrar_caracter():
    entrada.set(entrada.get()[:-1])

def borrar_todo():
    entrada.set("")

def calcular_resultado():
    try:
        resultado = eval(entrada.get().replace("√", "math.sqrt").replace("X", "*").replace("÷", "/"))
        entrada.set(str(resultado))
    except Exception:
        entrada.set("Error")

# Botones numéricos y operadores
botones = [
    ("(", 0, 1), (")", 1, 1), ("C", 2, 1), (chr(9003), 3, 1),
    ("7", 0, 2), ("8", 1, 2), ("9", 2, 2), (chr(247), 3, 2),
    ("4", 0, 3), ("5", 1, 3), ("6", 2, 3), ("X", 3, 3),
    ("1", 0, 4), ("2", 1, 4), ("3", 2, 4), ("+", 3, 4),
    ("0", 0, 5), (".", 1, 5), ("-", 2, 5), ("=", 3, 5),
    ("√", 3, 6)
]

for (texto, col, fila) in botones:
    if texto == "=":
        ttk.Button(mainframe, text=texto, command=calcular_resultado).grid(column=col, row=fila, columnspan=2, sticky=(W, E), padx=5, pady=5)
    elif texto == chr(9003):
        ttk.Button(mainframe, text=texto, command=borrar_caracter).grid(column=col, row=fila, sticky=(W, E), padx=5, pady=5)
    elif texto == "C":
        ttk.Button(mainframe, text=texto, command=borrar_todo).grid(column=col, row=fila, sticky=(W, E), padx=5, pady=5)
    else:
        ttk.Button(mainframe, text=texto, command=lambda t=texto: insertar_caracter(t)).grid(column=col, row=fila, sticky=(W, E), padx=5, pady=5)

# Ajuste del tamaño de las columnas
for i in range(4):
    mainframe.columnconfigure(i, weight=1)
for i in range(7):
    mainframe.rowconfigure(i, weight=1)

root.mainloop()
