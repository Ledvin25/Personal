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

atletas = [ ['3123456789', 'Pedro', 'Pérez', 'Peraza', 'M', 'CRI', '15/10/2000', 'pedropp@gmail.com', '55556789' ] ]

eventos = [[25, 'I Campeonato Centroamericano de atletismo', 'CRI', 'Parque La Sabana Costa Rica', '10/01/2023', '12/01/2023']]

marcas_por_evento = [25, ['V02', ('3123456789', 2, 1302),]]

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

# funciones auxiliares

# Validar nombre

def validar_nombre(nombre):

    # Nombre debe ser un string de 5 a 30 caracteres

    if isinstance(nombre, str) and len(nombre) >= 5 and len(nombre) <= 30:
        return True
    else:
        return False

# 1.1 Agregar disciplinas

def agregar_disciplinas():
    
    # Entrada de nombre de la disciplina y validacion de que este sea unico, longitud minima de 5 caracteres y maxima de 30

    global disciplinas
    
    # Variables locales
    temp = ()
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
    print('EVENTOS DE ATLETISMO \n \nCONSULTAR DISCIPLINAS \n')

    nombre = input('Ingrese el nombre de la disciplina: ')
    for elemento in disciplinas:
        if nombre == elemento[0]:
            print('Nombre: ', elemento[0])
            print('Forma de medir: ', elemento[1], '\n')
            break
    else:
        if nombre == 'C' or nombre == 'c':
                os.system('cls')
                registrar_disciplinas()
        os.system('cls')
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

    verify = True

    while verify:

        for i, elemento in enumerate(disciplinas):
            if nombre == elemento[0]:
                nombre = input('Ingrese el nuevo nombre de la disciplina: ')
                if nombre == '': # Si el nombre no se modifica se mantiene el anterior
                        nombre = elemento[0]
                        verify = False
                        break
                while not validar_nombre(nombre):
                    print('El nombre de la disciplina debe tener entre 5 y 30 caracteres')
                    nombre = input('Ingrese el nombre de la disciplina: ')
                verify = False
                break
        else:
            if nombre == 'C' or nombre == 'c':
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
        os.system('cls')
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
            agregar_pruebas()

    # Solicitar nombre de la prueba

    nombre = input('Ingrese el nombre de la prueba: ')
    

    while not validar_nombre(nombre):
        if nombre == ' ':
            nombre = elemento[1]
            break
        print('El nombre debe ser un string de 3 a 30 caracteres')
        nombre = input('Ingrese el nombre de la prueba: ')

    # solicitar categoria de la prueba

    categoria = input('Ingrese la categoria de la prueba: ')
    while categoria not in categorias:
        if categoria == '':
            categoria = elemento[2]
            break
        print('Categoria no valida')
        categoria = input('Ingrese la categoria de la prueba: ')

    # solicitar sexo de la prueba (F/M)

    sexo = input('Ingrese el sexo de la prueba: ')
    while sexo not in ('F', 'M'):
        if sexo == '':
            sexo = elemento[3]
            break
        print('Sexo no valido')
        sexo = input('Ingrese el sexo de la prueba: ')

    # nombre de la disciplina

    disciplina = input('Ingrese el nombre de la disciplina: ')

    verificacion = True
    while verificacion:
        if disciplina == '':
                disciplina = elemento[4]
                verificacion = False
        for elemento1 in disciplinas:
            if disciplina == elemento1[0]:
                verificacion = False
                break
        else:
            if disciplina == 'C' or disciplina == 'c':
                os.system('cls')
                agregar_pruebas()
            print('Disciplina no valida')
            disciplina = input('Ingrese el nombre de la disciplina: ')

    # opcion de cancelar 'C' y de aceptar 'A' y confirmacion de valores

    os.system('cls')

    print('Codigo de la prueba: ', elemento[0], '\nCodigo de la prueba modificado', codigo, '\nNombre de la prueba: ', elemento[1], '\nNombre de la prueba modificado: ', nombre, '\nCategoria: ', elemento[2], '\nCategoria modificado: ', categoria, '\nSexo (F/M): ', elemento[3], '\nSexo modificado: ', sexo, '\nNombre de la disciplina: ', elemento[4], '\nNombre de la disciplina modificado: ', disciplina, '\n')

    opcion = input('\nSeleccion una opcion:\n A. Aceptar\n C. Cancelar\n ')
    
    while opcion != 'A' and opcion != 'C':
        opcion = input('\nSeleccion una opcion:\n A. Aceptar\n C. Cancelar\n ')
        if opcion == 'C': # Si la opcion es cancelar se vuelve a llamar a la funcion
            os.system('cls')
            print('Prueba no modificada\n')
            modificar_pruebas()
        elif opcion == 'A': # Si la opcion es aceptar se agrega la prueba a la lista y se vuelve a llamar a la funcion
            pruebas[i] = (codigo, nombre, categoria, sexo, disciplina)
            os.system('cls')
            print('Prueba modificada\n')
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
        os.system('cls')
        print('Prueba no eliminada\n')
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

    return True1
    isvalid=validate_email(correo_electronico) # Verificar que el correo electronico exista

    if isvalid:
        return True
    else:
        return False

# validar telefono

