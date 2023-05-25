#Quiz 6 - Ledvin Manuel Leiva Mata

# Cuadro magico

def cuadrado_magico(lista):

    

    # Suma inicial
    sumaTotal = 0
    for i in lista:
        for j in i:
            sumaTotal += j
        break


    diagonal1 = diagonal2 = 0
    for i in lista:
        suma = 0
        for j in i:
            suma += j
            if i == j
        if suma != sumaTotal:
            return False
        

    return True


print(cuadrado_magico( [ [8, 1, 6], [3, 5, 7], [4, 9, 2] ] ))