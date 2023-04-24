# Made by: Ledvin Manuel Leiva Mata
# 2023071280
# Date: 2021-09-15 14:21:00 hora de inicio

# Importamos las librerias necesarias
import os # Libreria para limpiar la consola
import sys # Libreria para salir del programa
import pycountry # Libreria para validar el pais
import datetime # Libreria para validar la fecha de nacimiento
import validate_email # Libreria para validar el correo electronico

# Menu principal

# Variables globales

disciplinas = [('Carreras de velocidad', 'T'), ('Saltos', 'M'), ('Lanzamientos', 'M')]

pruebas = [('V02', '200 m', 'U20', 'F', 'Carreras de velocidad'), ('S01', '100 m vallas', 'U20', 'F', 'Carreras de saltos'), ('V01', '100 m', 'MAYOR', 'M', 'Carreras de velocidad') ] 

categorias = ('U12', 'U13', 'U14', 'U15', 'U16', 'U17', 'U18', 'U20', 'MAYOR','MASTER')

atletas = [ [3123456789, 'Pedro', 'Pérez', 'Peraza', 'M', 'CRI', 15102000, 'pedropp@gmail.com', 55556789 ] ]

def menu_principal():
    
    print(' 1. Registrar disciplinas \n 2. Registrar pruebas por disciplina \n 3. Registrar atletas \n 4. Registrar eventos \n 5. Registrar marcas \n 6. Analisis de datos \n 7. Ayuda \n 8. Acerca de \n 9. Salir \n')


    try:
        opcion = int(input('Ingrese una opcion: '))
        os.system('cls')

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
                sys.exit()
            case _:
                print('Opcion no valida')
                menu_principal()
    
    except ValueError:
        print('\nOpcion no valida\n')
        menu_principal()


# 1 Registrar disciplinas

def registrar_disciplinas():
    
    print('EVENTOS DE ATLETISMO \n \nREGISTRAR DISCIPLINAS \n')
    print(' 1. Agregar disciplinas \n 2. Consultar disciplinas \n 3. Modificar disciplinas \n 4. Eliminar disciplinas \n 0. Salir \n')

    try:
        opcion = int(input('Ingrese una opcion: '))
        os.system('cls')

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

    

# 1.1 Agregar disciplinas

def agregar_disciplinas():
    
    # Entrada de nombre de la disciplina y validacion de que este sea unico, longitud minima de 5 caracteres y maxima de 30

    global disciplinas
    
    # Variables locales
    temp = ()
    os.system('cls')
    print('EVENTOS DE ATLETISMO \n \nAGREGAR DISCIPLINAS \n')

    nombre = input('Ingrese el nombre de la disciplina: ')
    os.system('cls')

    while len(nombre) < 5 or len(nombre) > 30:
        print('El nombre de la disciplina debe tener entre 5 y 30 caracteres')
        nombre = input('Ingrese el nombre de la disciplina: ')
        if nombre == 'C' or nombre == 'c':
            registrar_disciplinas()
    if nombre in disciplinas:
        print('ESTA DISCIPLINA YA ESTÁ REGISTRADA, NO SE PUEDE AGREGAR')
        nombre = input('Ingrese el nombre de la disciplina: ')
    else:
        temp += (nombre,)
    
    # Entrada de la forma de medir y validacion de que sea 'T' o 'M'

    forma_medir = input('Ingrese la forma de medir: ')
    
    while forma_medir != 'T' and forma_medir != 'M':
        print('La forma de medir debe ser T o M')
        forma_medir = input('Ingrese la forma de medir: ')
    
    temp += (forma_medir,)

    # Opcion de cancelar 'C' y salir al menu anterior y de aceptar 'A'

    opcion = input('Seleccion una opcion:\n A. Aceptar\n C. Cancelar\n ')
    if opcion == 'C' or opcion == 'c': # Si la opcion es cancelar se vuelve a llamar a la funcion
        registrar_disciplinas()
    elif opcion == 'A': # Si la opcion es aceptar se agrega la disciplina a la lista y se vuelve a llamar a la funcion
        disciplinas.append(temp)
        print('Disciplina agregada')
        print(disciplinas, '\n')
        registrar_disciplinas()
    else: # Si la opcion es invalida se vuelve a llamar a la funcion
        print('Opcion no valida')
        registrar_disciplinas()