def validar_telefono(telefono):

    if telefono.isdigit() and len(telefono) >= 7 and len(telefono) <= 20: # Verificar que el telefono sea un string de 7 a 20 caracteres
        return True
    else:
        return False

# 3.1 Agregar atletas

def agregar_atletas():
    
    global atletas 

    print('EVENTOS DE ATLETISMO \n \nAGREGAR ATLETAS \n')

    # solicitar indentificacion del atleta y verificar que no exista

    idenfiticacion = input('Ingrese la identificacion del atleta: ')
    for elemento in atletas:
        if idenfiticacion == elemento[0]:
            os.system('cls')
            print('ESTE ATLETA YA ESTA REGISTRADO, NO SE PUEDE AGREGAR')
            agregar_atletas()

    while not validar_identificacion(idenfiticacion):
        if idenfiticacion == 'C' or idenfiticacion == 'c':
            os.system('cls')
            registrar_atletas()
        print('IDENTIFICACION INVALIDA')
        idenfiticacion = input('Ingrese la identificacion del atleta: ')

    # solicitar nombre del atleta

    nombre = input('Ingrese el nombre del atleta: ')
    while not validar_nombre(nombre):
        print('NOMBRE INVALIDO')
        nombre = input('Ingrese el nombre del atleta: ')

    # solicitar apellidos del atleta

    apellido1 = input('Ingrese el primer apellido del atleta: ')
    while not validar_apellido(apellido1):
        print('PRIMER APELLIDO INVALIDO')
        apellido1 = input('Ingrese el primer apellido del atleta: ')
    
    apellido2 = input('Ingrese el segundo apellido del atleta: ')
    while not validar_apellido(apellido2):
        print('SEGUNDO APELLIDO INVALIDO')
        apellido2 = input('Ingrese el segundo apellido del atleta: ')

    # solicitar sexo del atleta

    sexo = input('Ingrese el sexo del atleta (M/F): ')
    while sexo != 'M' and sexo != 'F':
        print('SEXO INVALIDO')
        sexo = input('Ingrese el sexo del atleta (M/F): ')

    # solicitar pais que representa

    pais = input('Ingrese el pais que representa el atleta "Codigo de 3 caracteres": ')
    while not validar_pais(pais):
        print('CODIGO DE PAIS INVALIDO')
        pais = input('Ingrese el pais que representa el atleta "Codigo de 3 caracteres": ')

    # solicitar fecha de nacimiento

    fecha_nacimiento = input('Ingrese la fecha de nacimiento del atleta "dd/mm/aaaa": ')
    while not validar_fecha_nacimiento(fecha_nacimiento):
        print('FECHA DE NACIMIENTO INVALIDA')
        fecha_nacimiento = input('Ingrese la fecha de nacimiento del atleta "dd/mm/aaaa": ')

    # solicitar correo electronico

    correo_electronico = input('Ingrese el correo electronico del atleta: ')
    while not validar_correo_electronico(correo_electronico):
        print('CORREO ELECTRONICO INVALIDO')
        correo_electronico = input('Ingrese el correo electronico del atleta: ')

    # solicitar telefono

    telefono = input('Ingrese el telefono del atleta: ')
    while not validar_telefono(telefono):
        print('TELEFONO INVALIDO')
        telefono = input('Ingrese el telefono del atleta: ')

    # opcion de cancelar 'C' y de aceptar 'A'

    opcion = input('Presione "C" para cancelar o "A" para aceptar: ')

    while opcion != 'C' and opcion != 'c' and opcion != 'A' and opcion != 'a':
        print('OPCION INVALIDA')
        opcion = input('Presione "C" para cancelar o "A" para aceptar: ')

        if opcion == 'C':
        os.system('cls')
        print('ATLETA NO AGREGADO')
        agregar_atletas()
        elif opcion == 'A':
            os.system('cls')
            print('ATLETA AGREGADO')
            atletas.append([idenfiticacion,nombre,apellido1,apellido2,sexo,pais,fecha_nacimiento,correo_electronico,telefono])
            agregar_atletas()

# 3.2 Consultar atletas

def consultar_atletas():
    
    print('EVENTOS DE ATLETISMO \n \nCONSULTAR ATLETAS \n')

    # solicitar indentificacion del atleta

    idenfiticacion = input('Ingrese la identificacion del atleta: ')

    for elemento in atletas:
        if idenfiticacion == elemento[0]:
            print('IDENTIFICACION: ',elemento[0])
            print('NOMBRE: ',elemento[1])
            print('PRIMER APELLIDO: ',elemento[2])
            print('SEGUNDO APELLIDO: ',elemento[3])
            print('SEXO: ',elemento[4])
            print('PAIS: ',elemento[5])
            print('FECHA DE NACIMIENTO: ',elemento[6])
            print('CORREO ELECTRONICO: ',elemento[7])
            print('TELEFONO: ',elemento[8])
    else:
        if idenfiticacion == 'C' or idenfiticacion == 'c':
            os.system('cls')
            registrar_atletas()
        print('EL ATLETA NO ESTA REGISTRADO, NO SE PUEDE CONSULTAR')
        consultar_atletas()

    # opcion aceptar 'A'

    opcion = input('Presione "A" para aceptar: ')

    while opcion != 'A':
        opcion = input('\nSeleccion una opcion:\n A. Aceptar\n ')
    os.system('cls')
    consultar_atletas()
    

