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

# Crear un lienzo (canvas) que ocupe toda la ventana
canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
canvas.grid(row=0, column=0, sticky="nsew")  # Agregar al grid

# Configurar el grid para expandir el lienzo
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Definir los colores de inicio y fin para el degradado
color_inicio = (255, 255, 255)
color_fin = (0, 0, 255) 

# Crear el degradado en el lienzo
create_gradient(canvas, 0, 0, root.winfo_screenwidth(), root.winfo_screenheight(), color_inicio, color_fin)

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

# Botones
playBtn = tk.Button(root, text="Jugar", width=20, height=2)
SettingsBtn = tk.Button(root, text="Configurar", width=20, height=2)
HelpBtn = tk.Button(root, text="Ayuda", width=20, height=2)
AboutBtn = tk.Button(root, text="Acerca de", width=20, height=2)
ExitBtn = tk.Button(root, text="Salir", width=20, height=2)

# Posicionamiento
playBtn.grid(row=1, column=0)

# Configurar el botón para tener un fondo transparente
playBtn.configure(highlightthickness=0)

# MainLoop

root.mainloop()