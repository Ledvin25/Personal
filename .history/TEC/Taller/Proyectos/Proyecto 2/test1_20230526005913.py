import pickle

category = 'FÁCIL'
elapsed_time = 100

with open('TEC/Taller/Proyectos/Proyecto 2/kakuro2023top10.dat', 'rb') as file:
        top10 = pickle.load(file)

        # Asignar nueva posicion si esta esta dentro del top 10

        for position in top10[category]:
            if elapsed_time < position[2]:
                new_position = top10[category].index(position)
                break