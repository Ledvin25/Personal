# Ledvin Manuel Leiva Mata
# 2023071280
# Quiz3
def indice_palabras(tupla):
 
    #variables

    lista_prefinal = []
    palabras = []
    palabras_encontradas = []


    # separar palabras por espacio
    for palabra in tupla:
        palabras.append(palabra.split(" "))

    for i,palabra in enumerate(palabras):
        for palabra2 in palabra:
            if palabra2 not in palabras_encontradas:
                lista_prefinal.append([palabra2, i+1])
            elif palabra2 in palabras_encontradas:
                for palabra3 in lista_prefinal:
                    if palabra3[0] == palabra2:
                        palabra3.append(i+1)
                        break
            palabras_encontradas.append(palabra2)
            


indice_palabras( ("en el aprendizaje de", "la programación de computadoras", "hay que practicar el desarrollo de", "algoritmos hay que practicar mucho") )