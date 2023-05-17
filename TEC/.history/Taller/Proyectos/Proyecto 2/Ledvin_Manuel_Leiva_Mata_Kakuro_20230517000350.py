# Proyecto 2: Kakuro
# Ledvin Manuel Leiva Mata
# 2023071280

# Importar librerias
import tkinter as tk

# Menu principal funciones

# ------------------------------------------------------------------------------------------------------------------------------

# Crear ventana
root = tk.Tk()
root.title("Kakuro")
root.geometry("1280x720")

# ------------------------------------------------------------------------------------------------------------------------------

# Jugar
def play():
    print("Jugar")

# Configurar
def settings():
    print("Configurar")

# Ayuda
def help():
    print("Ayuda")

# Acerca de
def about():
    print("Acerca de")

# Salir
def exit():
    print("Salir")

# ------------------------------------------------------------------------------------------------------------------------------

# Para un color de fondo:
fondo_color = "blue"
fondo_label = tk.Label(root, bg=fondo_color)

# Posicionar la etiqueta de fondo en la ventana principal
fondo_label.grid(row=0, column=0, sticky="nsew")

# Configurar el grid para expandir el fondo a lo largo de toda la ventana
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Agregar otros elementos utilizando el grid
label1 = tk.Label(root, text="Elemento 1")
label1.grid(row=1, column=0)

label2 = tk.Label(root, text="Elemento 2")
label2.grid(row=2, column=0)

button = tk.Button(root, text="Botón")
button.grid(row=3, column=0)

# MainLoop

root.mainloop()