# 3.3 Modificar atletas

def modificar_atletas():
    
    global atletas

    print('EVENTOS DE ATLETISMO \n \nMODIFICAR ATLETAS \n')

    # solicitar indentificacion del atleta

    idenfiticacion = input('Ingrese la identificacion del atleta: ')

    verify = True

    # To do: verificar la prueba no esta asociada a un evento

    while verify:
        for i, elemento in enumerate(atletas):
            if idenfiticacion == elemento[0]:
                verify = False
                break
        else:
            if idenfiticacion == 'C' or idenfiticacion == 'c':
                os.system('cls')
                registrar_atletas()
            print('ATLETA NO ENCONTRADO')
            idenfiticacion = input('Ingrese la identificacion del atleta: ')

    # solicitar nombre del atleta

    nombre = input('Ingrese el nombre del atleta modificado modificado: ')
    while not validar_nombre(nombre):
        if nombre == ' ':
            nombre = elemento[1] 
        print('NOMBRE INVALIDO')
        nombre = input('Ingrese el nombre del atleta : ')

    # solicitar apellidos del atleta

    apellido1 = input('Ingrese el primer apellido del atleta modificado: ')
    while not validar_apellido(apellido1):
        if apellido1 == ' ':
            apellido1 = elemento[2]
        print('PRIMER APELLIDO INVALIDO')
        apellido1 = input('Ingrese el primer apellido del atleta modificado: ')
    
    apellido2 = input('Ingrese el segundo apellido del atleta modificado: ')
    while not validar_apellido(apellido2):
        if apellido2 == ' ':
            apellido2 = elemento[3]
        print('SEGUNDO APELLIDO INVALIDO')
        apellido2 = input('Ingrese el segundo apellido del atleta modificado: ')

    # solicitar sexo del atleta

    sexo = input('Ingrese el sexo del atleta (M/F) modificado: ')
    while sexo != 'M' and sexo != 'F':
        if sexo == ' ':
            sexo = elemento[4]
        print('SEXO INVALIDO')
        sexo = input('Ingrese el sexo del atleta (M/F) modificado: ')

    # solicitar pais que representa

    pais = input('Ingrese el pais que representa el atleta "Codigo de 3 caracteres" modificado: ')

    while not validar_pais(pais):
        if pais == ' ':
            pais = elemento[5]
        print('CODIGO DE PAIS INVALIDO')
        pais = input('Ingrese el pais que representa el atleta "Codigo de 3 caracteres" modificado: ')

    # solicitar fecha de nacimiento

    fecha_nacimiento = input('Ingrese la fecha de nacimiento del atleta "dd/mm/aaaa" modificado: ')
    while not validar_fecha_nacimiento(fecha_nacimiento):
        if fecha_nacimiento == ' ':
            fecha_nacimiento = elemento[6]
        print('FECHA DE NACIMIENTO INVALIDA')
        fecha_nacimiento = input('Ingrese la fecha de nacimiento del atleta "dd/mm/aaaa" modificado: ')

    # solicitar correo electronico

    correo_electronico = input('Ingrese el correo electronico del atleta modificado: ')
    while not validar_correo_electronico(correo_electronico):
        if correo_electronico == ' ':
            correo_electronico = elemento[7]
        print('CORREO ELECTRONICO INVALIDO')
        correo_electronico = input('Ingrese el correo electronico del atleta modificado: ')

    # solicitar telefono

    telefono = input('Ingrese el telefono del atleta modificado: ')
    while not validar_telefono(telefono):
        if telefono == ' ':
            telefono = elemento[8]
        print('TELEFONO INVALIDO')
        telefono = input('Ingrese el telefono del atleta modificado: ')

    # opcion aceptar 'A' o cancelar 'C'

    print('Identificacion: ',elemento[0], '\nNombre del atleta: ', elemento[1], '\nNombre modificado del atleta: ', nombre, '\nPrimer apellido: ', elemento[2], '\nPrimer apellido modificado: ', apellido1, '\nSegundo apellido: ', elemento[3], '\nSegundo apellido modificado: ', apellido2, '\nSexo: ', elemento[4], '\nSexo modificado: ', sexo, '\nPais: ', elemento[5], '\nPais modificado: ', pais, '\nFecha de nacimiento: ', elemento[6], '\nFecha de nacimiento modificado: ', fecha_nacimiento, '\nCorreo electronico: ', elemento[7], '\nCorreo electronico modificado: ', correo_electronico, '\nTelefono: ', elemento[8], '\nTelefono modificado: ', telefono, '\n') 

    opcion = input('\nSeleccion una opcion:\n A. Aceptar\n C. Cancelar\n ')

    if opcion == 'A':
        os.system('cls')
        print('ATLETA MODIFICADO')
        atletas[i] = [idenfiticacion,nombre,apellido1,apellido2,sexo,pais,fecha_nacimiento,correo_electronico,telefono]
        modificar_atletas()	

    elif opcion == 'C':
        os.system('cls')
        print('ATLETA NO MODIFICADO')
        modificar_atletas()
    else:
        print('OPCION INVALIDA')
        modificar_atletas()

        
# 3.4 Eliminar atletas

