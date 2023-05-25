import pickle

lista = [1,2,3,4,5]

file = open("TEC/Taller/Proyectos/Proyecto 2/", "wb")

pickle.dump(lista, file)

file.close()