# 1.2 Consultar disciplinas
def consultar_disciplinas():

    # Entrada de la disciplina a consultar y validacion de que este exista

    os.system('cls')
    print('EVENTOS DE ATLETISMO \n \nCONSULTAR DISCIPLINAS \n')

    nombre = input('Ingrese el nombre de la disciplina: ')
    for elemento in disciplinas:
        if nombre == elemento[0]:
            print('Nombre: ', elemento[0])
            print('Forma de medir: ', elemento[1], '\n')
            break
    else:
        if nombre == 'C' or nombre == 'c':
            registrar_disciplinas()
        print('ESTA DISCIPLINA NO ESTA REGISTRADA, NO SE PUEDE CONSULTAR')
        consultar_disciplinas()
    # Opcion aceptar 'A' y volver a llamar a la funcion
    opcion = input('Seleccion una opcion:\n A. Aceptar\n ')
    if opcion == 'A':
        registrar_disciplinas()
    else:
        print('Opcion no valida')
        registrar_disciplinas()
    


# 1.3 Modificar disciplinas
def modificar_disciplinas():
    
    global disciplinas
    # Entrada de la disciplina a modificar y validacion de que este exista

    print('EVENTOS DE ATLETISMO \n \nMODIFICAR DISCIPLINAS \n')

    nombre = input('Ingrese el nombre de la disciplina: ')
    for i, elemento in enumerate(disciplinas):
        if nombre == elemento[0]:
            nombre = input('Ingrese el nuevo nombre de la disciplina: ')
            while len(nombre) < 5 or len(nombre) > 30:
                print('El nombre de la disciplina debe tener entre 5 y 30 caracteres')
                nombre = input('Ingrese el nombre de la disciplina: ')
                if nombre == ' ': # Si el nombre no se modifica se mantiene el anterior
                    nombre = elemento[0]
                break
    else:
        if nombre == 'C' or nombre == ' ':
            os.system('cls')
            registrar_disciplinas()
        os.system('cls')
        print('ESTA DISCIPLINA NO ESTA REGISTRADA, NO SE PUEDE MODIFICAR')
        modificar_disciplinas()
    
    # Entrada de la nueva forma de medir y validacion de que sea 'T' o 'M'
    forma_medir = input('Ingrese la forma de medir: ')
    
    while forma_medir != 'T' and forma_medir != 'M':
        if forma_medir == '': # Si la forma de medir no se modifica se mantiene la anterior
            forma_medir = elemento[1]
            break
        os.system('cls')
        print('La forma de medir debe ser T o M')
        forma_medir = input('Ingrese la forma de medir: ')
    
    # Opcion de cancelar 'C' y de aceptar 'A' y confirmacion de valores

    print('Nombre: ', elemento[0], '\n')
    print('Nombre modificado: ', nombre, '\n')
    print('Forma de medir: ', elemento[1], '\n')
    print('Forma de medir modificada: ', forma_medir, '\n')

    opcion = input('Seleccion una opcion:\n A. Aceptar\n C. Cancelar\n ')
    if opcion == 'C' or opcion == 'c': # Si la opcion es cancelar se vuelve a llamar a la funcion
        os.system('cls')
        modificar_disciplinas()
    elif opcion == 'A': # Si la opcion es aceptar se modifica la disciplina de la lista y se vuelve a llamar a la funcion
        disciplinas[i] = (nombre, forma_medir)
        os.system('cls')
        print('Disciplina modificada')
        print(disciplinas, '\n')
        modificar_disciplinas()
    else: # Si la opcion es invalida se vuelve a llamar a la funcion
        os.system('cls')
        print('Opcion no valida')
        registrar_disciplinas()
    
