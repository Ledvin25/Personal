# Ejercicio 4

def sopa_de_letras(lista, palabra):

    tupla = ()
    
    for i, element in enumerate(lista):
        for j, element2 in enumerate(element):
            for letra in palabra:
                if letra == element2:
                    print(f'La letra {letra} se encuentra en la posición {i},{j}')
                    break
                else:
                    continue

sopa_de_letras([ 'DAMEMORIAO', 'RZPUZLEÁÚY', 'DCPFBJLYDR', 'MSOPAOBSLJ', 'EBZSÑOGEUJ', 'NMQAHRTKDC', 'TMPNARYWST', 'ESYAAIUPWJ', 'EPVSJUODTW', 'ZARBALAPÓO'],'MENTE' )