def eliminar_atletas():
    
    global atletas

    print('EVENTOS DE ATLETISMO \n \nELIMINAR ATLETAS \n')

    # solicitar indentificacion del atleta

    idenfiticacion = input('Ingrese la identificacion del atleta: ')

    verify = True

    # To do: verificar que el atleta no este asociado a un evento

    while verify:
        for i, elemento in enumerate(atletas):
            if idenfiticacion == elemento[0]:
                print
                verify = False
                break
        else:
            if idenfiticacion == 'C' or idenfiticacion == 'c':
                os.system('cls')
                registrar_atletas()
            print('ATLETA NO ENCONTRADO')
            idenfiticacion = input('Ingrese la identificacion del atleta: ')

    print ('Identificacion: ', elemento[0], '\nNombre: ', elemento[1], '\nPrimer apellido: ', elemento[2], '\nSegundo apellido: ', elemento[3], '\nSexo: ', elemento[4], '\nPais: ', elemento[5], '\nFecha de nacimiento: ', elemento[6], '\nCorreo electronico: ', elemento[7], '\nTelefono: ', elemento[8])

    # opcion aceptar 'A' o cancelar 'C'

    opcion = input('\nSeleccion una opcion:\n A. Aceptar\n C. Cancelar\n ')

    if opcion == 'A':

        # confirmar eliminacion

        opcion = input('\nEsta seguro que desea eliminar el atleta? (S/N): ')

        if opcion == 'S':
            os.system('cls')
            print('ATLETA ELIMINADO')
            atletas.pop(i)
            eliminar_atletas()

        elif opcion == 'N':
            os.system('cls')
            print('ATLETA NO ELIMINADO')
            eliminar_atletas()

    elif opcion == 'C':
        os.system('cls')
        print('ATLETA NO ELIMINADO')
        eliminar_atletas()
    else:
        print('OPCION INVALIDA')
        eliminar_atletas()


registrar_atletas()

####################################################################################################################################################


# 4 Registrar eventos

def registrar_eventos():

    print('EVENTOS DE ATLETISMO \n \nREGISTRAR EVENTOS \n')
    
    print('Seleccion una opcion:\n 1. Agregar eventos\n 2. Consultar eventos\n 3. Modificar eventos\n 4. Eliminar eventos\n 0. Salir\n ')

    try:
        opcion = int(input('Ingrese una opcion: '))
        os.system('cls')

        match opcion:
            case 1:
                agregar_eventos()
            case 2:
                consultar_eventos()
            case 3:
                modificar_eventos()
            case 4:
                eliminar_eventos()
            case 0:
                menu_principal()
            case _:
                print('Opcion no valida')
                registrar_eventos()
    
    except ValueError:
        os.system('cls')
        print('\nOpcion no valida\n')
        registrar_eventos()

# funciones auxiliares

# validar identificacion del evento

def validar_identificacion_evento(identificacion):

    # debe ser un entero mayor o igual a 1

    if isinstance(identificacion, int) and identificacion >= 1:
        return True
    else:
        return False

# validar nombre del evento

def validar_nombre_evento(nombre):

    # debe ser un string de 5 a 60 caracteres

    if isinstance(nombre, str) and len(nombre) >= 5 and len(nombre) <= 60:
        return True
    else:
        return False

#validar pais del evento (Se reutiliza la funcion validar_pais)

#lugar donde se llevo a cabo el evento

def validar_lugar_evento(lugar):

    # debe ser un string de 5 a 60 caracteres

    if isinstance(lugar, str) and len(lugar) >= 5 and len(lugar) <= 60:
        return True
    else:
        return False

# validar fecha del evento

def validar_fecha_evento(fecha_inicial, fecha_final):

    # validar que la fecha este en formato dd/mm/aaaa

    try:
        # verificar que la fecha final sea mayor a la fecha inicial
        fecha_inicial = datetime.strptime(fecha_inicial, '%d/%m/%Y').date()
        fecha_final = datetime.strptime(fecha_final, '%d/%m/%Y').date()

        if fecha_final > fecha_inicial:
            return True
        else:
            return False
    except ValueError:
        return False
    
# 4.1 Agregar eventos

def agregar_eventos():

    global eventos

    print('EVENTOS DE ATLETISMO \n \nAGREGAR EVENTOS \n')

    # solicitar identificacion del evento

    identificacion = int(input('Ingrese la identificacion del evento: '))
    while not validar_identificacion_evento(identificacion):
        os.system('cls')
        print('IDENTIFICACION INVALIDA')
        identificacion = input('Ingrese la identificacion del evento: ')

    # verificar que la identificacion no exista

    for elemento in eventos:
        if identificacion == elemento[0]:
            print('EVENTO YA REGISTRADO, NO SE PUEDE AGREGAR')
            agregar_eventos()

    # solicitar nombre del evento

    nombre = input('Ingrese el nombre del evento: ')
    while not validar_nombre_evento(nombre):
        print('NOMBRE INVALIDO')
        nombre = input('Ingrese el nombre del evento: ')

    # solicitar pais del evento

    pais = input('Ingrese el pais del evento: ')
    while not validar_pais(pais):
        print('PAIS INVALIDO')
        pais = input('Ingrese el pais del evento: ')

    # solicitar lugar del evento

    lugar = input('Ingrese el lugar del evento: ')
    while not validar_lugar_evento(lugar):
        print('LUGAR INVALIDO')
        lugar = input('Ingrese el lugar del evento: ')

    # solicitar fecha del evento

    fecha_inicial = input('Ingrese la fecha inicial del evento (dd/mm/aaaa): ')
    fecha_final = input('Ingrese la fecha final del evento (dd/mm/aaaa): ')
    while not validar_fecha_evento(fecha_inicial, fecha_final):
        print('FECHA INVALIDA')
        fecha_inicial = input('Ingrese la fecha inicial del evento (dd/mm/aaaa): ')
        fecha_final = input('Ingrese la fecha final del evento (dd/mm/aaaa): ')

    # opcion aceptar 'A' o cancelar 'C'

    opcion = input('\nSeleccion una opcion:\n A. Aceptar\n C. Cancelar\n ')

    if opcion == 'A':
        os.system('cls')
        print('EVENTO AGREGADO')
        eventos.append([identificacion,nombre,pais,lugar,fecha_inicial,fecha_final])
        agregar_eventos()

    elif opcion == 'C':
        os.system('cls')
        print('EVENTO NO AGREGADO')
        agregar_eventos()

    else:
        print('OPCION INVALIDA')
        agregar_eventos()

