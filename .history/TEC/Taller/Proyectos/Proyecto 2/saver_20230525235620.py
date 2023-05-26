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
            (2, 36, 0, 2, 6),
            (2, 31, 0, 9, 5),
            (1, 10, 1, 0, 3),
            (1, 14, 1, 5, 4),
            (2, 23, 2, 1, 5),
            (2, 27, 2, 7, 5),
            (1, 12, 3, 3, 3),
            (2, 21, 3, 8, 4),
            (1, 9, 4, 2, 2),
            (2, 25, 4, 7, 5),
            (1, 8, 5, 3, 2),
            (1, 11, 5, 8, 3),
            (2, 17, 6, 2, 4),
            (1, 7, 6, 7, 2),
            (2, 34, 7, 0, 6),
            (2, 19, 7, 6, 4),
            (1, 16, 8, 1, 4),
            (2, 29, 8, 7, 5),
            (1, 15, 9, 2, 4),
            (1, 9, 9, 8, 2),
        ),
    ),
    'EXPERTO': (
        (
            (2, 40, 0, 1, 7),
            (2, 45, 0, 9, 7),
            (2, 26, 1, 0, 4),
            (1, 11, 1, 6, 3),
            (1, 10, 2, 1, 2),
            (2, 35, 2, 7, 6),
            (1, 18, 3, 0, 5),
            (2, 34, 3, 7, 6),
            (2, 32, 4, 2, 6),
            (1, 13, 4, 9, 3),
            (1, 9, 5, 1, 2),
            (2, 38, 5, 7, 7),
            (2, 37, 6, 0, 7),
            (1, 15, 6, 8, 3),
            (2, 42, 7, 3, 7),
            (1, 7, 7, 10, 2),
            (1, 14, 8, 2, 3),
            (2, 44, 8, 8, 7),
            (2, 41, 9, 1, 7),
            (1, 12, 9, 9, 4),
        ),
        (
            (2, 47, 0, 2, 7),
            (2, 42, 0, 9, 7),
            (2, 30, 1, 0, 5),
            (1, 14, 1, 6, 3),
            (1, 9, 2, 1, 2),
            (2, 39, 2, 7, 7),
            (1, 20, 3, 0, 6),
            (2, 43, 3, 7, 7),
            (2, 37, 4, 2, 6),
            (1, 12, 4, 9, 4),
            (1, 10, 5, 1, 2),
            (2, 46, 5, 8, 7),
            (2, 36, 6, 0, 6),
            (1, 17, 6, 7, 4),
            (2, 40, 7, 3, 7),
            (1, 8, 7, 10, 2),
            (1, 16, 8, 2, 4),
            (2, 44, 8, 8, 7),
            (2, 45, 9, 1, 7),
            (1, 13, 9, 9, 3),
        ),
        (
            (2, 50, 0, 3, 8),
            (2, 33, 1, 0, 6),
            (1, 15, 1, 7, 4),
            (1, 12, 2, 1, 3),
            (2, 45, 2, 8, 8),
            (1, 21, 3, 0, 7),
            (2, 48, 3, 8, 8),
            (2, 39, 4, 2, 7),
            (1, 11, 5, 1, 3),
            (2, 50, 5, 8, 8),
            (2, 42, 6, 0, 7),
            (1, 19, 6, 7, 4),
            (2, 46, 7, 3, 8),
            (1, 18, 8, 2, 4),
            (2, 49, 8, 9, 8),
            (2, 48, 9, 2, 8),
        ),
    ),
}


file = open("TEC/Taller/Proyectos/Proyecto 2/kakuro2023partidas.dat", "wb")

pickle.dump(partidas, file)

file.close()


