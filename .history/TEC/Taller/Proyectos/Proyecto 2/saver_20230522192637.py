import pickle

partidas = {
    'FÁCIL': (
        # Niveles de la categoría Fácil
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
            # Nivel adicional 1
            (2, 30, 1, 2, 5),
            (2, 15, 1, 3, 3),
            (2, 22, 1, 5, 4),
            (2, 12, 1, 6, 2),
            (2, 37, 1, 8, 7),
            (2, 18, 1, 9, 3),
            (1, 11, 2, 1, 3),
            (1, 12, 2, 4, 3),
            (1, 9, 2, 7, 2),
        ),
        (
            # Nivel adicional 2
            (2, 35, 1, 2, 6),
            (2, 50, 1, 3, 10),
            (2, 26, 1, 5, 5),
            (2, 8, 1, 6, 2),
            (2, 42, 1, 8, 6),
            (2, 21, 1, 9, 4),
            (1, 13, 2, 1, 4),
            (1, 14, 2, 4, 4),
            (1, 11, 2, 7, 3),
        ),
    ),
    'MEDIO': (
        # Niveles de la categoría Medio
        (
            (2, 55, 1, 2, 9),
            (2, 27, 1, 3, 6),
            (2, 40, 1, 5, 8),
            (2, 14, 1, 6, 2),
            (2, 48, 1, 8, 9),
            (2, 25, 1, 9, 5),
            (1, 16, 2, 1, 5),
            (1, 20, 2, 4, 6),
            (1, 15, 2, 7, 4),
        ),
        (
            # Nivel adicional 1
            (2, 38, 1, 2, 7),
            (2, 19, 1, 3, 4),
            (2, 32, 1, 5, 6),
            (2, 13, 1, 6, 2),
            (2, 45, 1, 8, 8),
            (2, 23, 1, 9, 4),
            (1, 14, 2, 1, 4),
            (1, 18, 2, 4, 5),
            (1, 13, 2, 7, 3),
        ),
        (
            # Nivel adicional 2
            (2, 42, 1, 2, 8),
            (2, 23, 1, 3, 5),
            (2, 36, 1, 5, 7),
            (2, 16, 1, 6, 3),
            (2, 50, 1, 8, 10),
            (2, 28, 1, 9, 6),
            (1, 15, 2, 1, 5),
            (1, 19, 2, 4, 6),
            (1, 14, 2, 7, 4),
        ),
    ),
    'DIFÍCIL': (
        # Niveles de la categoría Difícil
        (
            (2, 65, 1, 2, 11),
            (2, 32, 1, 3, 7),
            (2, 50, 1, 5, 10),
            (2, 18, 1, 6, 4),
            (2, 63, 1, 8, 11),
            (2, 32, 1, 9, 7),
            (1, 18, 2, 1, 6),
            (1, 25, 2, 4, 8),
            (1, 19, 2, 7, 5),
        ),
        (
            # Nivel adicional 1
            (2, 60, 1, 2, 10),
            (2, 29, 1, 3, 6),
            (2, 46, 1, 5, 9),
            (2, 16, 1, 6, 4),
            (2, 57, 1, 8, 10),
            (2, 29, 1, 9, 6),
            (1, 17, 2, 1, 6),
            (1, 24, 2, 4, 8),
            (1, 18, 2, 7, 5),
        ),
        (
            # Nivel adicional 2
            (2, 70, 1, 2, 12),
            (2, 35, 1, 3, 8),
            (2, 54, 1, 5, 11),
            (2, 20, 1, 6, 5),
            (2, 70, 1, 8, 12),
            (2, 35, 1, 9, 8),
            (1, 20, 2, 1, 7),
            (1, 27, 2, 4, 9),
            (1, 21, 2, 7, 6),
        ),
    ),
    'EXPERTO': (
        # Niveles de la categoría Experto
        (
            (2, 80, 1, 2, 14),
            (2, 40, 1, 3, 9),
            (2, 62, 1, 5, 13),
            (2, 22, 1, 6, 6),
            (2, 80, 1, 8, 14),
            (2, 40, 1, 9, 9),
            (1, 22, 2, 1, 8),
            (1, 30, 2, 4, 10),
            (1, 23, 2, 7, 7),
        ),
        (
            # Nivel adicional 1
            (2, 75, 1, 2, 13),
            (2, 37, 1, 3, 8),
            (2, 58, 1, 5, 12),
            (2, 21, 1, 6, 6),
            (2, 75, 1, 8, 13),
            (2, 37, 1, 9, 8),
            (1, 21, 2, 1, 7),
            (1, 28, 2, 4, 9),
            (1, 22, 2, 7, 7),
        ),
        (
            # Nivel adicional 2
            (2, 90, 1, 2, 16),
            (2, 45, 1, 3, 10),
            (2, 70, 1, 5, 15),
            (2, 25, 1, 6, 7),
            (2, 90, 1, 8, 16),
            (2, 45, 1, 9, 10),
            (1, 24, 2, 1, 9),
            (1, 33, 2, 4, 11),
            (1, 25, 2, 7, 8),
        ),
    ),
}


file = open("TEC/Taller/Proyectos/Proyecto 2/kakuro2023partidas.dat", "wb")

pickle.dump(partidas, file)

file.close()


