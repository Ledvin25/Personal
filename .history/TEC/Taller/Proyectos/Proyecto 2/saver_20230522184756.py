import pickle

partidas = {
    'FÁCIL': # llave para las partidas de este nivel
    ( # tupla con las partidas del nivel
        ( # tupla con la partida 1 de este nivel
        ( 2, 25, 1, 2, 4 ),
        ( 2, 44, 1, 3, 8 ),
        ( 2, 20, 1, 5, 3 ),
        ( 2, 10, 1, 6, 3 ),
        ( 2, 39, 1, 8, 8 ),
        ( 2, 16, 1, 9, 2),
        ( 1, 10, 2, 1, 2 ),
        ( 1, 10, 2, 4, 2),
        ( 1, 8, 2, 7, 2),
        ), # fin de la tupla con la partida 1 de este nivel
    ), # fin de la tupla de partidas de nivel FACIL
} # fin del diccionario de partidas


file = open("TEC/Taller/Proyectos/Proyecto 2/kakuro2023partidas.dat", "wb")

pickle.dump(lista, file)

file.close()

