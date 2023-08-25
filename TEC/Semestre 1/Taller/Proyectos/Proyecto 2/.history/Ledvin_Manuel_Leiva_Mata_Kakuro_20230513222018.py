# Proyecto 2: Kakuro
# Ledvin Manuel Leiva Mata
# 2023071280

# Importar librerias
import tkinter as tk

# Crear ventana
kakuro = tk.Tk()
kakuro.title("Kakuro")
kakuro.geometry("1280x720")

# Menu principal

# Botones

playBtn = tk.Button(kakuro, text="Jugar", width=20, height=2)
SettingsBtn = tk.Button(kakuro, text="Configurar", width=20, height=2)
HelpBtn = tk.Button(kakuro, text="Ayuda", width=20, height=2)
AboutBtn = tk.Button(kakuro, text="Acerca de", width=20, height=2)
ExitBtn = tk.Button(kakuro, text="Salir", width=20, height=2)

# MainLoop

kakuro.mainloop()