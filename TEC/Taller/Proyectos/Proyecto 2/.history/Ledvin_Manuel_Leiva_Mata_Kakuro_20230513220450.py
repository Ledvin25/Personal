# Proyecto 2: Kakuro
# Ledvin Manuel Leiva Mata
# 2023071280

# Importar librerias
import tkinter as tk

# Funciones para cada opción del menú
def funcion_abrir():
    print("Abrir archivo")

def funcion_guardar():
    print("Guardar archivo")

# Crear la ventana principal
root = tk.Tk()

# Crear el menú
menu = tk.Menu(root)

# Crear submenús
submenu1 = tk.Menu(menu)
submenu2 = tk.Menu(menu)

# Agregar opciones al menú y submenús
menu.add_cascade(label='Archivo', menu=submenu1)
submenu1.add_command(label='Abrir', command=funcion_abrir)
submenu1.add_command(label='Guardar', command=funcion_guardar)

menu.add_cascade(label='Edición', menu=submenu2)
submenu2.add_command(label='Cortar')
submenu2.add_command(label='Copiar')
submenu2.add_command(label='Pegar')

# Asignar el menú a la ventana principal
root.config(menu=menu)

# Mostrar la ventana
root.mainloop()