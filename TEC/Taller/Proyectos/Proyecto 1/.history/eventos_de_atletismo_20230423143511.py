# Made by: Ledvin Manuel Leiva Mata
# 2023071280
# Date: 2021-09-15 14:21:00 hora de inicio

# Importamos las librerias necesarias

# Menu principal

def menu_principal():
    
    print('1. Registrar disciplinas \n 2. Registrar prubas por disciplina \n 3. Registrar atletas \n 4. Registrar eventos \n 5. Registrar marcas \n 6. Analisis de datos \n 7 Ayuda \n 8. Acerca de \n 9. Salir \n')

    opcion = int(input('Ingrese una opcion: '))

    match opcion:
        case 1:
            print('Registrar disciplinas')
        case 2:
            print('Registrar pruebas por disciplina')
        case 3:
            print('Registrar atletas')
        case 4:
            print('Registrar eventos')
        case 5:
            print('Registrar marcas')
        case 6:
            print('Analisis de datos')
        case 7:
            print('Ayuda')
        case 8:
            print('Acerca de')
        case 9:
            print('Salir')


# 1 Registrar disciplinas

def registrar_disciplinas():
    print('Registrar disciplinas')

# 2 Registrar pruebas por disciplina

def registrar_pruebas():
    print('Registrar pruebas por disciplina')

# 3 Registrar atletas

def registrar_atletas():
    print('Registrar atletas')

# 4 Registrar eventos

def registrar_eventos()

# 5 Registrar marcas

# 6 Analisis de datos

menu_principal()