# 1.4 Eliminar disciplinas
def eliminar_disciplinas():

    global disciplinas

    # To do: Validar que no se pueda eliminar una disciplina que este asociada a una prueba

    # Entrada de la disciplina a eliminar y validacion de que este exista
    print('EVENTOS DE ATLETISMO \n \nELIMINAR DISCIPLINAS \n')

    nombre = input('Ingrese el nombre de la disciplina: ')
    for elemento in disciplinas:
        if nombre == elemento[0]:
            print('Nombre: ', elemento[0])
            print('Forma de medir: ', elemento[1])
            break
    else:
        if nombre == 'C' or nombre == 'c':
            os.system('cls')
            registrar_disciplinas()
        os.system('cls')
        print('ESTA DISCIPLINA NO ESTA REGISTRADA, NO SE PUEDE ELIMINAR')
        eliminar_disciplinas()

    # Opcion de cancelar 'C' y de aceptar 'A'
    opcion = input('Seleccion una opcion:\n A. Aceptar\n C. Cancelar\n ')
    if opcion == 'C' or opcion == 'c': # Si la opcion es cancelar se vuelve a llamar a la funcion
        eliminar_disciplinas()
    elif opcion == 'A': # Si la opcion es aceptar se elimina la disciplina de la lista y se vuelve a llamar a la funcion
        # Confirmacion de la eliminacion
        confirmacion = input('Esta seguro que desea eliminar esta disciplina? S/N ')
        if confirmacion == 'S':
            disciplinas.remove(elemento)
            os.system('cls')
            print('Disciplina eliminada')
            print(disciplinas, '\n')
            eliminar_disciplinas()
        elif confirmacion == 'N':
            os.system('cls')
            eliminar_disciplinas()
        else:
            os.system('cls')
            print('Opcion no valida')
            eliminar_disciplinas()
        
    else: # Si la opcion es invalida se vuelve a llamar a la funcion
        os.system('cls')
        print('Opcion no valida')
        registrar_disciplinas()

####################################################################################################################################################

# 2 Registrar pruebas por disciplina

def registrar_pruebas():

    print('EVENTOS DE ATLETISMO \n \nREGISTRAR PRUEBAS POR DISCIPLINA \n')
    
    print('Seleccion una opcion:\n 1. Agregar pruebas\n 2. Consultar pruebas\n 3. Modificar pruebas\n 4. Eliminar pruebas\n 0. Salir\n ')

    try:
        opcion = int(input('Ingrese una opcion: '))
        os.system('cls')

        match opcion:
            case 1:
                agregar_pruebas()
            case 2:
                consultar_pruebas()
            case 3:
                modificar_pruebas()
            case 4:
                eliminar_pruebas()
            case 0:
                menu_principal()
            case _:
                print('Opcion no valida')
                registrar_pruebas()
    
    except ValueError:
        os.system('cls')
        print('\nOpcion no valida\n')
        registrar_pruebas()

# 2.0 Funciones auxiliares

# Validar codigo de la prueba
def validar_codigo(codigo):
    
    # el codigo tiene que ser un string de 3 caracteres de letras y numeros

    if isinstance(codigo, str) and len(codigo) == 3:
        for caracter in codigo:
            if caracter.isalnum(): # Si el caracter es alfanumerico
                return True
            else:
                return False

# Validar nombre de la prueba
def validar_nombre(nombre):
        
    # el nombre tiene que ser un string de 3 a 30 caracteres

    if isinstance(nombre, str) and len(nombre) >= 3 and len(nombre) <= 30:
        return True
    else:
        return False

# 2.1 Agregar pruebas

