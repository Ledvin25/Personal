# Ledvin Manuel Leiva Mata
# 2023071280
# Quiz3
def indice_palabras(tupla):
 
    #variables

    lista_final = []
    palabras = []
    palabras_encontradas = []


    # separar palabras por espacio
    for palabra in tupla:
        palabras.append(palabra.split(" "))

    for palabra in palabras:
        if palabra not in palabras_encontradas:
            palabras_encontradas.append(palabra)
            for i in range(len(palabras)):
                if palabra == palabras[i]:
                    lista_final.append(pala)
            


indice_palabras( ("en el aprendizaje de", "la programación de computadoras", "hay que practicar el desarrollo de", "algoritmos hay que practicar mucho") )