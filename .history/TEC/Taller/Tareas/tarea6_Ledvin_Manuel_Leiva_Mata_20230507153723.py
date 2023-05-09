# Tarea 6 - Ledvin Manuel Leiva Mata

def lugares_de_votacion():
    # Diccionario
    { 
        1234567: ["José", "Cartago Escuela Buenaventura", 2000],
        3456712: ["Carmen", "Turrialba Colegio Central", 1700],
        1234444: ["Alberto", "Cartago Colegio SLG", 3002],
        1111111: ["Olga", "Cartago Colegio SLG", 3002],
        1234555: ["Emilia", "Cartago Colegio SLG", 3010],
        5555555: ["Ana", "Turrialba Colegio Central", 1700],
        1234565: ["Ali", "Cartago Colegio SLG", 3002] 
        }
    # Funciones

    def agregar():

        cedula = int(input("Ingrese el número de cédula: "))

        # verificar si la cedula ya existe

        if cedula in lugares_de_votacion:
            print("La cédula ya existe")
            agregar()
        else:
            nombre = input("Ingrese el nombre: ")
            lugar = input("Ingrese el lugar de votación: ")
            mesa = int(input("Ingrese el número de mesa: "))
            lugares_de_votacion[cedula] = [nombre, lugar, mesa]
            print("Cédula agregada")
            agregar()

    def consultar():
        
        cedula = int(input("Ingrese el número de cédula: "))

        # verificar si la cedula existe

        if not cedula in lugares_de_votacion:
            print("La cédula no existe")
            consultar()
        else:
            nombre = lugares_de_votacion[cedula][0]
            lugar = lugares_de_votacion[cedula][1]
            mesa = lugares_de_votacion[cedula][2]
            print(f"Nombre: {nombre}\nLugar: {lugar}\nMesa: {mesa}")
            input("Presione enter para continuar")
            consultar()

    def actualizar():
        
        # verificar si la cedula existe

        cedula = int(input("Ingrese el número de cédula: "))

        if not cedula in lugares_de_votacion:
            print("La cédula no existe")
            actualizar()
        else:
            nombre = input("Ingrese el nuevo nombre: ")
            lugar = input("Ingrese el nuevo lugar de votación: ")
            mesa = int(input("Ingrese el nuevo número de mesa: "))
            lugares_de_votacion[cedula] = [nombre, lugar, mesa]
            print("Cédula actualizada")
            actualizar()

    def eliminar():

        # verificar si la cedula existe

        cedula = int(input("Ingrese el número de cédula: "))

        if not cedula in lugares_de_votacion:
            print("La cédula no existe")
            eliminar()
        else:
            del lugares_de_votacion[cedula]
            print("Cédula eliminada")
            eliminar()

    def informe():

        # Despliega todos los datos del diccionario clasificados por mesa de votación y dentro de cada mesa en orden alfabético.

        for mesa in sorted(lugares_de_votacion.values()):
            print(mesa)

    # Menu

    opcion = 5#int(input("Ingrese una opcion: "))

    match opcion:
        case 1:
            agregar()
        case 2:
            consultar()
        case 3:
            actualizar()
        case 4:
            eliminar()    
        case 5:
            informe()
        case 0:
            print("Adios")


lugares_de_votacion()