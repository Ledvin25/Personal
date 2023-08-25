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
        opcion = int(input('Ingrese una opcion: '))

        match opcion:
            case 1:
                agregar_disciplinas()
            case 2:
                consultar_disciplinas()
            case 3:
                modificar_disciplinas()
            case 4:
                eliminar_disciplinas()
            case 0:
                menu_principal()
            case _:
                print('Opcion no valida')
                registrar_disciplinas()
    
    except ValueError:
        print('\nOpcion no valida\n')
        registrar_disciplinas()
        
# Agregar disciplinas

def agregar_disciplinas():
    print('Agregar disciplinas')

    menu_principal()

# Consultar disciplinas

def consultar_disciplinas():
    print('Consultar disciplinas')

    menu_principal()

# Modificar disciplinas

def modificar_disciplinas():
    print('Modificar disciplinas')

    menu_principal()

# Eliminar disciplinas

def eliminar_disciplinas():
    print('Eliminar disciplinas')

    menu_principal()

####################################################################################################################################################

# 2 Registrar pruebas por disciplina

def registrar_pruebas():
    print('Registrar pruebas por disciplina')

    menu_principal()

# 3 Registrar atletas

def registrar_atletas():
    print('Registrar atletas')
    menu_principal()

# 4 Registrar eventos

def registrar_eventos():
    print('Registrar eventos')
    menu_principal()

# 5 Registrar marcas

def registrar_marcas():
    print('Registrar marcas')
    menu_principal()

# 6 Analisis de datos

def analisis_datos():
    print('Analisis de datos')
    menu_principal()

# 7 Ayuda

def ayuda():
    print('Ayuda')
    menu_principal()

# 8 Acerca de

def acerca_de():
    print(' Nombre: Eventos de atletismo \n Version: 1.0 \n Autor: Ledvin Manuel Leiva Mata \n Fecha: 2022-04-17 \n')
    menu_principal()


menu_principal()