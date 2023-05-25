import pickle

file = open("archivo.dat", "db")

lista = [1,2,3,4,5]

pickle.dump(lista, file)

file.close()
