import pickle

category = 'FÁCIL'
elapsed_time = 100

with open('TEC/Taller/Proyectos/Proyecto 2/kakuro2023top10.dat', 'rb') as file:
        top10 = pickle.load(file)

        # Asignar nueva posicion si esta esta dentro del top 10

        for i, position in enumerate(top10[category]):
            if elapsed_time < position[2]:
                top10[category][i][position[0],'Ledvinasdas', elapsed_time])
                top10.pop()
                
                # Actualizar posiciones

                for j in range(i+1, len(top10[category])):
                    top10[category][j][0] = j+1

