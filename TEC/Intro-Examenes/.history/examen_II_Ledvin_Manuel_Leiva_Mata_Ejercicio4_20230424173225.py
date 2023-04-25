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
        
        # verificar que las posiciones de las letras esten en alguno de los siguientes ordenes: 
        for element in tupla:
            if element not in wrong_list:
                wrong_list.append(element)
                
    

sopa_de_letras([ 'DAMEMORIAO', 'RZPUZLEÁÚY', 'DCPFBJLYDR', 'MSOPAOBSLJ', 'EBZSÑOGEUJ', 'NMQAHRTKDC', 'TMPNARYWST', 'ESYAAIUPWJ', 'EPVSJUODTW', 'ZARBALAPÓO'],'MENTE' )