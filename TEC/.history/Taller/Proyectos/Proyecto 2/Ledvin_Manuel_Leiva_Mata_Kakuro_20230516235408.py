# Proyecto 2: Kakuro
# Ledvin Manuel Leiva Mata
# 2023071280

# Importar librerias
import tkinter as tk

# Menu principal funciones

def create_gradient(canvas, x, y, width, height, color1, color2):
    for i in range(height):
        r = int(color1[0] * (height - i) / height + color2[0] * i / height)
        g = int(color1[1] * (height - i) / height + color2[1] * i / height)
        b = int(color1[2] * (height - i) / height + color2[2] * i / height)
        color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        canvas.create_line(x, y + i, x + width, y + i, fill=color, width=1)

# Crear ventana
root = tk.Tk()
root.title("Kakuro")
root.geometry("1280x720")

# Crear un lienzo (canvas) que ocupe toda la ventana
canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
canvas.pack()

# Definir los colores de inicio y fin para el degradado
color_inicio = (255, 255, 255)  # Blanco
color_fin = (0, 0, 255)  # Azul


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

# Botones
playBtn = tk.Button(root, text="Jugar", width=20, height=2)
SettingsBtn = tk.Button(root, text="Configurar", width=20, height=2)
HelpBtn = tk.Button(root, text="Ayuda", width=20, height=2)
AboutBtn = tk.Button(root, text="Acerca de", width=20, height=2)
ExitBtn = tk.Button(root, text="Salir", width=20, height=2)

# Posicionamiento
playBtn.pack()

# MainLoop

root.mainloop()