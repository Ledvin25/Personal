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

# Botones
playBtn = tk.Button(root, text="Jugar", width=20, height=2)
SettingsBtn = tk.Button(root, text="Configurar", width=20, height=2)
HelpBtn = tk.Button(root, text="Ayuda", width=20, height=2)
AboutBtn = tk.Button(root, text="Acerca de", width=20, height=2)
ExitBtn = tk.Button(root, text="Salir", width=20, height=2)

# Posicionamiento
playBtn.grid(row=1, column=0)

# MainLoop

root.mainloop()