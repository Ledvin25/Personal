# Proyecto 2: Kakuro
# Ledvin Manuel Leiva Mata
# 2023071280

# Importar librerias
import tkinter as tk
import time
import pickle
import random
import os

# Funciones para el menu principal ------------------------------------------------------------------------------------------------------------------------------:

# Niveles

nivel_Casillas = ()
iDificulty = 0
partidas = {}

# Jugar ------------------------------------------------------------------------------------------------------------------------------
def play():
    global iDificulty
    global casillas
    global nivel_Casillas
    global segundos
    global minutos
    global horas

        # comprobar que un nivel se haya escogido
    if iDificulty == 0:
        Error1 = tk.Tk()
        Error1.title("ERROR")
        Error1.geometry(f"300x100+{Error1.winfo_screenwidth()//2-150}+{Error1.winfo_screenheight()//2-50}")
        Error1.resizable(False, False)

        # Crear label
        
        label = tk.Label(Error1, text="Por favor, escoga un nivel\nen configuración", font=("Arial", 13))
        label.pack(pady=10)

        # Crear boton

        boton = tk.Button(Error1, text="OK", font=("Arial", 12), command=Error1.destroy)
        boton.pack(pady=10)

        Error1.mainloop()

    # Escoger nivel
    def escogerNivel():
        global iDificulty
        global casillas
        global nivel_Casillas
        global category

        numerosMostrados = []

        match iDificulty:
            case 1: category = "FÁCIL"
            case 2: category = "MEDIO"
            case 3: category = "DIFÍCIL"
            case 4: category = "EXPERTO"

        if len(partidas[category]) == len(numerosMostrados):
            numerosMostrados = []

        # Escoger nivel aleatorio
        nivelRandom = random.randrange(0, len(partidas[category]))

        # No se repitan los niveles
        while nivelRandom in numerosMostrados:
            nivelRandom = random.randrange(0, len(partidas[category]))
            
        # Agregar nivel a la lista de niveles mostrados
        numerosMostrados.append(nivelRandom)

        # Escoger nivel
        nivel_Casillas = partidas[category][nivelRandom]

    escogerNivel()


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
            playerName.config(state='disabled')

            accionesFuturas = []
            accionesPasadas = []

            if clockVar == 2 or clockVar == 1:
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
        global elapsed_time

        if running:
            for casilla in casillas.values():
                casilla.config(text='')
                casillaSeleccionada = None
                accionesPasadas = []
                accionesFuturas = []
                casilla.config(bg="white", fg="black")
                elapsed_time = 0
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
        global casillas

        if running:
            deleteJuego()

            # limpiar casillas
            casillas = {}

            # Escoger nivel
            escogerNivel()

            # Cargar tablero

            cargarTablero()

            # limpiar cronmetro

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

    # Guardar juego

    def saveGame():

        global running

        running = False
        
        casillas_save = {}
        accionesPasadas_save = []
        accionesFuturas_save = []

        # Decodifica las casillas para que el bendito pickle las pueda guardar en un .dat
        for casilla in casillas:
            casillas_save[casilla] = casillas[casilla]["text"]

        # Decodificar acciones pasadas

        for accion in accionesPasadas:
            info = accion[0].grid_info()
            colum = info['column']
            row = info['row']

            accionesPasadas_save.append([(colum, row), accion[1], accion[2]])

        # Decodificar acciones futuras

        for accion in accionesFuturas:
            info = accion[0].grid_info()
            colum = info['column']
            row = info['row']

            accionesFuturas_save.append([(colum, row), accion[1], accion[2]])
        
        # datos a guardar
        saved = [casillas_save, segundos['text'], minutos['text'], horas['text'], nivel_Casillas, elapsed_time]

        # guardar datos

        with open('TEC/Taller/Proyectos/Proyecto 2/kakuro2023juegoactual.dat', 'wb') as file:
            pickle.dump(saved, file)

        # cerrar
        file.close()

        # Volver al menu principal

        def volverMenu():
            save.destroy()
            playWindow.destroy()
            mainMenu()

        # Continuar

        def continuarJuego():
            global running
            global elapsed_time

            save.destroy()
            running = True
            iniciarCronometro()

        # Mensaje de continuar jugando y confirmacion de guardado

        save = tk.Tk()
        save.title("JUEGO GUARDADO")
        save.geometry(f"300x200+{save.winfo_screenwidth()//2-150}+{save.winfo_screenheight()//2-50}")
        save.resizable(False, False)

        # Crear etiqueta de juego guardado y de desea continuar jugando

        guardado = tk.Label(save, text="JUEGO GUARDADO", font=("Eras Demi ITC", 12))
        guardado.pack(pady=10)

        continuar = tk.Label(save, text="¿DESEA CONTINUAR JUGANDO?", font=("Eras Demi ITC", 12))
        continuar.pack(pady=10)

        # Boton de si o no

        si = tk.Button(save, text="SI", font=("Eras Demi ITC", 12), command=continuarJuego)
        si.pack(side=tk.LEFT, padx=10, pady=10)

        no = tk.Button(save, text="NO", font=("Eras Demi ITC", 12), command=volverMenu)
        no.pack(side=tk.RIGHT, padx=10, pady=10)

        save.mainloop()
        


    # Cargar juego

    def loadGame():

        global casillas
        global accionesPasadas
        global accionesFuturas
        global segundos
        global minutos
        global horas
        global nivel_Casillas
        global elapsed_time
        global running

        # Verificar si hay un juego guardado

        if not os.path.isfile('TEC/Taller/Proyectos/Proyecto 2/kakuro2023juegoactual.dat'):

            Error1 = tk.Tk()
            Error1.title("ERROR")
            Error1.geometry(f"300x100+{Error1.winfo_screenwidth()//2-150}+{Error1.winfo_screenheight()//2-50}")
            Error1.resizable(False, False)
            
            # Crear etiqueta de error
            error = tk.Label(Error1, text="NO HAY JUEGO GUARDADO", font=("Eras Demi ITC", 12))
            error.pack(pady=10)

            # Boton de aceptar
            aceptar = tk.Button(Error1, text="Aceptar", font=("Eras Demi ITC", 12), command=Error1.destroy)
            aceptar.pack(pady=10)

            Error1.mainloop()

        if not running:
            iniciarJuego()
            running = False

            casillas = {}

            # abrir archivo
            with open('TEC/Taller/Proyectos/Proyecto 2/kakuro2023juegoactual.dat', 'rb') as file:
                saved = pickle.load(file)
            
            # cerrar archivo
            file.close()

            # cargar datos

            casillas_save = saved[0]
            segundos_save = saved[1]
            minutos_save = saved[2]
            horas_save = saved[3]
            nivel_Casillas = saved[4]

            # Cargar tablero
            cargarTablero()

            # cargar casillas

            for casilla in casillas_save:
                casillas[casilla].config(text=casillas_save[casilla])

            # cargar cronometro

            elapsed_time = saved[5]

            segundos.config(text=segundos_save)
            minutos.config(text=minutos_save)
            horas.config(text=horas_save)

        else:

            Error1 = tk.Tk()
            Error1.title("ERROR")
            Error1.geometry(f"300x100+{Error1.winfo_screenwidth()//2-150}+{Error1.winfo_screenheight()//2-50}")
            Error1.resizable(False, False)
            
            # Crear etiqueta de error
            error = tk.Label(Error1, text="DEBE TERMINAR EL JUEGO ACTUAL", font=("Eras Demi ITC", 12))
            error.pack(pady=10)

            # Boton de aceptar
            aceptar = tk.Button(Error1, text="Aceptar", font=("Eras Demi ITC", 12), command=Error1.destroy)
            aceptar.pack(pady=10)

            Error1.mainloop()

    # top 10

    def top10():

        # abrir archivo

        with open('TEC/Taller/Proyectos/Proyecto 2/kakuro2023top10.dat', 'rb') as file:
            top10file = pickle.load(file)

            # Asignar nueva posicion si esta esta dentro del top 10

        if playerName.get() != "" and elapsed_time != 0:
            for i, position in enumerate(top10file[category]):
                if elapsed_time < position[2]:
                    top10file[category].insert(i, [position[0],playerName.get(), elapsed_time])
                    top10file[category].pop()
                    
                    # Actualizar posiciones
                    for j in range(i+1, len(top10file[category])):
                        top10file[category][j][0] = j+1
                break

            # guardar cambios
            with open('TEC/Taller/Proyectos/Proyecto 2/kakuro2023top10.dat', 'wb') as file:
                pickle.dump(top10file, file)
                file.close()

        # Mostrar top 10

        top = tk.Tk()
        top.title("TOP 10")
        top.geometry(f"1200x600+{top.winfo_screenwidth()//2-600}+{top.winfo_screenheight()//2-300}")
        top.resizable(False, False)

        # Crear etiqueta de top 10
        
        top10 = tk.Label(top, text="TOP 10", font=("Eras Demi ITC", 12))
        top10.pack(pady=10)

        # Crear tabla de top 10 - nivel

        for level in top10file:

            # Crear frame para cada nivel y usarlo como cuadricula

            frame = tk.Frame(top)
            frame.pack(pady=10)

            # Crear etiqueta de nivel


            ''''nivel = tk.Label(top, text=level, font=("Eras Demi ITC", 12))
            nivel.pack(pady=10)

            # Crear cuadricula para top 10 - encabezado

            pos = tk.Label(top, text="Posicion", font=("Eras Demi ITC", 12))
            

            # Crear tabla de top 10 - posiciones

            for position in top10file[level]:

                # Posicion
                pos = tk.Label(top, text=position[0], font=("Eras Demi ITC", 12))
                pos.pack(side=tk.LEFT, padx=10, pady=10)

                # Nombre
                name = tk.Label(top, text=position[1], font=("Eras Demi ITC", 12))
                name.pack(side=tk.LEFT, padx=10, pady=10)

                # Tiempo
                textTime = str(position[2]//3600) + ":" + str(position[2]//60) + ":" + str(position[2]%60)

                time = tk.Label(top, text=textTime, font=("Eras Demi ITC", 12))
                time.pack(side=tk.LEFT, padx=10, pady=10)'''

        # Boton de aceptar
        aceptar = tk.Button(top, text="Aceptar", font=("Eras Demi ITC", 12), command=top.destroy)
        aceptar.pack(pady=10)

        top.mainloop()

    # Funciones secundarias: 

    # Iniciar cronometro
    def iniciarCronometro():

        global running
        global elapsed_time

        running = True

        if elapsed_time == 0:
            elapsed_time = 0

        actualizarCronometro()

    # Actualizar cronometro

    def actualizarCronometro():

        global elapsed_time
        global running

        if running:
            elapsed_time += 1
            hours = int(elapsed_time // 3600)
            mins = int(elapsed_time // 60)
            secs = int(elapsed_time - mins * 60.0)
            # Actualizar cronometro
            
            segundos.config(text=secs)
            minutos.config(text=mins)
            horas.config(text=hours)

             # Comprobar tiempo limite

            if elapsed_time == limitTime and clockVar == 2:
                running = False
                gameOver()

            # Actualizar cada segundo

            segundos.after(1000, actualizarCronometro)

    # Juego terminado

    def gameOver():
            
            global running

            # funciones de botones
            def continuarJuego():
                global running

                gameOver.destroy()
                running = True
                iniciarCronometro()

            def terminarJuego():
                global running

                gameOver.destroy()
                running = True
                endGame()

            # Crear ventana
    
            gameOver = tk.Tk()
            gameOver.title("GAME OVER")
            gameOver.geometry(f"300x200+{gameOver.winfo_screenwidth()//2-150}+{gameOver.winfo_screenheight()//2-50}")
            gameOver.resizable(False, False)
    
            # Crear etiqueta de juego terminado
    
            terminado = tk.Label(gameOver, text="TIEMPO LIMITE SUPERADO", font=("Eras Demi ITC", 12))
            terminado.pack(pady=10)
    
            # Boton de continuar jugando o terminar juego
    
            continuar = tk.Button(gameOver, text="CONTINUAR JUGANDO", font=("Eras Demi ITC", 12), command=continuarJuego)
            continuar.pack(pady=10)

            terminar = tk.Button(gameOver, text="TERMINAR JUEGO", font=("Eras Demi ITC", 12), command=terminarJuego)
            terminar.pack(pady=10)
    
            gameOver.mainloop()

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

                # comprobar que el numero no este en la misma fila o columna

                for i in range(9):
                    try: 
                        if casillas[(btn_id[0],i)]['text'] == numero['text'] or casillas[(i,btn_id[1])]['text'] == numero['text']:
                            jugadaNoValida(' EL \nNUMERO YA ESTA EN SU GRUPO DE FILA O COLUMNA')
                            return  # Salir de la funcion
                    except:
                        pass

                # agregar numero a la casilla
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
                            jugadaNoValida('LA SUMA DE LA COLUMNA ES ' + str(suma) + '\nY DEBERIA SER ' + str(casilla[1]))
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
                            jugadaNoValida('LA SUMA DE LA FILA ES ' + str(suma) + '\nY DEBERIA SER ' + str(casilla[1]))
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
        Error1.geometry(f"600x100+{Error1.winfo_screenwidth()//2-150}+{Error1.winfo_screenheight()//2-50}")
        Error1.resizable(False, False)
        
        # Crear etiqueta de error
        error = tk.Label(Error1, text='LA JUGADA NO ES VALIDA PORQUE' + text, font=("Eras Demi ITC", 12))
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

    def cargarTablero():

        global casillas

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

    cargarTablero()

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

    top10btn = tk.Button(playWindow, text="TOP 10", width=15, height=2, font=("Eras Demi ITC", 12), background='#FFFF00', command=top10)
    top10btn.grid(row=1, column=3, padx=30, pady=(690,0))
    guardarJuego = tk.Button(playWindow, text="GUARDAR JUEGO", width=15, height=2, font=("Eras Demi ITC", 12), background='#ED7D31', command=saveGame)
    guardarJuego.grid(row=2, column=3, padx=30, pady=0)
    cargarJuego = tk.Button(playWindow, text="CARGAR JUEGO", width=15, height=2, font=("Eras Demi ITC", 12), background='#C55A11', command=loadGame)
    cargarJuego.grid(row=3, column=3, padx=30, pady=0)

    if clockVar == 1 or clockVar == 2:
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

    # funciones
    global iDificulty
    global nivel_Casillas
    global partidas
    global limitTime
    global clockVar

    iDificulty = 0
    clockVar = 0

    def dificulty():
        global iDificulty
        iDificulty += 1

        if iDificulty == 1:
            dificultyBtn.configure(text="FACIL")
        elif iDificulty == 2:
            dificultyBtn.configure(text="MEDIO")
        elif iDificulty == 3:
            dificultyBtn.configure(text="DIFICIL")
        elif iDificulty == 4:
            dificultyBtn.configure(text="EXPERTO")


        if iDificulty == 5:
            iDificulty = 0
            dificultyBtn.configure(text="SELECCIONE")

        cargarPartidas()

    def cargarPartidas():
        global nivel_Casillas
        global partidas

        with open('TEC/Taller/Proyectos/Proyecto 2/kakuro2023partidas.dat', 'rb') as file:
            partidas = pickle.load(file)
        
    # Ventana de error
 
    def errorWindow(text1):      
        
        errorWindow = tk.Toplevel()
        errorWindow.title("Error")
        errorWindow.geometry(f"500x150+{errorWindow.winfo_screenwidth()//2-150}+{errorWindow.winfo_screenheight()//2-50}")
        errorWindow.resizable(0,0)

        errorLabel = tk.Label(errorWindow, text=text1, font=("Eras Demi ITC", 12))
        errorLabel.pack(pady=(20,0))

        aceptar = tk.Button(errorWindow, text="ACEPTAR", width=15, height=2, font=("Eras Demi ITC", 12), background='#ED7D31', command=errorWindow.destroy)
        aceptar.pack(pady=(20,0))

        errorWindow.mainloop()

    # Tiempo limite
    
    def tiempoLimite():
        global limitTime

        time = [horas, minutos, segundos]

        for i in range(3):
            if time[i].get() == "":
                time[i] = 0
            else:
                time[i] = int(time[i].get())

        limitTime = time[0]*3600 + time[1]*60 + time[2]

        # Mensajes de error
        
        if time[0] > 2 and clockVar == 2:
            errorWindow("LAS HORAS TIENEN QUE ESTAR ENTRE 0 Y 2")
        elif 0 >= time[1] >= 59 and clockVar == 2:
            errorWindow("LOS MINUTOS TIENEN QUE ESTAR ENTRE 0 Y 59")
        elif 0 >= time[2] >= 59 and clockVar == 2:
            errorWindow("LOS SEGUNDOS TIENEN QUE ESTAR ENTRE 0 Y 59")
        else:
            settingsWindow.destroy()

    # Controlar el tiempo limite

    def clock():

        global clockVar
        clockVar += 1

        match clockVar:
            case 1:
                clockbtn.configure(text="Cronometro")
                horas.configure(state="disabled")
                minutos.configure(state="disabled")
                segundos.configure(state="disabled")
            case 2:
                clockbtn.configure(text="Timer")
                horas.configure(state="normal")
                minutos.configure(state="normal")
                segundos.configure(state="normal")
            case 3:
                clockbtn.configure(text="No usar")
                horas.configure(state="disabled")
                minutos.configure(state="disabled")
                segundos.configure(state="disabled")
            case 4:
                clockbtn.configure(text="SELECCIONE")
                clockVar = 0

            

    # crear ventana
    settingsWindow = tk.Tk()
    settingsWindow.title("CONFIGURACION")

    # tamaño de la ventana 500x600 en el centro de la pantalla
    settingsWindow.geometry(f"500x600+{settingsWindow.winfo_screenwidth()//2-250}+{settingsWindow.winfo_screenheight()//2-300}")

    # labels
    dificultyLabel = tk.Label(settingsWindow, text="DIFICULTAD", font=("Eras Demi ITC", 15))
    cronometroLabel = tk.Label(settingsWindow, text="CRONOMETRO", font=("Eras Demi ITC", 15))
    horasLabel = tk.Label(settingsWindow, text="HORAS", font=("Eras Demi ITC", 12))
    minutosLabel = tk.Label(settingsWindow, text="MINUTOS", font=("Eras Demi ITC", 12))
    segundosLabel = tk.Label(settingsWindow, text="SEGUNDOS", font=("Eras Demi ITC", 12))

    # botones
    dificultyBtn = tk.Button(settingsWindow, text="SELECCIONE", width=15, height=2, font=("Eras Demi ITC", 12), background='#FF0066', command=dificulty)
    cerrar = tk.Button(settingsWindow, text="CERRAR", width=15, height=2, font=("Eras Demi ITC", 12), background='#FF0066', command=tiempoLimite)

    # entrada cronometro, horas, minutos, segundos
    horas = tk.Entry(settingsWindow, width=5, font=("Eras Demi ITC", 12), state="disabled")
    minutos = tk.Entry(settingsWindow, width=5, font=("Eras Demi ITC", 12), state="disabled")
    segundos = tk.Entry(settingsWindow, width=5, font=("Eras Demi ITC", 12), state="disabled")

    # Boton de timer, cronometro o no usar

    clockbtn = tk.Button(settingsWindow, text="SELECCIONE", width=15, height=2, font=("Eras Demi ITC", 12), background='#FF0066', command=clock)

    # posicionamiento
    dificultyLabel.place(x=250, y=100, anchor="center")
    dificultyBtn.place(x=250, y=180, anchor="center")
    cronometroLabel.place(x=250, y=250, anchor="center")
    horasLabel.place(x=150, y=300, anchor="center")
    horas.place(x=150, y=350, anchor="center")
    minutosLabel.place(x=250, y=300, anchor="center")
    minutos.place(x=250, y=350, anchor="center")
    segundosLabel.place(x=350, y=300, anchor="center")
    segundos.place(x=350, y=350, anchor="center")
    clockbtn.place(x=250, y=400, anchor="center")
    cerrar.place(x=250, y=550, anchor="center")


    settingsWindow.mainloop()

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

def mainMenu():

    # Variables globales
    global elapsed_time
    global root

    elapsed_time = 0

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

    # Iniciar ventana
    root.mainloop()

# ------------------------------------------------------------------------------------------------------------------------------

# Iniciar programa

mainMenu()