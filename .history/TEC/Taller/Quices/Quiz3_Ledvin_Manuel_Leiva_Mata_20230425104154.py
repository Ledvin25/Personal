# Ledvin Manuel Leiva Mata
# 2023071280
# Quiz3
def indice_palabras(tupla):
 
    #variables

    lista_final = []
    palabras = []
    palabras_encontradas = []

    lista_final = []


    # separar palabras por espacio
    for palabra in tupla:
        palabras.append(palabra.split(" "))

    # buscar palabras en lista de palabras

    for i,palabra in enumerate(palabras): # i = indice, palabra = lista de palabras
        for palabra2 in palabra:
            if palabra2 not in palabras_encontradas: # si la palabra no esta en la lista de palabras encontradas
                lista_final.append([palabra2, i+1])
            elif palabra2 in palabras_encontradas: # si la palabra esta en la lista de palabras encontradas
                for palabra3 in lista_final:
                    if palabra3[0] == palabra2: # si la palabra esta en la lista de palabras encontradas
                        palabra3.append(i+1) # agregar el indice de la palabra
                        break
            palabras_encontradas.append(palabra2)

    
    # orderar lista por orden alfabetico
    lista_final.sort()

    return lista_final # lista de listas




# test

