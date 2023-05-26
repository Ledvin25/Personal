import pickle

partidas = {
    
}


file = open("TEC/Taller/Proyectos/Proyecto 2/kakuro2023partidas.dat", "wb")

pickle.dump(partidas, file)

file.close()


