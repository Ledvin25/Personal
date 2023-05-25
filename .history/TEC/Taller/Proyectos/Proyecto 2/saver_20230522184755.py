import pickle

partidas = [1,2,3,4,5]

file = open("TEC/Taller/Proyectos/Proyecto 2/kakuro2023partidas.dat", "wb")

pickle.dump(lista, file)

file.close()