# 4.2 Consultar eventos

def consultar_eventos():

    print('EVENTOS DE ATLETISMO \n \nCONSULTAR EVENTOS \n')

    if len(eventos) == 0: # verificar si no hay eventos registrados
        print('NO HAY EVENTOS REGISTRADOS')
        registrar_eventos()

    else:

        # solicitar identificacion del evento
        identificacion = int(input('Ingrese la identificacion del evento: '))
        
        for elemento in eventos: 
            if identificacion == elemento[0]:
                print('Identificacion: ', elemento[0])
                print('Nombre: ', elemento[1])
                print('Pais: ', elemento[2])
                print('Lugar: ', elemento[3])
                print('Fecha inicial: ', elemento[4])
                print('Fecha final: ', elemento[5])
        else:
            if identificacion == 'C' or identificacion == 'c':
                os.system('cls')
                registrar_eventos()
            os.system('cls')
            print('EVENTO NO ESTA REGISTRADO, NO SE PUEDE CONSULTAR')
            consultar_eventos()


        # opcion aceptar 'A'
        opcion = input('Seleccion una opcion:\n A. Aceptar\n ')

        while opcion != 'A':
            print('OPCION INVALIDA')
            opcion = input('Seleccion una opcion:\n A. Aceptar\n ')
        consultar_eventos()

# 4.3 Modificar eventos

def modificar_eventos():

    global eventos

    print('EVENTOS DE ATLETISMO \n \nMODIFICAR EVENTOS \n')

    # solicitar identificacion del evento

    identificacion = int(input('Ingrese la identificacion del evento: '))

    verify = True

    # verificar que la identificacion exista

    identificacion = int(input('Ingrese la identificacion del evento: '))

    while verify:
        for i, elemento in enumerate(eventos):
            if identificacion == elemento[0]:
                verify = False
        if identificacion == 'C' or identificacion == 'c':
            os.system('cls')
            registrar_eventos()
        else:
            print('EVENTO NO ESTA REGISTRADO, NO SE PUEDE MODIFICAR')
            identificacion = int(input('Ingrese la identificacion del evento: '))

    # solicitar nombre del evento

    nombre = input('Ingrese el nombre del evento: ')

    while not validar_nombre_evento(nombre):
        print('NOMBRE INVALIDO')
        nombre = input('Ingrese el nombre del evento: ')

    # solicitar pais del evento

    pais = input('Ingrese el pais del evento: ')

    while not validar_pais(pais):
        print('PAIS INVALIDO')
        pais = input('Ingrese el pais del evento: ')

    # solicitar lugar del evento

    lugar = input('Ingrese el lugar del evento: ')

    while not validar_lugar_evento(lugar):
        print('LUGAR INVALIDO')
        lugar = input('Ingrese el lugar del evento: ')

    # solicitar fecha del evento

    fecha_inicial = input('Ingrese la fecha inicial del evento (dd/mm/aaaa): ')
    fecha_final = input('Ingrese la fecha final del evento (dd/mm/aaaa): ')

    while not validar_fecha_evento(fecha_inicial, fecha_final):
        print('FECHA INVALIDA')
        fecha_inicial = input('Ingrese la fecha inicial del evento (dd/mm/aaaa): ')
        fecha_final = input('Ingrese la fecha final del evento (dd/mm/aaaa): ')

    # opcion aceptar 'A' o cancelar 'C'

    print('Identificacion: ', eventos[0], '\n Nombre del evento: ', eventos[1], '\nNombre modificado: ', nombre, '\n Pais: ', eventos[2], '\n Pais modificado: ', pais, '\n Lugar: ', eventos[3], '\n Lugar modificado: ', lugar, '\n Fecha inicial: ', eventos[4], '\n Fecha inicial modificada: ', fecha_inicial, '\n Fecha final: ', eventos[5], '\n Fecha final modificada: ', fecha_final, '\n')

    opcion = input('\nSeleccion una opcion:\n A. Aceptar\n C. Cancelar\n ')
            
    if opcion == 'A':
        os.system('cls')
        print('EVENTO MODIFICADO')
        eventos[i] = [identificacion,nombre,pais,lugar,fecha_inicial,fecha_final]
        modificar_eventos()

    elif opcion == 'C':
        os.system('cls')
        print('EVENTO NO MODIFICADO')
        modificar_eventos()

    else:
        os.system('cls')
        print('OPCION INVALIDA')
        modificar_eventos()