def agregar_pruebas():

    global categorias, pruebas
    
    # Solicitar codigo de la prueba y comprobar si este es unico

    print('EVENTOS DE ATLETISMO \n \nAGREGAR PRUEBAS \n')

    codigo = input('Ingrese el codigo de la prueba: ')

    for elemento in pruebas:
        if codigo == elemento[0]:
            print('ESTA PRUEBA YA ESTÁ REGISTRADA, NO SE PUEDE AGREGAR')
            agregar_pruebas()

    while not validar_codigo(codigo):
        if codigo == 'C' or codigo == 'c':
            os.system('cls')
            registrar_pruebas()
        print('El codigo debe ser un string de 3 caracteres de letras y numeros')
        codigo = input('Ingrese el codigo de la prueba: ')

    # Solicitar nombre de la prueba

    nombre = input('Ingrese el nombre de la prueba: ')
    

    while not validar_nombre(nombre):
        if nombre == 'C' or nombre == 'c':
            os.system('cls')
            registrar_pruebas()
        print('El nombre debe ser un string de 3 a 30 caracteres')
        nombre = input('Ingrese el nombre de la prueba: ')

    # solicitar categoria de la prueba

    categoria = input('Ingrese la categoria de la prueba: ')
    while categoria not in categorias:
        print('Categoria no valida')
        categoria = input('Ingrese la categoria de la prueba: ')
        if categoria == 'C':
            os.system('cls')
            agregar_pruebas()

    # solicitar sexo de la prueba (F/M)

    sexo = input('Ingrese el sexo de la prueba: ')
    while sexo not in ('F', 'M'):
        print('Sexo no valido')
        sexo = input('Ingrese el sexo de la prueba: ')
        if sexo == 'C' or sexo == 'c':
            os.system('cls')
            agregar_pruebas()

    # nombre de la disciplina

    disciplina = input('Ingrese el nombre de la disciplina: ')

    verificacion = True
    while verificacion:
        for elemento in disciplinas:
            if disciplina == elemento[0]:
                verificacion = False
                break
        else:
            if disciplina == 'C' or disciplina == 'c':
                os.system('cls')
                agregar_pruebas()
            print('Disciplina no valida')
            disciplina = input('Ingrese el nombre de la disciplina: ')

    # opcion de cancelar 'C' y de aceptar 'A'

    opcion = input('\nSeleccion una opcion:\n A. Aceptar\n C. Cancelar\n ')
    if opcion == 'C': # Si la opcion es cancelar se vuelve a llamar a la funcion
        agregar_pruebas()
    elif opcion == 'A': # Si la opcion es aceptar se agrega la prueba a la lista y se vuelve a llamar a la funcion
        pruebas.append((codigo, nombre, categoria, sexo, disciplina))
        os.system('cls')
        print('Prueba agregada\n')
        agregar_pruebas()
        


# 2.2 Consultar pruebas

def consultar_pruebas():

    # Solicitar codigo de la prueba y verificar si existe

    print('EVENTOS DE ATLETISMO \n \nCONSULTAR PRUEBAS \n')
    

    codigo = input('Ingrese el codigo de la prueba: ')

    for elemento in pruebas:
        if codigo == elemento[0]:
            print('Codigo de la prueba: ', elemento[0], '\nNombre de la prueba: ', elemento[1], '\nCategoria: ', elemento[2], '\nSexo (F/M): ', elemento[3], '\nNombre de la disciplina: ', elemento[4], '\n')
            consultar_pruebas()

    else:
        if codigo == 'C' or codigo == 'c':
            os.system('cls')
            registrar_pruebas()
        print('Prueba no encontrada')
        consultar_pruebas()

    # opcion de aceptar 'A' y volver a llamar a la funcion

    opcion = input('\nSeleccion una opcion:\n A. Aceptar\n ')
    while opcion != 'A':
        opcion = input('\nSeleccion una opcion:\n A. Aceptar\n ')
    os.system('cls')
    consultar_pruebas()


# 2.3 Modificar pruebas

