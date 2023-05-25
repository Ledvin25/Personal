import pickle

partidas = {
    'FÁCIL': # llave para las partidas de este nivel
    (
        ((2, 25, 1, 2, 4),
         (2, 44, 1, 3, 8),
         (2, 20, 1, 5, 3),
         (2, 10, 1, 6, 3),
         (2, 39, 1, 8, 8),
         (2, 16, 1, 9, 2),
         (1, 10, 2, 1, 2),
         (1, 10, 2, 4, 2),
         (1, 8, 2, 7, 2)),
        
        ((2, 12, 1, 3, 3),
         (2, 30, 1, 5, 6),
         (2, 17, 1, 7, 3),
         (2, 8, 1, 9, 2),
         (2, 24, 1, 11, 5),
         (2, 14, 1, 12, 3),
         (1, 9, 2, 2, 2),
         (1, 8, 2, 5, 2),
         (1, 6, 2, 8, 2)),
        
        ((2, 22, 1, 2, 5),
         (2, 16, 1, 4, 3),
         (2, 13, 1, 6, 2),
         (2, 29, 1, 8, 6),
         (2, 11, 1, 11, 3),
         (2, 18, 1, 12, 4),
         (1, 6, 2, 1, 2),
         (1, 11, 2, 3, 4),
         (1, 5, 2, 7, 2))
    ), # fin de la tupla de partidas de nivel FACIL
} # fin del diccionario de partidas


file = open("TEC/Taller/Proyectos/Proyecto 2/kakuro2023partidas.dat", "wb")

pickle.dump(partidas, file)

file.close()


