# Ejercicio 4

def sopa_de_letras(lista, palabra):

    tupla = []

    wrong_list = []

    verify = True

    while verify:
        # Crear lista de tuplas con las posiciones de las letras de la palabra
        for letra in palabra:
            for i, element in enumerate(lista):
                for j, element2 in enumerate(element):
                    if letra == element2:
                        tupla.append((i, j))
                        break
                    else:
                        continue
                break
        
        # verificar que las posiciones de las letras esten en alguno de los siguientes ordenes: horizontal, vertical, diagonal, en caso de que no, se agrega la primera letra de la palabra a una lista de posiciones erroneas
        
        for element in tupla
                
    

sopa_de_letras([ 'DAMEMORIAO', 'RZPUZLEÁÚY', 'DCPFBJLYDR', 'MSOPAOBSLJ', 'EBZSÑOGEUJ', 'NMQAHRTKDC', 'TMPNARYWST', 'ESYAAIUPWJ', 'EPVSJUODTW', 'ZARBALAPÓO'],'MENTE' )