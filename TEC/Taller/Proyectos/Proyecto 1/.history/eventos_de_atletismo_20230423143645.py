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
    print('Acerca de')

menu_principal()