def modificar_pruebas():

    global pruebas

    print('EVENTOS DE ATLETISMO \n \nMODIFICAR PRUEBAS \n')

    # Solicitar codigo de la prueba y verificar si existe

    codigo = input('Ingrese el codigo de la prueba: ')

    verify = True

    # To do: verificar la prueba no esta asociada a un evento

    while verify:
        for i, elemento in enumerate(pruebas):
            if codigo == elemento[0]:
                codigo = input('Ingrese el nuevo codigo de la prueba: ')
                if codigo == '':
                    codigo = elemento[0]
                while not validar_codigo(codigo):
                    codigo = input('Ingrese el nuevo codigo de la prueba: ')
                    print('El codigo debe ser de 3 caracteres de letras y numeros')
                verify = False
                break
        else:
            if codigo == 'C' or codigo == 'c':
                os.system('cls')
                registrar_pruebas()
            os.system('cls')
            print('Prueba no encontrada')
            codigo = input('Ingrese el codigo de la prueba: ')

    # Solicitar nombre de la prueba

    nombre = input('Ingrese el nombre de la prueba: ')
    

    while not validar_nombre(nombre):
        if nombre == 'C' or nombre == 'c':
            os.system('cls')
            registrar_pruebas()
        print('El nombre debe ser un string de 3 a 30 caracteres')
        nombre = input('Ingrese el nombre de la prueba: ')

    # solicitar categoria de la prueba

    categoria = input('Ingrese la categoria de la prueba: ')
    while categoria not in categorias:
        print('Categoria no valida')
        categoria = input('Ingrese la categoria de la prueba: ')
        if categoria == 'C':
            os.system('cls')
            agregar_pruebas()

    # solicitar sexo de la prueba (F/M)

    sexo = input('Ingrese el sexo de la prueba: ')
    while sexo not in ('F', 'M'):
        print('Sexo no valido')
        sexo = input('Ingrese el sexo de la prueba: ')
        if sexo == 'C' or sexo == 'c':
            os.system('cls')
            agregar_pruebas()

    # nombre de la disciplina

    disciplina = input('Ingrese el nombre de la disciplina: ')

    verificacion = True
    while verificacion:
        for elemento in disciplinas:
            if disciplina == elemento[0]:
                verificacion = False
                break
        else:
            if disciplina == 'C' or disciplina == 'c':
                os.system('cls')
                agregar_pruebas()
            print('Disciplina no valida')
            disciplina = input('Ingrese el nombre de la disciplina: ')

    # opcion de cancelar 'C' y de aceptar 'A' y confirmacion de valores

    print('Codigo de la prueba: ', elemento[0], '\nCodigo de la prueba modificado', codigo, '\nNombre de la prueba: ', elemento[1], '\nNombre de la prueba modificado: ', nombre, '\nCategoria: ', elemento[2], '\nCategoria modificado: ', categoria, '\nSexo (F/M): ', elemento[3], '\nSexo modificado: ', sexo, '\nNombre de la disciplina: ', elemento[4], '\nNombre de la disciplina modificado: ', disciplina, '\n')

    opcion = input('\nSeleccion una opcion:\n A. Aceptar\n C. Cancelar\n ')
    if opcion == 'C': # Si la opcion es cancelar se vuelve a llamar a la funcion
        modificar_pruebas()
    elif opcion == 'A': # Si la opcion es aceptar se agrega la prueba a la lista y se vuelve a llamar a la funcion
        pruebas[i] = (codigo, nombre, categoria, sexo, disciplina)
        os.system('cls')
        print('Prueba modificada\n')
        modificar_pruebas()
    else:
        os.system('cls')
        print('Opcion no valida\n')
        modificar_pruebas()

# 2.4 Eliminar pruebas

def eliminar_pruebas():
    
    global pruebas

    print('EVENTOS DE ATLETISMO \n \nELIMINAR PRUEBAS \n')

    # Solicitar codigo de la prueba y verificar si existe

    codigo = input('Ingrese el codigo de la prueba: ')

    verify = True

    # To do: verificar la prueba no esta asociada a un evento

    while verify:
        for i, elemento in enumerate(pruebas):
            if codigo == elemento[0]:
                verify = False
                break
        else:
            if codigo == 'C' or codigo == 'c':
                os.system('cls')
                registrar_pruebas()
            os.system('cls')
            print('Prueba no encontrada')
            codigo = input('Ingrese el codigo de la prueba: ')

    # opcion de cancelar 'C' y de aceptar 'A' y confirmacion de valores

    print('Codigo de la prueba: ', elemento[0], '\nNombre de la prueba: ', elemento[1], '\nCategoria: ', elemento[2], '\nSexo (F/M): ', elemento[3], '\nNombre de la disciplina: ', elemento[4], '\n')


    # To do: verificar la prueba no esta asociada a un evento

    opcion = input('\nSeleccion una opcion:\n A. Aceptar\n C. Cancelar\n ')
    if opcion == 'C': # Si la opcion es cancelar se vuelve a llamar a la funcion
        eliminar_pruebas()
    elif opcion == 'A': # Si la opcion es aceptar se elimina la prueba de la lista y se vuelve a llamar a la funcion
        # Confirmacion de eliminacion
        confirmacion = input('Esta seguro que desea eliminar la prueba? (S/N): ')
        if confirmacion == 'S' or confirmacion == 's':
            pruebas.pop(i)
            os.system('cls')
            print('Prueba eliminada\n')
            eliminar_pruebas()
        else:
            os.system('cls')
            print('Prueba no eliminada\n')
            eliminar_pruebas()
    else:
        os.system('cls')
        print('Opcion no valida\n')
        eliminar_pruebas()

