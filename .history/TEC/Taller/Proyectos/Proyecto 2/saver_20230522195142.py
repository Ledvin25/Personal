import pickle

partidas = {
    'FÁCIL': (
        (
            (2, 25, 1, 2, 4),
            (2, 44, 1, 3, 8),
            (2, 20, 1, 5, 3),
            (2, 10, 1, 6, 3),
            (2, 39, 1, 8, 8),
            (2, 16, 1, 9, 2),
            (1, 10, 2, 1, 2),
            (1, 10, 2, 4, 2),
            (1, 8, 2, 7, 2),
        ),
        (
            (1, 18, 1, 0, 5),
            (2, 17, 2, 1, 3),
            (2, 6, 1, 3, 2),
            (2, 21, 3, 4, 5),
            (2, 11, 5, 6, 4),
            (2, 16, 7, 7, 4),
            (2, 10, 8, 8, 2),
            (1, 10, 6, 0, 2),
            (1, 8, 7, 0, 2),
        ),
        (
            (2, 25, 1, 0, 4),
            (2, 11, 3, 2, 3),
            (2, 28, 4, 3, 7),
            (2, 6, 6, 5, 2),
            (2, 11, 7, 6, 4),
            (1, 10, 8, 1, 2),
            (1, 7, 8, 3, 2),
            (1, 6, 8, 6, 2),
            (1, 6, 5, 0, 2),
        ),
    ),
    'MEDIO': (
        (
            (2, 32, 0, 0, 6),
            (2, 9, 0, 2, 2),
            (2, 19, 0, 4, 4),
            (2, 21, 0, 6, 5),
            (2, 11, 0, 8, 4),
            (1, 8, 0, 1, 2),
            (1, 8, 0, 7, 2),
            (1, 9, 0, 3, 2),
            (1, 5, 0, 5, 2),
        ),
        (
            (2, 23, 1, 0, 5),
            (2, 17, 1, 2, 3),
            (2, 10, 1, 4, 2),
            (2, 29, 1, 7, 6),
            (2, 17, 1, 8, 3),
            (1, 7, 0, 1, 2),
            (1, 9, 0, 6, 2),
            (1, 6, 0, 4, 2),
            (1, 4, 0, 7, 2),
        ),
        (
            (2, 21, 0, 0, 5),
            (2, 19, 0, 2, 4),
            (2, 12, 0, 4, 3),
            (2, 11, 0, 6, 3),
            (2, 9, 0, 8, 2),
            (1, 6, 0, 1, 2),
            (1, 5, 0, 3, 2),
            (1, 6, 0, 7, 2),
            (1, 4, 0, 5, 2),
        ),
    ),
    'DIFÍCIL': (
        (
            (2, 34, 0, 0, 6),
            (2, 15, 0, 2, 3),
            (2, 10, 0, 4, 2),
            (2, 28, 0, 7, 6),
            (2, 13, 0, 8, 3),
            (1, 9, 0, 1, 2),
            (1, 7, 0, 3, 2),
            (1, 9, 0, 6, 2),
            (1, 6, 0, 5, 2),
        ),
        (
            (2, 32, 0, 0, 6),
            (2, 14, 0, 2, 3),
            (2, 11, 0, 4, 2),
            (2, 30, 0, 7, 6),
            (2, 12, 0, 8, 3),
            (1, 9, 0, 1, 2),
            (1, 8, 0, 3, 2),
            (1, 6, 0, 5, 2),
            (1, 4, 0, 6, 2),
        ),
        (
            (2, 31, 0, 0, 6),
            (2, 16, 0, 2, 4),
            (2, 10, 0, 4, 2),
            (2, 29, 0, 7, 6),
            (2, 14, 0, 8, 3),
            (1, 7, 0, 1, 2),
            (1, 9, 0, 6, 2),
            (1, 6, 0, 3, 2),
            (1, 4, 0, 5, 2),
        ),
    ),
    'EXPERTO': (
        (
            (2, 33, 0, 0, 6),
            (2, 14, 0, 2, 3),
            (2, 11, 0, 4, 2),
            (2, 28, 0, 7, 6),
            (2, 13, 0, 8, 3),
            (1, 9, 0, 1, 2),
            (1, 7, 0, 3, 2),
            (1, 9, 0, 6, 2),
            (1, 6, 0, 5, 2),
        ),
        (
            (2, 32, 0, 0, 6),
            (2, 14, 0, 2, 3),
            (2, 11, 0, 4, 2),
            (2, 29, 0, 7, 6),
            (2, 13, 0, 8, 3),
            (1, 9, 0, 1, 2),
            (1, 8, 0, 3, 2),
            (1, 6, 0, 5, 2),
            (1, 4, 0, 6, 2),
        ),
        (
            (2, 32, 0, 0, 6),
            (2, 15, 0, 2, 3),
            (2, 10, 0, 4, 2),
            (2, 29, 0, 7, 6),
            (2, 14, 0, 8, 3),
            (1, 8, 0, 1, 2),
            (1, 9, 0, 6, 2),
            (1, 6, 0, 3, 2),
            (1, 4, 0, 5, 2),
        ),
    ),
}


file = open("TEC/Taller/Proyectos/Proyecto 2/kakuro2023partidas.dat", "wb")

pickle.dump(partidas, file)

file.close()


