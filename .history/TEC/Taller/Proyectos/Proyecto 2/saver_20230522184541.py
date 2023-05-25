import pickle

lista = [1,2,3,4,5]

file = open("archivo.dat", "wb")

pickle.dump(lista, file)

file.close()
