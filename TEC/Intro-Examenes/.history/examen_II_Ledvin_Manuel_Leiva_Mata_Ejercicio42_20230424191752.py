# Funcion sopa_de_letras, donde esta recibe una lista de listas y una palabra, y retorna una lista de tuplas con las posiciones de las letras de la palabra en la lista de listas
# Cada tupla debe ser la posicion de una letra de la palabra en la lista de listas donde la primera tupla es la posicion de la primera letra de la palabra en la lista de listas, la segunda tupla es la posicion de la segunda letra de la palabra en la lista de listas, y asi sucesivamente
# La palabra puede estar en la lista de listas en horizontal, vertical o diagonal, pero no en zigzag
# Si la palabra no esta en la lista de listas, la funcion retorna una lista vacia

def sopa_de_letras(lista, palabras):

    # Crear lista de tuplas con las posiciones de las letras de la palabra
    tupla = []
    letras = []

    horizontal = vertical = diagonal = diagonal_inversa = True

    verify0 = True

    while verify0:
        for letra in palabras:
            verify = True
            if verify:
                for i, element in enumerate(lista):
                    if verify:
                        for j, element2 in enumerate(element):
                            if letra == element2 and (i, j) not in tupla:
                                letras.append(letra)
                                tupla.append((i, j))
                                verify = False
                                break
                            elif letra == element2 and (i, j) not in tupla and palabras.count(letra) > letras.count(letra) and palabras[(len(letras))] == letra:
                                letras.append(letra)
                                tupla.append((i, j))
                                verify = False
                                break
                            else:
                                continue
                    else:
                        break
            else:
                break
            


        # verificar que las posiciones de las letras esten en alguno de los siguientes ordenes: horizontal, vertical, diagonal, en caso de que no, se agrega la primera letra de la palabra a una lista de posiciones erroneas

        # horizontal

        for i in range(len(tupla) - 1):
            if tupla[i][0] == tupla[i + 1][0]:
                continue
            else:
                horizontal = False
            
        # vertical

        for i in range(len(tupla) - 1):

            if tupla[i][1] == tupla[i + 1][1]:
                continue
            else:
                vertical = False
            
        # diagonal

        for i in range(len(tupla) - 1):

            if tupla[i][0] + 1 == tupla[i + 1][0] and tupla[i][1] + 1 == tupla[i + 1][1]:
                continue
            else:
                diagonal = False
            
        # diagonal inversa

        for i in range(len(tupla) - 1):
                if tupla[i][0] - 1 == tupla[i + 1][0] and tupla[i][1] - 1 == tupla[i + 1][1]:
                    continue
                else:
                    diagonal_inversa = False

    
        
    return tupla

# Test

sopa_de_letras([ 'DAMEMORIAO', 'RZPUZLEÁÚY', 'DCPFBJLYDR', 'MSOPAOBSLJ', 'EBZSÑOGEUJ','NMQAHRTKDC', 'TMPNARYWST', 'ESYAAIUPWJ', 'EPVSJUODTW', 'ZARBALAPÓO'],'MEMORIA' )
