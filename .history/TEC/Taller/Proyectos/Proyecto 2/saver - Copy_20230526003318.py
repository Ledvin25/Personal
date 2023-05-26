import pickle

partidas = {
    'FÁCIL': (1, 'Ledvin M ')
}


file = open("TEC/Taller/Proyectos/Proyecto 2/kakuro2023top10.dat", "wb")

pickle.dump(partidas, file)

file.close()


