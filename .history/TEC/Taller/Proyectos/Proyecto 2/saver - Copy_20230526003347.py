import pickle

partidas = {
    'FÁCIL': (1, 'Ledvin25', (6,4,))
}


file = open("TEC/Taller/Proyectos/Proyecto 2/kakuro2023top10.dat", "wb")

pickle.dump(partidas, file)

file.close()


