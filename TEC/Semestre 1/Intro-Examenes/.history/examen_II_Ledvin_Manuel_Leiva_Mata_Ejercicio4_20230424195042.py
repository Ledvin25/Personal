# Ejercicio 4
# Ledvin Manuel Leiva Mata
# 2023071280

def sopa_de_letras(lista, word):

    # inicializar variables

    filas = len(lista) # numero de filas
    columnas = len(lista[0]) # numero de columnas
    tupla = [] # lista de tuplas de pre_tuple

    for i in range(filas): # recorrer filas
        for j in range(columnas): # recorrer columnas
            if lista[i][j] == word[0]: # si la letra es igual a la primera letra de la palabra
                for diagonal_i in range(-1, 2): # recorrer diagonales
                    for diagonal_j in range(-1, 2): # recorrer diagonales
                        if diagonal_i != 0 or diagonal_j != 0: 
                            verify = True # verificar si la palabra esta en la sopa de letras
                            pre_tuple = [(i, j)] # lista de posiciones
                            for k in range(1, len(word)): 
                                fila = i + k * diagonal_i
                                columna = j + k * diagonal_j
                                if fila < 0 or fila >= filas or columna < 0 or columna >= columnas or lista[fila][columna] != word[k]:
                                    verify = False
                                    break
                                pre_tuple.append((fila, columna))
                            if verify:
                                tupla.append(tuple(pre_tuple))
    return tupla
    

sopa_de_letras([ 'DAMEMORIAO', 'RZPUZLEÁÚY', 'DCPFBJLYDR', 'MSOPAOBSLJ', 'EBZSÑOGEUJ', 'NMQAHRTKDC', 'TMPNARYWST', 'ESYAAIUPWJ', 'EPVSJUODTW', 'ZARBALAPÓO'],'MEMORIA' )