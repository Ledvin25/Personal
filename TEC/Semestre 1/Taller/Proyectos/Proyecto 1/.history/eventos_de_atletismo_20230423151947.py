# Made by: Ledvin Manuel Leiva Mata
# 2023071280
# Date: 2021-09-15 14:21:00 hora de inicio

# Importamos las librerias necesarias

# Menu principal

def menu_principal():
    
    print(' 1. Registrar disciplinas \n 2. Registrar prubas por disciplina \n 3. Registrar atletas \n 4. Registrar eventos \n 5. Registrar marcas \n 6. Analisis de datos \n 7. Ayuda \n 8. Acerca de \n 9. Salir \n')


    try:
        opcion = int(input('Ingrese una opcion: '))

        match opcion:
            case 1:
                registrar_disciplinas()
            case 2:
                registrar_pruebas()
            case 3:
                registrar_atletas()
            case 4:
                registrar_eventos()
            case 5:
                registrar_marcas()
            case 6:
                analisis_datos()
            case 7:
                ayuda()
            case 8:
                acerca_de()
            case 9:
                print('Gracias por usar el programa')
            case _:
                print('Opcion no valida')
                menu_principal()
    
    except ValueError:
        print('\nOpcion no valida\n')
        menu_principal()


# 1 Registrar disciplinas

def registrar_disciplinas():
    
    print(' 1. Agregar disciplinas \n 2. Consultar disciplinas \n 3. Modificar disciplinas \n 4. Eliminar disciplinas \n 0. Salir \n')


    try:
        lista_disciplinas = []
        opcion = int(input('Ingrese una opcion: '))

        match opcion:
            case 1:
                agregar_disciplinas(lista_disciplinas)
            case 2:
                consultar_disciplinas(lista_disciplinas)
            case 3:
                modificar_disciplinas(lista_disciplinas)
            case 4:
                eliminar_disciplinas(lista_disciplinas)
            case 0:
                menu_principal()
            case _:
                print('Opcion no valida')
                registrar_disciplinas()
    
    except ValueError:
        print('\nOpcion no valida\n')
        registrar_disciplinas()

    

# 1.1 Agregar disciplinas

    def agregar_disciplinas():
        
        # Entrada de nombre de la disciplina y validacion de que este sea unico, longitud minima de 5 caracteres y maxima de 30
        

        temp = ()

        while len(nombre) < 5 or len(nombre) > 30:
            print('El nombre de la disciplina debe tener entre 5 y 30 caracteres')
            nombre = input('Ingrese el nombre de la disciplina: ')
            if nombre == 'C':
                registrar_disciplinas()

        if nombre in lista_disciplinas:
            print('El nombre de la disciplina ya existe')
            nombre = input('Ingrese el nombre de la disciplina: ')
        else:
            temp += (nombre,)
        
        # Entrada de la forma de medir y validacion de que sea 'T' o 'M'

        while forma_medir != 'T' and forma_medir != 'M':
            print('La forma de medir debe ser T o M')
            forma_medir = input('Ingrese la forma de medir: ')
        
        temp += (forma_medir,)

        # Opcion de cancelar 'C' y salir al menu anterior y de aceptar 'A'

        opcion = input('Seleccion una opcion:\n A. Aceptar\n C. Cancelar\n ')

        if opcion == 'C': # Si la opcion es cancelar se vuelve a llamar a la funcion
            registrar_disciplinas()
        elif opcion == 'A': # Si la opcion es aceptar se agrega la disciplina a la lista y se vuelve a llamar a la funcion
            lista_disciplinas.append(temp)
            print('Disciplina agregada')
            print(lista_disciplinas)
            registrar_disciplinas()

def test_agregar_disciplinas():
    assert agregar_disciplinas('C') == 'C'

    # 1.2 Consultar disciplinas

    def consultar_disciplinas():
        print('Consultar disciplinas')

        

    # 1.3 Modificar disciplinas

    def modificar_disciplinas():
        print('Modificar disciplinas')

        

    # 1.4 Eliminar disciplinas

    def eliminar_disciplinas():
        print('Eliminar disciplinas')

####################################################################################################################################################

# 2 Registrar pruebas por disciplina

def registrar_pruebas():
    print('Registrar pruebas por disciplina')


# 3 Registrar atletas

def registrar_atletas():
    print('Registrar atletas')

# 4 Registrar eventos

def registrar_eventos():
    print('Registrar eventos')

# 5 Registrar marcas

def registrar_marcas():
    print('Registrar marcas')

# 6 Analisis de datos

def analisis_datos():
    print('Analisis de datos')

# 7 Ayuda

def ayuda():
    print('Ayuda')

# 8 Acerca de

def acerca_de():
    print(' Nombre: Eventos de atletismo \n Version: 1.0 \n Autor: Ledvin Manuel Leiva Mata \n Fecha: 2022-04-17 \n')


menu_principal()