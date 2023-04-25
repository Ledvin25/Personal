# Ejercicio 4

def sopa_de_letras(lista, palabra):

    tupla = []

    wrong_list = []

    word_list = []

    verify = True

    horizontal = vertical = diagonal = diagonal_inversa = True

    while verify:
        # Crear lista de tuplas con las posiciones de las letras de la palabra
        for letra in palabra:
            for i, element in enumerate(lista):
                for j, element2 in enumerate(element):
                    if letra == element2 and (i, j) not in tupla and len(tupla) <= len(palabra) and letra not in word_list :
                        word_list.append(letra)
                        tupla.append((i, j))
                        break
                    elif letra == element2 and (i, j) not in tupla and len(tupla) <= len(palabra) and letra in word_list and palabra.count(letra) > word_list.count(letra) and palabra[(len(word_list))] == letra:
                        word_list.append(letra)
                        tupla.append((i, j))
                        break
                    else:
                        continue
        
        # verificar que las posiciones de las letras esten en alguno de los siguientes ordenes: horizontal, vertical, diagonal, en caso de que no, se agrega la primera letra de la palabra a una lista de posiciones erroneas
        
        # horizontal

        for i in range(len(tupla) - 1):
            if tupla[i][0] == tupla[i + 1][0]:
                continue
            else:
                horizontal = False
                break
        
        # vertical

        for i in range(len(tupla) - 1):
            if tupla[i][1] == tupla[i + 1][1]:
                continue
            else:
                vertical = False
                break

        # diagonal

        for i in range(len(tupla) - 1):
            if tupla[i][0] + 1 == tupla[i + 1][0] and tupla[i][1] + 1 == tupla[i + 1][1]:
                continue
            else:
                diagonal = False
                break

        # diagonal inversa

        for i in range(len(tupla) - 1):
            if tupla[i][0] - 1 == tupla[i + 1][0] and tupla[i][1] - 1 == tupla[i + 1][1]:
                continue
            else:
                diagonal_inversa = False
                break

        # verifi
        if horizontal or vertical or diagonal or diagonal_inversa:
            verify = False
        else:
            wrong_list.append(tupla[0])
            tupla = []
            word_list = []
            horizontal = vertical = diagonal = diagonal_inversa = True
                
    

sopa_de_letras([ 'DAMEMORIAO', 'RZPUZLEÁÚY', 'DCPFBJLYDR', 'MSOPAOBSLJ', 'EBZSÑOGEUJ', 'NMQAHRTKDC', 'TMPNARYWST', 'ESYAAIUPWJ', 'EPVSJUODTW', 'ZARBALAPÓO'],'MENTE' )