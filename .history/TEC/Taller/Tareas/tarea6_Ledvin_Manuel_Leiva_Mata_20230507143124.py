# Tarea 6 - Ledvin Manuel Leiva Mata

def lugares_de_votacion():
    { 
        1234567: ["José", "Cartago Escuela Buenaventura", 2000],
        3456712: ["Carmen", "Turrialba Colegio Central", 1700],
        1234444: ["Alberto", "Cartago Colegio SLG", 3002],
        1111111: ["Olga", "Cartago Colegio SLG", 3002],
        1234555: ["Emilia", "Cartago Colegio SLG", 3010],
        5555555: ["Ana", "Turrialba Colegio Central", 1700],
        1234565: ["Ali", "Cartago Colegio SLG", 3002] 
        }

    # Menu

    opcion = int(input("Ingrese el número de cédula: "))

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

