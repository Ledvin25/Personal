#Quiz 6 - Ledvin Manuel Leiva Mata

# Cuadro magico

def cuadrado_magico(lista):

    sumaTotal = 0

    # Suma inicial

    for i in lista:
        for j in i:
            sumaTotal += j
        break

    return sumaTotal


print(cuadrado_magico( [ [8, 1, 6], [3, 5, 7], [4, 9, 2] ] ))