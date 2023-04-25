# Ejercicio 4

def sopa_de_letras(lista, palabra):

    tupla = ()

    for letra in palabra:
        for i, element in enumerate(lista):
            for j, element2 in enumerate(element):
                if letra == element2:
                    # horizontal

                    if len(tupla) > 0 and i == tupla[0]
                    tupla += (i,j),
                    break
                else:
                    continue
            break

sopa_de_letras([ 'DAMEMORIAO', 'RZPUZLEÁÚY', 'DCPFBJLYDR', 'MSOPAOBSLJ', 'EBZSÑOGEUJ', 'NMQAHRTKDC', 'TMPNARYWST', 'ESYAAIUPWJ', 'EPVSJUODTW', 'ZARBALAPÓO'],'MENTE' )