# 4.4 Eliminar eventos

def eliminar_eventos():

    global eventos

    print('EVENTOS DE ATLETISMO \n \nELIMINAR EVENTOS \n')

    # solicitar identificacion del evento

    identificacion = int(input('Ingrese la identificacion del evento: '))

    verify = True

    # verificar que la identificacion exista

    identificacion = int(input('Ingrese la identificacion del evento: '))

    while verify:
        for i, elemento in enumerate(eventos):
            if identificacion == elemento[0]:
                verify = False
        if identificacion == 'C' or identificacion == 'c':
            os.system('cls')
            registrar_eventos()
        else:
            print('EVENTO NO ESTA REGISTRADO, NO SE PUEDE ELIMINAR')
            identificacion = int(input('Ingrese la identificacion del evento: '))

    # opcion aceptar 'A' o cancelar 'C'

    print('Identificacion: ', eventos[0], '\n Nombre del evento: ', eventos[1], '\n Pais: ', eventos[2], '\n Lugar: ', eventos[3], '\n Fecha inicial: ', eventos[4], '\n Fecha final: ', eventos[5], '\n')

    opcion = input('\nSeleccion una opcion:\n A. Aceptar\n C. Cancelar\n ')

    # To do: verificar que el evento no tenga marcas registradas
            
    if opcion == 'A':
        os.system('cls')
        print('EVENTO ELIMINADO')
        eventos.pop(i)
        eliminar_eventos()

    elif opcion == 'C':
        os.system('cls')
        print('EVENTO NO ELIMINADO')
        eliminar_eventos()

    else:
        os.system('cls')
        print('OPCION INVALIDA')
        eliminar_eventos()

# 5 Registrar marcas

def registrar_marcas():
    
    print('EVENTOS DE ATLETISMO \n \nREGISTRAR MARCAS \n')
    
    print('Seleccion una opcion:\n 1. Agregar marcas\n 2. Consultar marcas\n 3. Modificar marcas\n 4. Eliminar marcas\n 0. Salir\n ')

    try:
        opcion = int(input('Ingrese una opcion: '))
        os.system('cls')

        match opcion:
            case 1:
                agregar_marcas()
            case 2:
                consultar_marcas()
            case 3:
                modificar_marcas()
            case 4:
                eliminar_marcas()
            case 0:
                menu_principal()
            case _:
                print('Opcion no valida')
                registrar_marcas()
    
    except ValueError:
        os.system('cls')
        print('\nOpcion no valida\n')
        registrar_marcas()

# Primer elemento de la lista: identificacion del evento
# Segundo elemento de la lista: codigo de la prueba
# Los siguientes elementos de la lista: marcas de los atletas, cada marca es una tupla con los siguientes elementos: 
# identificacion del atleta, dorsal del atleta, marca del atleta

# 5.1 Agregar marcas

def agregar_marcas():

    global marcas_por_evento

    print('EVENTOS DE ATLETISMO \n \nAGREGAR MARCAS \n')

    # solicitar identificacion del evento

    identificacion_evento = int(input('Ingrese la identificacion del evento: '))

    verify = True

    # verificar que la identificacion exista

    while verify:
        for elemento in eventos:
            if identificacion_evento == elemento[0]:
                print(elemento[1])
                verify = False
        if identificacion_evento == 'C' or identificacion_evento == 'c':
            os.system('cls')
            registrar_marcas()
        else:
            print('EVENTO NO ESTA REGISTRADO, NO SE PUEDE AGREGAR MARCAS')
            identificacion_evento = int(input('Ingrese la identificacion del evento: '))

    # solicitar codigo de la prueba

    codigo = int(input('Ingrese el codigo de la prueba: '))

    verify = True

    # verificar que el codigo exista

    while verify:
        for elemento in pruebas:
            if codigo == elemento[0]:
                print(elemento[1])
                verify = False
        else:
            print('CODIGO NO ESTA REGISTRADO, NO SE PUEDE AGREGAR MARCAS')
            codigo = int(input('Ingrese el codigo de la prueba: '))

    # solicitar identificacion del atleta

    identificacion_atleta = input('Ingrese la identificacion del atleta: ')

    verify = True

    # verificar que la identificacion exista

    while verify:
        for elemento in atletas:
            if identificacion_atleta == elemento[0]:
                print(elemento[1])
                verify = False
        else:
            print('ATLETA NO ESTA REGISTRADO, NO SE PUEDE AGREGAR MARCAS')
            identificacion_atleta = input('Ingrese la identificacion del atleta: ')

    for elemento1 in marcas_por_evento:
        if identificacion_evento == elemento1[0] and codigo == elemento1[1]:
            for elemento2 in elemento1[2:]:
                if identificacion_atleta == elemento2[0]:
                    print('MARCA YA ESTA REGISTRADA, NO SE PUEDE AGREGAR')
                    agregar_marcas()

    # solicitar dorsal del atleta y verificar que este sea unico en el evento

    dorsal = int(input('Ingrese el dorsal del atleta: '))

    for elemento1 in marcas_por_evento:
        if identificacion_evento == elemento1[0] and codigo == elemento1[1]:
            for elemento2 in elemento1[2:]:
                if dorsal == elemento2[1]:
                    print('DORSAL FUE ASIGNADO AL ATLETA: ', elemento2[0])
                    agregar_marcas()

    # verificar el tipo de medicion de la prueba

    for elemento3 in pruebas:
        if codigo == elemento3[0]:
            for elemento4 in disciplinas:
                if elemento4[0] == elemento3[4]:
                    tipo_medicion = elemento4[1]

    # solicitar marca del atleta

    if tipo_medicion == 'T':
        marca = input('Ingrese la marca del atleta en formato "hhmmsscc": ')
    elif tipo_medicion == 'M':
        marca = float(input('Ingrese la marca del atleta en formato "mmmcc": '))

    # opcion aceptar 'A' o cancelar 'C'

    print('Identificacion del evento: ', identificacion_evento, '\n Codigo de la prueba: ', codigo, '\n Identificacion del atleta: ', identificacion_atleta, '\n Dorsal del atleta: ', dorsal, '\n Marca del atleta: ', marca, '\n')

    opcion = input('\nSeleccion una opcion:\n A. Aceptar\n C. Cancelar\n ')

    if opcion == 'A':
        
        indice = marcas_por_evento.index(identificacion_evento)

        os.system('cls')
        print('MARCA AGREGADA')
        marcas_por_evento[indice].append([codigo, (identificacion_atleta, dorsal, marca)])
        agregar_marcas()

    elif opcion == 'C':
        os.system('cls')
        print('MARCA NO AGREGADA')
        agregar_marcas()

    else:
        os.system('cls')
        print('OPCION INVALIDA')
        agregar_marcas()

