# Proyecto 2: Kakuro
# Ledvin Manuel Leiva Mata
# 2023071280

# Importar librerias
import tkinter as tk
import time

# Funciones para el menu principal ------------------------------------------------------------------------------------------------------------------------------:

# Niveles

nivel_Casillas = ( # tupla con la partida 1 de este nivel
    ( 2, 25, 1, 2, 3 ),
    ( 2, 44, 1, 3, 7 ),
    ( 2, 20, 1, 5, 3 ),
    ( 2, 10, 1, 6, 2 ),
    ( 2, 39, 1, 8, 7 ),
    ( 1, 10, 2, 1, 2 ),
    ( 1, 10, 2, 4, 2),
    ( 1, 8, 2, 7, 1),
    ( 2, 17, 2, 7, 2),
    ) # fin de la tupla con la partida 1 de este nivel

# Jugar ------------------------------------------------------------------------------------------------------------------------------
def play():

    # Funciones para el juego ------------------------------------------------------------------------------------------------------------------------------:
    global running
    running = False

    # Iniciar juego
    def iniciarJuego():
        global accionesPasadas
        global accionesFuturas
        global running

        if not running:
            running = True

            accionesFuturas = []
            accionesPasadas = []
            iniciarCronometro()

    # eliminar numero de la casilla

    def borrarNumero():

        global casillaSeleccionada
        global accionesPasadas

        if running:
            if casillaSeleccionada != None:

                # Agregar accion a la lista de acciones pasadas

                accionesPasadas.append([casillaSeleccionada, casillaSeleccionada["text"], 'borrarNumero'])

                # Limpiar casilla
                casillaSeleccionada.config(text=" ")
                casillaSeleccionada = None
                
                for casilla in casillas.values():
                    if casilla["bg"] == "#00CCCC":
                        casilla.config(bg="white", fg="black")
                comprobarSumas()

    # deshacer accion

    def deshacerAccion():
        global casillaSeleccionada
        global accionesPasadas
        global accionesFuturas

        if running:

            accion = accionesPasadas.pop()
            accionesFuturas.append(accion)
            if accion[2] == 'colocarNumero':
                accion[0].config(text=' ')
            elif accion[2] == 'borrarNumero':
                accion[0].config(text=accion[1])
            comprobarSumas()
        

    # rehacer accion

    def rehacerAccion():
        global casillaSeleccionada
        global accionesPasadas
        global accionesFuturas

        if running:
            
            accion = accionesFuturas.pop()
            accionesPasadas.append(accion)

            if accion[2] == 'colocarNumero':
                accion[0].config(text=accion[1])
            elif accion[2] == 'borrarNumero':
                accion[0].config(text=' ')
            comprobarSumas()

    # Borrar juego

    def deleteJuego():
        global casillaSeleccionada
        global accionesPasadas
        global accionesFuturas
        global running

        if running:
            for casilla in casillas.values():
                casilla.config(text='')
                casillaSeleccionada = None
                accionesPasadas = []
                accionesFuturas = []
                casilla.config(bg="white", fg="black")
            running = False
        else: 
            Error1 = tk.Tk()
            Error1.title("ERROR")
            Error1.geometry(f"300x100+{Error1.winfo_screenwidth()//2-150}+{Error1.winfo_screenheight()//2-50}")
            Error1.resizable(False, False)
            
            # Crear etiqueta de error
            error = tk.Label(Error1, text="EL JUEGO NO HA INICIADO", font=("Eras Demi ITC", 12))
            error.pack(pady=10)

            # Boton de aceptar
            aceptar = tk.Button(Error1, text="Aceptar", font=("Eras Demi ITC", 12), command=Error1.destroy)
            aceptar.pack(pady=10)

            Error1.mainloop()

    # Terminar juego

    def endGame():

        global running

        if running:
            deleteJuego()

            # limpiar numeros seleccionados

            for numero in numeros.values():
                    if numero["bg"] == "#00CCCC":
                        numero.config(bg="white", fg="black")

            # limpiar casillas seleccionadas

            for casilla in casillas.values():
                            casilla.config(bg="white", fg="black")

            # Actualizar cronometro
                
            segundos.config(text='')
            minutos.config(text='')
            horas.config(text='')
        else:
            Error1 = tk.Tk()
            Error1.title("ERROR")
            Error1.geometry(f"300x100+{Error1.winfo_screenwidth()//2-150}+{Error1.winfo_screenheight()//2-50}")
            Error1.resizable(False, False)
            
            # Crear etiqueta de error
            error = tk.Label(Error1, text="EL JUEGO NO HA INICIADO", font=("Eras Demi ITC", 12))
            error.pack(pady=10)

            # Boton de aceptar
            aceptar = tk.Button(Error1, text="Aceptar", font=("Eras Demi ITC", 12), command=Error1.destroy)
            aceptar.pack(pady=10)

            Error1.mainloop()

    # Funciones secundarias: 

    # Iniciar cronometro
    def iniciarCronometro():

        global running
        running = True

        start_time = time.time()
        actualizarCronometro(start_time)

    # Actualizar cronometro

    def actualizarCronometro(start_time):
        if running:
            elapsed_time = time.time() - start_time
            hours = int(elapsed_time // 3600)
            mins = int(elapsed_time // 60)
            secs = int(elapsed_time - mins * 60.0)
            # Actualizar cronometro
            
            segundos.config(text=secs)
            minutos.config(text=mins)
            horas.config(text=hours)

            # Actualizar cada segundo

            segundos.after(1000, actualizarCronometro, start_time)
            

    # Seleccionar numero
    def seleccionarNumero(btn_id):

        global numero
        
        if running:
            # deseleccionar numeros
            for numero in numeros.values():
                if numero["bg"] == "#00CCCC":
                    numero.config(bg="white", fg="black")

            # Limpiar casillas

            for casilla in casillas.values():
                    if casilla["bg"] == "#00CCCC":
                        casilla.config(bg="white", fg="black")
            
            #Seleccionar numero

            numero = numeros[btn_id]
            
            if numero["bg"] == "#00CCCC":
                numero.config(bg="white", fg="black")
            else:
                numero.config(bg="#00CCCC", fg="black")

    # Acciones

    # Colocar numeros en el tablero
    def colocarNumero(btn_id):
        global numero
        global casillaSeleccionada
        global accionesPasadas

        casillaSeleccionada = casillas[btn_id]

        if running:
            
            if numero != None:
                casilla = casillas[btn_id]
                casilla.config(text=numero['text'])
                accionesPasadas.append([casilla, numero['text'], 'colocarNumero'])

                for numero in numeros.values():
                    if numero["bg"] == "#00CCCC":
                        numero.config(bg="white", fg="black")

                numero = casillaSeleccionada = None

                # Comprobar sumas

                comprobarSumas()
            else:
                # Limpiar casilla

                for casilla in casillas.values():
                    if casilla["bg"] == "#00CCCC":
                        casilla.config(bg="white", fg="black")

                if casillaSeleccionada["bg"] == "#00CCCC":
                    casillaSeleccionada.config(bg="white", fg="black")
                else:
                    casillaSeleccionada.config(bg="#00CCCC", fg="black")

    # Ventana confirmar borrar

    def confirmarBorrar():

        def si():
            confirmWindow.destroy()
            deleteJuego()

        confirmWindow = tk.Tk()
        confirmWindow.title('BORRAR JUEGO')
        confirmWindow.geometry(f"300x100+{confirmWindow.winfo_screenwidth()//2-150}+{confirmWindow.winfo_screenheight()//2-50}")
        confirmWindow.resizable(False, False)

        # Crear etiqueta de confirmacion
        confirmacion = tk.Label(confirmWindow, text=f"¿ESTA SEGURO DE BORRAR EL JUEGO?", font=("Eras Demi ITC", 12))
        confirmacion.pack(pady=10)

        # Boton de aceptar
        aceptar = tk.Button(confirmWindow, text="SI", font=("Eras Demi ITC", 12), command=si)
        aceptar.place(x=50, y=50)

        # Boton de cancelar
        cancelar = tk.Button(confirmWindow, text="NO", font=("Eras Demi ITC", 12), command=confirmWindow.destroy)
        cancelar.place(x=200, y=50)

        confirmWindow.mainloop()

    # Ventana confirmar terminar juego

    def confirmarTerminar():

        def si():
            confirmWindow.destroy()
            endGame()

        confirmWindow = tk.Tk()
        confirmWindow.title('TERMINAR JUEGO')
        confirmWindow.geometry(f"300x100+{confirmWindow.winfo_screenwidth()//2-150}+{confirmWindow.winfo_screenheight()//2-50}")
        confirmWindow.resizable(False, False)

        # Crear etiqueta de confirmacion
        confirmacion = tk.Label(confirmWindow, text=f"¿ESTA SEGURO DE TERMINAR EL JUEGO?", font=("Eras Demi ITC", 12))
        confirmacion.pack(pady=10)

        # Boton de aceptar
        aceptar = tk.Button(confirmWindow, text="SI", font=("Eras Demi ITC", 12), command=si)
        aceptar.place(x=50, y=50)

        # Boton de cancelar
        cancelar = tk.Button(confirmWindow, text="NO", font=("Eras Demi ITC", 12), command=confirmWindow.destroy)
        cancelar.place(x=200, y=50)

        confirmWindow.mainloop()

    # Comprobar sumas de filas y columnas ------------------------------------------------------------------------------------------------------------------------------

    def comprobarSumas():

        if running:
        # comprobar sumas de columnas
            for casilla in nivel_Casillas:
                if casilla[0] == 2:
                    suma = 0
                    for i in range(casilla[4]):
                        i += casilla[2]+1
                        if casillas[(i,casilla[3])]['text'] != ' ':
                            suma += int(casillas[(i,casilla[3])]['text'])
                    if casillas[(i,casilla[3])]['text'] != ' ':
                        if suma == casilla[1]:
                            for i in range(casilla[4]):
                                i += casilla[2]+1
                                casillas[(i,casilla[3])].config(bg="green", fg="white")
                        else:
                            tk.messagebox.showinfo("KAKURO GAME", "� ERROR !") 
                    else:
                        for i in range(casilla[4]):
                            i += casilla[2]+1
                            if casillas[(i,casilla[3])]['bg'] == 'green':
                                casillas[(i,casilla[3])].config(bg="yellow", fg="black")
                            else:
                                casillas[(i,casilla[3])].config(bg="white", fg="black")
                # comprobar sumas de filas
                elif casilla[0] == 1:
                    suma = 0
                    for i in range(casilla[4]):
                        i += casilla[3]+1
                        if casillas[(casilla[2],i)]['text'] != ' ':
                            suma += int(casillas[(casilla[2],i)]['text'])
                    if casillas[(casilla[2],i)]['text'] != ' ':
                        if suma == casilla[1]:
                            for i in range(casilla[4]):
                                i += casilla[3]+1
                                casillas[(casilla[2],i)].config(bg="green", fg="white")
                        else:
                            tk.messagebox.showinfo("KAKURO GAME", "� ERROR !") 
                    else:
                        for i in range(casilla[4]):
                            i += casilla[3]+1
                            if casillas[(casilla[2],i)]['bg'] == 'green':
                                casillas[(casilla[2],i)].config(bg="yellow", fg="black")
                            else:
                                casillas[(casilla[2],i)].config(bg="white", fg="black")

    # Jugada no valida

    def jugadaNoValida(text):
        Error1 = tk.Tk()
        Error1.title("JUGADA NO VALIDA")
        Error1.geometry(f"300x100+{Error1.winfo_screenwidth()//2-150}+{Error1.winfo_screenheight()//2-50}")
        Error1.resizable(False, False)
        
        # Crear etiqueta de error
        error = tk.Label(Error1, text="LA JUGADA NO ES VALIDA PORQUE', font=("Eras Demi ITC", 12))
        error.pack(pady=10)
        # Boton de aceptar
        aceptar = tk.Button(Error1, text="Aceptar", font=("Eras Demi ITC", 12), command=Error1.destroy)
        aceptar.pack(pady=10)
        Error1.mainloop()

    # Crear ventana de juego ------------------------------------------------------------------------------------------------------------------------------

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

    # Cargar tablero
    
        # Rellenar casillas bloqueadas

    for i in range(9):
        for j in range(9):
            canvas = tk.Canvas(Tablero, width=67, height=67, bg='#5c5c5c')
            canvas.grid(row=i, column=j)
    
    casillasBloqueadas = [] # lista con las casillas bloqueadas

    # Funcion para las casillas bloqueadas del tablero

    def crear_diagonal(canvas, x1, y1, x2, y2):
        canvas.create_line(x1, y1, x2, y2, width=2)  # Dibujar la línea diagonal
    def crear_texto(canvas, x, y, texto):
        canvas.create_text(x, y, text=texto, font=("Eras Demi ITC", 12), fill="black")  # Dibujar el texto

    # Dibujar las casillas bloqueadas
    for casilla in nivel_Casillas:
        if (casilla[2], casilla[3]) not in casillasBloqueadas:
            canvas = tk.Canvas(Tablero, width=67, height=67, bg='#5c5c5c')
            canvas.grid(row=casilla[2], column=casilla[3])
            casillasBloqueadas.append((casilla[2], casilla[3]))
            # Dibujar la división diagonal
            crear_diagonal(canvas, 0, 0, 66, 66)
            # Dibujar el texto
            for numeroCasilla in nivel_Casillas:
                if (numeroCasilla[2], numeroCasilla[3]) == (casilla[2], casilla[3]):
                    if numeroCasilla[0] == 1:
                        crear_texto(canvas, 50, 25, numeroCasilla[1])
                    elif numeroCasilla[0] == 2:
                        crear_texto(canvas, 25, 50, numeroCasilla[1])

    # Crear casillas

    casillas = {}

    # Funcion para colocar numeros en las casillas
    for lenCasillas in nivel_Casillas:
        if lenCasillas[0] == 1:
            for i in range(lenCasillas[4]): # Crear casillas horizontales
                i += lenCasillas[3] + 1
                casilla = tk.Button(Tablero, width=6, height=3, text=' ', command=lambda num_id=(lenCasillas[2],i): colocarNumero(num_id), bg="white", font=("Eras Demi ITC", 12))
                casilla.grid(row=lenCasillas[2], column=i)
                casillas[(lenCasillas[2],i)] = casilla
        elif lenCasillas[0] == 2: # Crear casillas verticales
            for i in range(lenCasillas[4]):
                i += lenCasillas[2] + 1
                casilla = tk.Button(Tablero, width=6, height=3, text=' ', command=lambda num_id=(i,lenCasillas[3]): colocarNumero(num_id), bg="white", font=("Eras Demi ITC", 12))
                casilla.grid(row=i, column=lenCasillas[3])
                casillas[(i,lenCasillas[3])] = casilla

    # Numeros
    numbersWrap = tk.Frame(playWindow, borderwidth=1, relief="solid")
    numbersWrap.place(x=850, y=350, anchor="center")

    numeros = {}

    for i in range(1,10):
        numero = tk.Button(numbersWrap, text=i, width=4, height=2, command=lambda num_id=i: seleccionarNumero(num_id), background='white', font=("Eras Demi ITC", 12))
        numero.grid(row=i, column=0)

        numeros[i] = numero

    # Botones de accion

    # Iniciar
    iniciar = tk.Button(playWindow, text="INICIAR JUEGO", width=15, height=2, font=("Eras Demi ITC", 12), background='#FF0066', command=iniciarJuego)
    iniciar.grid(row=1, column=0, padx=30, pady=(690,0))

    # Deshacer y Rehacer
    deshacer = tk.Button(playWindow, text="DESHACER", width=15, height=2, font=("Eras Demi ITC", 12), background='#C5E0B4', command=deshacerAccion)
    deshacer.grid(row=1, column=1, padx=30, pady=(690,0))
    rehacer = tk.Button(playWindow, text="REHACER", width=15, height=2, font=("Eras Demi ITC", 12), background='#0FD1DB', command=rehacerAccion)
    rehacer.grid(row=2, column=1, padx=30, pady=25)

    # Borrar casilla, Borrar juego y terminar juego

    borrarCasilla = tk.Button(playWindow, text="BORRAR CASILLA", width=15, height=2, font=("Eras Demi ITC", 12), background='#C9C9C9', command=borrarNumero)
    borrarCasilla.grid(row=1, column=2, padx=30, pady=(690,0))
    borrarJuego = tk.Button(playWindow, text="BORRAR JUEGO", width=15, height=2, font=("Eras Demi ITC", 12), background='#8DB3E2', command=confirmarBorrar)
    borrarJuego.grid(row=2, column=2, padx=30)
    terminarJuego = tk.Button(playWindow, text="TERMINAR JUEGO", width=15, height=2, font=("Eras Demi ITC", 12), background='#00B050', command=confirmarTerminar)
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
    horas = tk.Label(Contador, text="", font=("Eras Demi ITC", 12))
    horas.grid(row=1, column=0, padx=10, pady=10)

    # Minutos
    minutosTexto = tk.Label(Contador, text="Minutos", font=("Eras Demi ITC", 12))
    minutosTexto.grid(row=0, column=1, padx=10, pady=10)
    minutos = tk.Label(Contador, text="", font=("Eras Demi ITC", 12))
    minutos.grid(row=1, column=1, padx=10, pady=10)

    # Segundos
    segundosTexto = tk.Label(Contador, text="Segundos", font=("Eras Demi ITC", 12))
    segundosTexto.grid(row=0, column=2, padx=10, pady=10)
    segundos = tk.Label(Contador, text="", font=("Eras Demi ITC", 12))
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