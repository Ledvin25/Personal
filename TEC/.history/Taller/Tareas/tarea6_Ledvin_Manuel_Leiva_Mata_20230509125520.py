# Tarea 6 - Ledvin Manuel Leiva Mata

def lugares_de_votacion():
    # Diccionario
    
    lugares_de_votacion = { 
        1234567: ["José", "Cartago Escuela Buenaventura", 2000],
        3456712: ["Carmen", "Turrialba Colegio Central", 1700],
        3456715: ["Beto", "Turrialba Colegio Central", 1700],
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
            menu()

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
            menu()

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
            menu()

    def eliminar():

        # verificar si la cedula existe

        cedula = int(input("Ingrese el número de cédula: "))

        if not cedula in lugares_de_votacion:
            print("La cédula no existe")
            eliminar()
        else:
            del lugares_de_votacion[cedula]
            print("Cédula eliminada")
            menu()

    def informe():

        # Despliega todos los datos del diccionario clasificados por mesa de votación y dentro de cada mesa en orden alfabético.


        # Crear lista de mesas
        mesas = set([value[2] for value in lugares_de_votacion.values()])
        
        for mesa in sorted(mesas):
            print("{:<10} {:<10}".format("MESA " + str(mesa), " NOMBRE"))
            print("-"*9)
            for cedula, value in sorted(lugares_de_votacion.items(), reverse=True): # reverse=True para ordenar de alfabeticamente
                if value[2] == mesa:
                    print("{:<10} {:<10}".format(cedula, value[0]))
            print("\n"*2)
        menu()


    # Menu

    def menu():
        print("1. Agregar elementos\n2. Consultar elementos\n3. Actualizar elementos\n4. Eliminar elementos\n5. Informe de electores\n0. Salir")
        opcion = int(input("Ingrese una opcion: "))

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

    menu()


# Ejercicio 2

def compactar(lista):

    diccionario = {}

    for numero in lista:
        if numero not in diccionario:
            for i, numero2 in enumerate(lista):
                if numero2 not in diccionario: # si el numero no esta en el diccionario se agrega el numero como key con su indice
                    if numero == numero2:
                        diccionario[numero] = (i,)
                else: # si el numero ya esta en el diccionario se agrega solo el indice
                    if numero == numero2:
                        diccionario[numero] += (i,)

    return diccionario
                    

# Ejercicio 3

def seleccionar_proveedores(proveedores, proyectos):

    proyecto_final = {}

    for proveedor, precio_proveedor in enumerate(proveedores):
        for proyecto in proyectos:
            i = 0
            suma final
            while True:
                suma = precio_proveedor[i] * proyecto[i]

                if suma <
        


seleccionar_proveedores([[8, 13, 6, 6], [6, 12, 7, 8], [7, 14, 6, 7]],
[[24, 5, 12, 18], [20, 7, 15, 20], [20, 4, 15, 15]])