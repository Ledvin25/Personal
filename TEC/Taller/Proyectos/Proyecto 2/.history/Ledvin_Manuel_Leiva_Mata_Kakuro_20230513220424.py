# Proyecto 2: Kakuro
# Ledvin Manuel Leiva Mata
# 2023071280

# Importar librerias
import tkinter as tk


# Crear la ventana principal
root = tk.Tk()

# Crear el menú
menu = tk.Menu(root)

# Crear submenús
submenu1 = tk.Menu(menu)
submenu2 = tk.Menu(menu)

# Asignar el menú a la ventana principal
root.config(menu=menu)

# Mostrar la ventana
root.mainloop()