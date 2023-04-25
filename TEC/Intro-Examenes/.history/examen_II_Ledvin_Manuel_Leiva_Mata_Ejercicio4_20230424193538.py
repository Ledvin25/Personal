# Ejercicio 4
# Ledvin Manuel Leiva Mata
# 2023071280

def sopa_de_letras(lista, palabra):

    # inicializar variables
    filas = len(lista) 
    columnas = len(lista[0])
    tupla = []

    for i in range(filas):
        for j in range(columnas):
            if lista[i][j] == palabra[0]:
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if di != 0 or dj != 0:
                            encontrada = True
                            posiciones = [(i, j)]
                            for k in range(1, len(palabra)):
                                fila = i + k * di
                                columna = j + k * dj
                                if fila < 0 or fila >= filas or columna < 0 or columna >= columnas or lista[fila][columna] != palabra[k]:
                                    encontrada = False
                                    break
                                posiciones.append((fila, columna))
                            if encontrada:
                                tupla.append(tuple(posiciones))
    return encontradas
    

sopa_de_letras([ 'DAMEMORIAO', 'RZPUZLEÁÚY', 'DCPFBJLYDR', 'MSOPAOBSLJ', 'EBZSÑOGEUJ', 'NMQAHRTKDC', 'TMPNARYWST', 'ESYAAIUPWJ', 'EPVSJUODTW', 'ZARBALAPÓO'],'MEMORIA' )