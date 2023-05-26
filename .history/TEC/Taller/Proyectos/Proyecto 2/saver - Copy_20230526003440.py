import pickle

partidas = {
    'FÁCIL': (1, 'Ledvin25', (0,6,25)), (2, 'JuanGamer', (0,6,25)), (3, 'Jorge', (0,6,25)), (4, 'Jorge', (0,6,25)), (5, 'Jorge', (0,6,25)), (6, 'Jorge', (0,6,25)), (7, 'Jorge', (0,6,25)), (8, 'Jorge', (0,6,25)), (9, 'Jorge', (0,6,25)), (10, 'Jorge', (0,6,25)),
}


file = open("TEC/Taller/Proyectos/Proyecto 2/kakuro2023top10.dat", "wb")

pickle.dump(partidas, file)

file.close()


