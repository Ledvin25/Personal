#Quiz 6 - Ledvin Manuel Leiva Mata

# Cuadro magico

def cuadrado_magico(lista):

    

    # Suma inicial
    sumaTotal = 0
    for i in lista:
        for j in i:
            sumaTotal += j
        break

    for i in lista:
        suma = 0
        for j in i:
            suma += j
        if suma != sumaTotal:
            return False
        if 

    return True


print(cuadrado_magico( [ [8, 1, 6], [3, 5, 7], [4, 9, 2] ] ))