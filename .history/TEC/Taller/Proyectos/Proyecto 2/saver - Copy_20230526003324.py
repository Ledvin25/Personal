import pickle

partidas = {
    'FÁCIL': (1, 'Ledvin25', '')
}


file = open("TEC/Taller/Proyectos/Proyecto 2/kakuro2023top10.dat", "wb")

pickle.dump(partidas, file)

file.close()


