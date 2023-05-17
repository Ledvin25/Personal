# Proyecto 2: Kakuro
# Ledvin Manuel Leiva Mata
# 2023071280

# Importar librerias
import tkinter as tk

# Funciones para el menu principal ------------------------------------------------------------------------------------------------------------------------------:

# Jugar ------------------------------------------------------------------------------------------------------------------------------
def play():
    root.destroy()
    playWindow = tk.Tk()
    playWindow.title("KAKURO GAME")
    playWindow.geometry(f"1000x1000+{playWindow.winfo_screenwidth()//2-500}+{playWindow.winfo_screenheight()//2-500}")
    playWindow.maxsize(width=1000, height=1000)
    playWindow.minsize(width=1000, height=1000)

    # Header
    KakuroText = tk.Label(playWindow, text="Kakuro", font=("Eras Bold ITC", 25))
    playerName = tk.Entry(playWindow, text= 'Nombre de usuario',  width=20, font=("Eras Bold ITC", 12))

    # Posicionamiento
    KakuroText.grid(row=0, column=0, columnspan=2)
    playerName.grid(row=1, column=0, columnspan=2)

    playWindow.mainloop()


# Configurar ------------------------------------------------------------------------------------------------------------------------------
def settings():
    print("Configurar")

# Ayuda ------------------------------------------------------------------------------------------------------------------------------
def help():
    print("Ayuda")

# Acerca de ------------------------------------------------------------------------------------------------------------------------------
def about():
    aboutWindow = tk.Tk()
    aboutWindow.title("Acerca de")
    aboutWindow.geometry(f"400x200+{aboutWindow.winfo_screenwidth()//2-150}+{aboutWindow.winfo_screenheight()//2-100}")

    aboutText = tk.Label(aboutWindow, text="KAKURO\n\nLedvin Manuel Leiva Mata\n\nVersion 1.0", font=("Eras Bold ITC", 12))
    aboutText.place(x=200, y=100, anchor="center")

    aboutWindow.mainloop()

# Menu Principal ------------------------------------------------------------------------------------------------------------------------------

# Crear ventana
root = tk.Tk()
root.title("Kakuro")
root.geometry(f"1280x720+{root.winfo_screenwidth()//2-640}+{root.winfo_screenheight()//2-360}")
root.maxsize(width=1280, height=720)
root.minsize(width=1280, height=720)
root.configure(bg="#1a2f40")

# Botones

KakuroText = tk.Label(root, text="Kakuro", font=("Eras Bold ITC", 50), bg="#1a2f40", fg="#ffffff")
playBtn = tk.Button(root, text="Jugar", width=20, height=2, font=("Eras Bold ITC", 12), command=play)
SettingsBtn = tk.Button(root, text="Configurar", width=20, height=2, font=("Eras Bold ITC", 12), command=settings)
HelpBtn = tk.Button(root, text="Ayuda", width=20, height=2, font=("Eras Bold ITC", 12), command=help)
AboutBtn = tk.Button(root, text="Acerca de", width=20, height=2, command=about, font=("Eras Bold ITC", 12))
ExitBtn = tk.Button(root, text="Salir", width=20, height=2, command=lambda: root.destroy(), font=("Eras Bold ITC", 12))

madeby = tk.Label(root, text="Made by: Ledvin Leiva", font=("Eras Bold ITC", 10), bg="#1a2f40", fg="#ffffff")


# Posicionamiento
KakuroText.place(x=640, y=150, anchor="center")
playBtn.place(x=640, y=260, anchor="center")
SettingsBtn.place(x=640, y=340, anchor="center")
HelpBtn.place(x=640, y=420, anchor="center")
AboutBtn.place(x=640, y=500, anchor="center")
ExitBtn.place(x=640, y=580, anchor="center")
madeby.place(x= 1200, y=700, anchor="center")

# ------------------------------------------------------------------------------------------------------------------------------
# MainLoop
play()