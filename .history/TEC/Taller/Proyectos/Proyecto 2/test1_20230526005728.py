import pickle

category = 'FÁCIL'

with open('TEC/Taller/Proyectos/Proyecto 2/kakuro2023top10.dat', 'rb') as file:
            top10 = pickle.load(file)

        # Asignar nueva posicion si esta esta dentro del top 10

        for position in top10[category]:
            print(position)