# Ejercicio 4

def sopa_de_letras(lista, palabra):

    for i, element in enumerate(lista):
        for j, element2 in enumerate(element):
            for palabra in element2:

sopa_de_letras([ 'DAMEMORIAO', 'RZPUZLEÁÚY', 'DCPFBJLYDR', 'MSOPAOBSLJ', 'EBZSÑOGEUJ', 'NMQAHRTKDC', 'TMPNARYWST', 'ESYAAIUPWJ', 'EPVSJUODTW', 'ZARBALAPÓO'],'MENTE' )