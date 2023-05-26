import pickle

partidas = {
    'FÁCIL': [(1, 'Ledvin25', (0,6,25)), (2, 'JuanGamer', (0,8,32)), (3, 'YorchMmn',)]
}


file = open("TEC/Taller/Proyectos/Proyecto 2/kakuro2023top10.dat", "wb")

pickle.dump(partidas, file)

file.close()


