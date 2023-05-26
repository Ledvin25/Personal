import pickle

partidas = {
    'FÁCIL': [(1, 'Ledvin25', (0,6,25)), (2, 'JuanGamer', (0,8,32)), (3, 'YorchMmn', (0,9,35)), (4, 'Jorge', (0,10,40)), (5, 'Jorge', (0,11,45)), (6, 'Jorge', (0,12,50)), (7, 'Jorge', (0,13,55)), (8, 'Jorge', (0,14,60)), (9, 'Jorge', (0,15,65)), (10, 'Jorge', (0,16,70))],
}


file = open("TEC/Taller/Proyectos/Proyecto 2/kakuro2023top10.dat", "wb")

pickle.dump(partidas, file)

file.close()