# 5.2 Consultar marcas

def consultar_marcas():


    print('EVENTOS DE ATLETISMO \n \nCONSULTAR MARCAS \n')

    # solicitar identificacion del evento

    identificacion = int(input('Ingrese la identificacion del evento: '))

    verify = True

    # verificar que la identificacion exista

    while verify:

        for elemento in eventos:
            if identificacion == elemento[0]:
                verify = False
        else:
            print('EVENTO NO ESTA REGISTRADO, NO SE PUEDE CONSULTAR MARCAS')
            identificacion = int(input('Ingrese la identificacion del evento: '))

    # solicitar codigo de la prueba

    codigo = int(input('Ingrese el codigo de la prueba: '))

    verify = True

    # verificar que el codigo exista

    while verify:

        for elemento1 in elemento:
            if codigo == elemento1[0]:
                verify = False
        else:
            print('CODIGO NO ESTA REGISTRADO, NO SE PUEDE CONSULTAR MARCAS')
            codigo = int(input('Ingrese el codigo de la prueba: '))

    # solicitar identificacion del atleta

    identificacion_atleta = input('Ingrese la identificacion del atleta: ')

    verify = True

    # verificar que la identificacion exista

    while verify:

        for elemento2 in elemento1:
            if identificacion_atleta == elemento2[0]:
                verify = False
        else:
            print('ATLETA NO ESTA REGISTRADO, NO SE PUEDE CONSULTAR MARCAS')
            identificacion_atleta = input('Ingrese la identificacion del atleta: ')

    # Imprimir consulta

    os.system('cls')
    print('EVENTOS DE ATLETISMO \n \nCONSULTAR MARCAS \n')

    print('Identificacion del evento: ', identificacion, '\n Codigo de la prueba: ', codigo, '\n Identificacion del atleta: ', identificacion_atleta, '\n Dorsal del atleta: ', elemento2[1], '\n Marca del atleta: ', elemento2[2], '\n')

    # opcion aceptar 'A'

    opcion = input('\nSeleccion una opcion:\n A. Aceptar\n ')

    while opcion != 'A':
        os.system('cls')
        print('OPCION INVALIDA')
        opcion = input('\nSeleccion una opcion:\n A. Aceptar\n ')

# 5.3 Modificar marcas

