# Ejercicio 4

def sopa_de_letras(lista, palabra):

    tupla = []

    wrong_list = []

    verify = True

    while verify:

        for letra in palabra:
            for i, element in enumerate(lista):
                for j, element2 in enumerate(element):
                    if letra == element2:
                        tupla.append((i, j))
                        break
                    else:
                        continue
                break
        for 
                
    

sopa_de_letras([ 'DAMEMORIAO', 'RZPUZLEÁÚY', 'DCPFBJLYDR', 'MSOPAOBSLJ', 'EBZSÑOGEUJ', 'NMQAHRTKDC', 'TMPNARYWST', 'ESYAAIUPWJ', 'EPVSJUODTW', 'ZARBALAPÓO'],'MENTE' )