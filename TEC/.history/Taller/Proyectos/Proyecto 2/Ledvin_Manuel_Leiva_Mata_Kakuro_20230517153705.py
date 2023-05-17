# Proyecto 2: Kakuro
# Ledvin Manuel Leiva Mata
# 2023071280

# Importar librerias
import tkinter as tk

# Funciones para el menu principal ------------------------------------------------------------------------------------------------------------------------------:

# Jugar ------------------------------------------------------------------------------------------------------------------------------
def play():

    # Funciones para el juego

    # Cambiar color de numeros

    def seleccionarNumero(btn_id):
        
        
        numero = numeros[btn_id]

        if numero["bg"] == "#00CCCC":
            numero.config(bg="white", fg="black")
        else:
            numero.config(bg="#00CCCC", fg="black")
            

    root.destroy()
    playWindow = tk.Tk()
    playWindow.title("KAKURO GAME")
    playWindow.geometry(f"1000x1000+{playWindow.winfo_screenwidth()//2-500}+{playWindow.winfo_screenheight()//2-500}")
    playWindow.maxsize(width=1000, height=1000)
    playWindow.minsize(width=1000, height=1000)

    # Header
    KakuroText = tk.Label(playWindow, text="Kakuro", font=("Eras Bold ITC", 25))
    playerNameLabel = tk.Label(playWindow, text="Nombre de usuario:", font=("Eras Demi ITC", 12))
    playerName = tk.Entry(playWindow, width=20, font=("Eras Demi ITC", 12))

    # Tablero 

    Tablero = tk.Frame(playWindow, borderwidth=1, relief="solid")

    # Posicionamiento
    KakuroText.grid(row=0, column=0,  padx=30)
    playerNameLabel.grid(row=0, column=2)
    playerName.grid(row=0, column=3 )
    Tablero.place(x=330, y=390, anchor="center")

    # Crear casillas
    for i in range(9):
        for j in range(9):
            casilla = tk.Button(Tablero, width=8, height=4)
            casilla.grid(row=i, column=j)

    # Numeros
    numbersWrap = tk.Frame(playWindow, borderwidth=1, relief="solid")
    numbersWrap.place(x=850, y=350, anchor="center")

    numeros = {}

    for i in range(1,9):
        numero = tk.Button(numbersWrap, text=i, width=6, height=3, command=lambda num_id=i: seleccionarNumero(num_id))
        numero.grid(row=i, column=0)

        numeros[i] = numero

    # Botones de accion

    # Iniciar
    iniciar = tk.Button(playWindow, text="INICIAR JUEGO", width=15, height=2, font=("Eras Demi ITC", 12), background='#FF0066')
    iniciar.grid(row=1, column=0, padx=30, pady=(690,0))

    # Deshacer y Rehacer
    deshacer = tk.Button(playWindow, text="DESHACER", width=15, height=2, font=("Eras Demi ITC", 12), background='#C5E0B4')
    deshacer.grid(row=1, column=1, padx=30, pady=(690,0))
    rehacer = tk.Button(playWindow, text="REHACER", width=15, height=2, font=("Eras Demi ITC", 12), background='#0FD1DB')
    rehacer.grid(row=2, column=1, padx=30, pady=25)

    # Borrar casilla, Borrar juego y terminar juego

    borrarCasilla = tk.Button(playWindow, text="BORRAR CASILLA", width=15, height=2, font=("Eras Demi ITC", 12), background='#C9C9C9')
    borrarCasilla.grid(row=1, column=2, padx=30, pady=(690,0))
    borrarJuego = tk.Button(playWindow, text="BORRAR JUEGO", width=15, height=2, font=("Eras Demi ITC", 12), background='#8DB3E2')
    borrarJuego.grid(row=2, column=2, padx=30)
    terminarJuego = tk.Button(playWindow, text="TERMINAR JUEGO", width=15, height=2, font=("Eras Demi ITC", 12), background='#00B050')
    terminarJuego.grid(row=3, column=2, padx=30)

    # Top 10, guardar juego y cargar juego

    top10 = tk.Button(playWindow, text="TOP 10", width=15, height=2, font=("Eras Demi ITC", 12), background='#FFFF00')
    top10.grid(row=1, column=3, padx=30, pady=(690,0))
    guardarJuego = tk.Button(playWindow, text="GUARDAR JUEGO", width=15, height=2, font=("Eras Demi ITC", 12), background='#ED7D31')
    guardarJuego.grid(row=2, column=3, padx=30, pady=0)
    cargarJuego = tk.Button(playWindow, text="CARGAR JUEGO", width=15, height=2, font=("Eras Demi ITC", 12), background='#C55A11')
    cargarJuego.grid(row=3, column=3, padx=30, pady=0)

    # Contador
    Contador = tk.Frame(playWindow, borderwidth=1, relief="solid")
    Contador.grid(row= 2, column=0, padx=20, pady=(20,0))

    # Horas
    horasTexto = tk.Label(Contador, text="Horas", font=("Eras Demi ITC", 12))
    horasTexto.grid(row=0, column=0, padx=10, pady=10)
    horas = tk.Label(Contador, text="00", font=("Eras Demi ITC", 12))
    horas.grid(row=1, column=0, padx=10, pady=10)

    # Minutos
    minutosTexto = tk.Label(Contador, text="Minutos", font=("Eras Demi ITC", 12))
    minutosTexto.grid(row=0, column=1, padx=10, pady=10)
    minutos = tk.Label(Contador, text="00", font=("Eras Demi ITC", 12))
    minutos.grid(row=1, column=1, padx=10, pady=10)

    # Segundos
    segundosTexto = tk.Label(Contador, text="Segundos", font=("Eras Demi ITC", 12))
    segundosTexto.grid(row=0, column=2, padx=10, pady=10)
    segundos = tk.Label(Contador, text="00", font=("Eras Demi ITC", 12))
    segundos.grid(row=1, column=2, padx=10, pady=10)

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

KakuroText = tk.Label(root, text="Kakuro", font=("Eras Demi ITC", 50), bg="#1a2f40", fg="#ffffff")
playBtn = tk.Button(root, text="Jugar", width=20, height=2, font=("Eras Demi ITC", 12), command=play)
SettingsBtn = tk.Button(root, text="Configurar", width=20, height=2, font=("Eras Demi ITC", 12), command=settings)
HelpBtn = tk.Button(root, text="Ayuda", width=20, height=2, font=("Eras Demi ITC", 12), command=help)
AboutBtn = tk.Button(root, text="Acerca de", width=20, height=2, command=about, font=("Eras Demi ITC", 12))
ExitBtn = tk.Button(root, text="Salir", width=20, height=2, command=lambda: root.destroy(), font=("Eras Bold ITC", 12))

madeby = tk.Label(root, text="Made by: Ledvin Leiva", font=("Eras Demi ITC", 10), bg="#1a2f40", fg="#ffffff")


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