def modificar_marcas():

    global marcas_por_evento

    print('EVENTOS DE ATLETISMO \n \nMODIFICAR MARCAS \n')

    # solicitar identificacion del evento

    identificacion = int(input('Ingrese la identificacion del evento: '))

    verify = True

    # verificar que la identificacion exista

    while verify:

        for elemento in marcas_por_evento:
            if identificacion == elemento[0]:
                verify = False
        else:
            print('EVENTO NO ESTA REGISTRADO, NO SE PUEDE MODIFICAR')
            identificacion = int(input('Ingrese la identificacion del evento: '))

    # solicitar codigo de la prueba

    codigo = int(input('Ingrese el codigo de la prueba: '))

    verify = True

    # verificar que el codigo exista

    while verify:

        for elemento1 in elemento:
            if codigo == elemento1[0]:
                verify = False
        else:
            print('CODIGO NO ESTA REGISTRADO, NO SE PUEDE MODIFICAR')
            codigo = int(input('Ingrese el codigo de la prueba: '))

    # solicitar identificacion del atleta

    identificacion_atleta = input('Ingrese la identificacion del atleta: ')

    verify = True

    # verificar que la identificacion exista

    while verify:

        for elemento2 in elemento1:
            if identificacion_atleta == elemento2[0]:
                verify = False
        else:
            print('ATLETA NO ESTA REGISTRADO, NO SE PUEDE MODIFICAR')
            identificacion_atleta = input('Ingrese la identificacion del atleta: ')

    # modificar datos

    # solicitar nuevo dorsal

    dorsal = input('Ingrese el nuevo dorsal para el atleta: ')

    #verificar que el dorsal no este asignado

    for elemento3 in elemento1:
        if dorsal == elemento3[1]:
            print('DORSAL YA ESTA ASIGNADO, NO SE PUEDE MODIFICAR')
            modificar_marcas()

    # verificar el tipo de medicion

    for elemento3 in elemento1:
        if identificacion_atleta == elemento3[0]:
            tipo_medicion = elemento3[3]

    # solicitar nueva marca

    if tipo_medicion == 'T':
        marca = input('Ingrese la nueva marca del atleta en formato "hhmmsscc": ')
    elif tipo_medicion == 'M':
        marca = float(input('Ingrese la nueva marca del atleta en formato "mmmcc": '))

    # Imprimir datos a modificar y datos nuevos

    os.system('cls')
    print('EVENTOS DE ATLETISMO \n \nMODIFICAR MARCAS \n')
    print('Identificacion del evento: ', identificacion, '\n Codigo de la prueba: ', codigo, '\n Identificacion del atleta: ', identificacion_atleta, '\n Dorsal del atleta: ', elemento3[1], '\n Dorsal modificado: ', dorsal, '\n Marca del atleta: ', elemento3[1], '\nMarca del atleta modificada: ', marca, '\n')   

    # opcion aceptar 'A' o cancelar 'C'

    opcion = input('\nSeleccion una opcion:\n A. Aceptar\n C. Cancelar\n ')

    if opcion == 'A':

        # modificar datos

        for elemento3 in elemento1:
            if identificacion_atleta == elemento3[0]:
                elemento3[1] = dorsal
                elemento3[2] = marca
    elif opcion == 'C':
        os.system('cls')
        modificar_marcas()
    else: 
        os.system('cls')
        print('OPCION INVALIDA')
        modificar_marcas()

# 5.4 Eliminar marcas

def eliminar_marcas():

    global marcas_por_evento

    print('EVENTOS DE ATLETISMO \n \nELIMINAR MARCAS \n')

    # solicitar identificacion del evento

    identificacion = int(input('Ingrese la identificacion del evento: '))

    verify = True

    # verificar que la identificacion exista

    while verify:

        for elemento in marcas_por_evento:
            if identificacion == elemento[0]:
                verify = False
        else:
            print('EVENTO NO ESTA REGISTRADO, NO SE PUEDE ELIMINAR')
            identificacion = int(input('Ingrese la identificacion del evento: '))

    # solicitar codigo de la prueba

    codigo = int(input('Ingrese el codigo de la prueba: '))

    verify = True

    # verificar que el codigo exista

    while verify:

        for elemento1 in elemento:
            if codigo == elemento1[0]:
                verify = False
        else:
            print('CODIGO NO ESTA REGISTRADO, NO SE PUEDE ELIMINAR')
            codigo = int(input('Ingrese el codigo de la prueba: '))

    # solicitar identificacion del atleta

    identificacion_atleta = input('Ingrese la identificacion del atleta: ')

    verify = True

    # verificar que la identificacion exista

    while verify:

        for elemento2 in elemento1:
            if identificacion_atleta == elemento2[0]:
                verify = False
        else:
            print('ATLETA NO ESTA REGISTRADO, NO SE PUEDE ELIMINAR')
            identificacion_atleta = input('Ingrese la identificacion del atleta: ')

    # Imprimir datos a eliminar

    os.system('cls')
    print('EVENTOS DE ATLETISMO \n \nELIMINAR MARCAS \n')
    print('Identificacion del evento: ', identificacion, '\n Codigo de la prueba: ', codigo, '\n Identificacion del atleta: ', identificacion_atleta, '\n Dorsal del atleta: ', elemento2[1], '\n Marca del atleta: ', elemento2[2], '\n')   

    # opcion aceptar 'A' o cancelar 'C'

    opcion = input('\nSeleccion una opcion:\n A. Aceptar\n C. Cancelar\n ')

    if opcion == 'A':

        # confirmacion de eliminacion

        confirmacion = input('Esta seguro que desea eliminar la marca del atleta? S/N: ')

        if confirmacion == 'S':

            # eliminar datos

            marcas_por_evento.remove(elemento2)

        elif confirmacion == 'N':
            os.system('cls')
            print('ELIMINACION CANCELADA')
            eliminar_marcas()

        else:
            os.system('cls')
            print('OPCION INVALIDA')
            eliminar_marcas()

    elif opcion == 'C':
        os.system('cls')
        eliminar_marcas()

    else:
        os.system('cls')
        eliminar_marcas() 

# 6 Analisis de datos

def analisis_datos():
    print('Analisis de datos')

# 7 Ayuda

def ayuda():
    print('Ayuda')

# 8 Acerca de

def acerca_de():
    print(' Nombre: Eventos de atletismo \n Version: 1.0 \n Autor: Ledvin Manuel Leiva Mata \n Fecha: 2022-04-17 \n')


#menu_principal()
