import pickle

partidas = {
    'FÁCIL': (
        (
            (2, 11, 0, 0, 4),
            (2, 17, 0, 5, 3),
            (2, 3, 1, 0, 2),
            (2, 14, 1, 3, 3),
            (2, 4, 2, 0, 2),
            (1, 9, 2, 2, 3),
            (2, 7, 2, 6, 2),
            (2, 22, 3, 0, 5),
            (1, 6, 3, 5, 3),
            (2, 5, 4, 0, 2),
            (2, 15, 4, 2, 4),
         ),
        (
            (2, 11, 0, 1, 4),
            (2, 14, 0, 5, 3),
            (1, 6, 1, 0, 2),
            (1, 13, 1, 3, 4),
            (2, 4, 2, 2, 2),
            (1, 7, 2, 3, 3),
            (1, 9, 3, 0, 2),
            (1, 16, 3, 3, 4),
            (1, 15, 4, 3, 4),
            (2, 9, 2, 8, 2),
        ),
        (
            (1, 8, 1, 0, 2),
            (1, 12, 1, 4, 3),
            (2, 5, 2, 2, 2),
            (2, 13, 2, 5, 3),
            (1, 7, 3, 1, 2),
            (1, 15, 3, 4, 4),
            (1, 14, 4, 3, 3),
            (2, 8, 3, 7, 2),
            (2, 17, 0, 5, 3),
        ),
    ),
    'MEDIO': (
        (
            (2, 15, 0, 2, 4),
            (2, 18, 0, 7, 4),
            (1, 9, 1, 0, 2),
            (2, 17, 1, 3, 4),
            (1, 5, 2, 1, 2),
            (2, 16, 1, 4, 4),
            (1, 6, 3, 1, 2),
            (1, 7, 3, 4, 3),
            (2, 12, 3, 7, 3),
            (1, 19, 2, 0, 5),
            (2, 11, 1, 5, 3),
            (1, 11, 4, 1, 3),
            (1, 9, 4, 4, 2),
            (2, 10, 4, 7, 3),
        ),
        (
            (2, 14, 0, 2, 4),
            (2, 16, 0, 7, 4),
            (1, 8, 1, 0, 2),
            (2, 17, 1, 3, 4),
            (1, 6, 2, 1, 2),
            (2, 12, 1, 4, 3),
            (1, 7, 3, 1, 2),
            (1, 9, 3, 4, 3),
            (2, 13, 3, 7, 3),
            (1, 19, 2, 0, 5),
            (2, 11, 1, 5, 3),
            (1, 5, 4, 1, 2),
            (1, 10, 4, 3, 3),
            (2, 15, 4, 6, 3),
        ),
        (
            (2, 15, 0, 2, 4),
            (2, 17, 0, 7, 4),
            (1, 9, 1, 0, 2),
            (2, 14, 1, 3, 4),
            (1, 5, 2, 1, 2),
            (2, 11, 1, 4, 3),
            (1, 7, 3, 1, 2),
            (1, 8, 3, 4, 3),
            (2, 13, 3, 7, 3),
            (1, 19, 2, 0, 5),
            (2, 12, 1, 5, 3),
            (1, 6, 4, 1, 2),
            (1, 10, 4, 3, 3),
            (2, 16, 4, 6, 3),
        ),
    ),
    'DIFÍCIL': (
        (
            (2, 30, 0, 2, 5),
            (2, 25, 0, 8, 5),
            (1, 12, 1, 1, 3),
            (1, 16, 1, 6, 4),
            (2, 20, 2, 0, 5),
            (2, 24, 2, 7, 4),
            (1, 10, 3, 2, 3),
            (2, 23, 3, 6, 5),
            (2, 26, 4, 1, 5),
            (1, 13, 4, 7, 3),
            (1, 8, 5, 3, 3),
            (2, 19, 5, 7, 4),
            (1, 11, 6, 2, 3),
            (2, 21, 6, 6, 4),
            (2, 28, 7, 0, 5),
            (1, 9, 7, 5, 2),
            (1, 7, 8, 4, 2),
            (2, 14, 8, 7, 3),
            (1, 12, 9, 3, 3),
            (1, 7, 9, 8, 2),
        ),
        (
            (2, 27, 0, 1, 5),
            (2, 32, 0, 7, 5),
            (1, 15, 1, 0, 4),
            (2, 30, 1, 6, 5),
            (1, 9, 2, 1, 2),
            (2, 26, 2, 7, 4),
            (1, 12, 3, 2, 3),
            (2, 23, 3, 6, 5),
            (2, 28, 4, 1, 5),
            (1, 14, 4, 8, 4),
            (1, 10, 5, 3, 3),
            (2, 19, 5, 7, 4),
            (2, 34, 6, 0, 6),
            (1, 11, 6, 7, 3),
            (2, 22, 7, 2, 4),
            (1, 8, 7, 7, 2),
            (1, 13, 8, 4, 3),
            (2, 20, 8, 8, 4),
            (1, 16, 9, 1, 4),
            (2, 33, 9, 7, 6),
        ),
        (
            (2, 15, 0, 0, 3),
            (1, 12, 0, 3, 2),
            (2, 7, 1, 0, 3),
            (1, 8, 1, 4, 2),
            (2, 9, 2, 1, 3),
            (1, 7, 2, 4, 2),
        ),
    ),
    'EXPERTO': (
        (
            (2, 30, 0, 0, 5),
            (2, 14, 0, 6, 3),
            (1, 18, 1, 1, 3),
            (1, 13, 1, 5, 2),
            (2, 7, 2, 0, 2),
            (2, 16, 2, 3, 4),
        ),
        (
            (2, 26, 0, 0, 5),
            (2, 13, 0, 6, 3),
            (1, 16, 1, 1, 3),
            (1, 10, 1, 5, 2),
            (2, 7, 2, 0, 2),
            (2, 19, 2, 3, 4),
        ),
        (
            (2, 28, 0, 0, 5),
            (2, 12, 0, 6, 3),
            (1, 17, 1, 1, 3),
            (1, 11, 1, 5, 2),
            (2, 7, 2, 0, 2),
            (2, 18, 2, 3, 4),
        ),
    ),
}


file = open("TEC/Taller/Proyectos/Proyecto 2/kakuro2023partidas.dat", "wb")

pickle.dump(partidas, file)

file.close()