####################################################################################################################################################

# 3 Registrar atletas

def registrar_atletas():
    
    print('EVENTOS DE ATLETISMO \n \nREGISTRAR ATLETAS \n')
    
    print('Seleccion una opcion:\n 1. Agregar atletas\n 2. Consultar atletas\n 3. Modificar atletas\n 4. Eliminar atletas\n 0. Salir\n ')

    try:
        opcion = int(input('Ingrese una opcion: '))
        os.system('cls')

        match opcion:
            case 1:
                agregar_atletas()
            case 2:
                consultar_atletas()
            case 3:
                modificar_atletas()
            case 4:
                eliminar_atletas()
            case 0:
                menu_principal()
            case _:
                print('Opcion no valida')
                registrar_atletas()
    
    except ValueError:
        os.system('cls')
        print('\nOpcion no valida\n')
        registrar_atletas()

# Funciones auxiliares

# Validar identificacion

def validar_identificacion(identificacion):
    
    # la identificacion debe ser un string de 9 a 20 caracteres y debe ser unico

    if isinstance(identificacion,str) and len(identificacion) >= 9 and len(identificacion) <= 20: # Verificar que la identificacion sea un string y que tenga entre 9 y 20 caracteres
        for elemento in atletas:
            if identificacion == elemento[0]:
                return False
        else:
            return True

# Validar nombre

def validar_nombre(nombre):
    # el nombre debe ser un string de 2 a 20 caracteres

    if isinstance(nombre,str) and len(nombre) >= 2 and len(nombre) <= 20: # Verificar que el nombre sea un string y que tenga entre 2 y 20 caracteres
        return True
    else:
        return False

# Validar apellido

def validar_apellido(apellido):
    # el apellido debe ser un string de 2 a 20 caracteres

    if isinstance(apellido,str) and len(apellido) >= 2 and len(apellido) <= 20: # Verificar que el apellido sea un string y que tenga entre 2 y 20 caracteres
        return True
    else:
        return False

# Validar pais

def validar_pais(pais):
    # el pais debe ser un string de 3 caracteres en codificacion ISO 3166-1 alpha-3

    try:
        country = pycountry.countries.get(alpha_3=pais.upper()) # Verificar que el pais sea un string de 3 caracteres en codificacion ISO 3166-1 alpha-3
        if country is None and len(pais) != 3:
            return False
        else:
            return True
    except:
        return False
    

# validar fecha de nacimiento

def validar_fecha_nacimiento(fecha_nacimiento):
    # la fecha de nacimiento debe ser un string con formato 'dd/mm/aaaa'
    try:
        datetime.datetime.strptime(fecha_nacimiento, '%d/%m/%Y') # Verificar que la fecha de nacimiento sea un string con formato 'dd/mm/aaaa'
        return True
    except ValueError:
        return False

# validar correo electronico

def validar_correo_electronico(correo_electronico):

    
    isvalid=validate_email(correo_electronico)

    if isvalid:

# validar telefono

# 3.1 Agregar atletas

def agregar_atletas():
    print('Agregar atletas')

# 3.2 Consultar atletas

def consultar_atletas():
    print('Consultar atletas')

# 3.3 Modificar atletas

def modificar_atletas():
    print('Modificar atletas')

# 3.4 Eliminar atletas

def eliminar_atletas():
    print('Eliminar atletas')

####################################################################################################################################################


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