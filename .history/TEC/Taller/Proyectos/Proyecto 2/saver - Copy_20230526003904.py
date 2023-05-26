import pickle

partidas = {
    'FÁCIL': [(1, 'Ledvin25', (0,6,25)), 
              (2, 'JuanGamer', (0,8,32)), 
              (3, 'YorchMmn', (0,9,35)), 
              (4, 'ProPlayer', (1, 12, 45)), 
              (5, 'GamingMaster', (0, 10, 15)),
              (6, 'EpicGamer123', (0, 11, 50))

(7, 'NinjaWarrior', (0, 9, 10))
(8, 'SpeedyGamer', (0, 7, 55))]
}


file = open("TEC/Taller/Proyectos/Proyecto 2/kakuro2023top10.dat", "wb")

pickle.dump(partidas, file)

file.close()


