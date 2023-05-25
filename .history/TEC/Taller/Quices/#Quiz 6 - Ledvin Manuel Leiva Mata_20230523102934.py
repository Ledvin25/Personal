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
        sumaFila = 0
        for j in i:
            sumaFila += j
            if i == j:
                diagonal1 += j
            if len(lista) - i == len(lista[0]) - j:
                diagonal2 += j
                
        if sumaFila != sumaTotal:
            return False
        

    return True


print(cuadrado_magico( [ [8, 1, 6], [3, 5, 7], [4, 9, 2] ] ))