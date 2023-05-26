import pickle

top10 = {
    'FÁCIL': [(1, 'Ledvin25', (0,6,25)), 
              (2, 'JuanGamer', (0,8,32)), 
              (3, 'YorchMmn', (0,9,35)), 
              (4, 'ProPlayer', (0, 12, 45)), 
              (5, 'GamingMaster', (0, 16, 15)),
              (6, 'EpicGamer123', (0, 18, 50)),
              (7, 'NinjaWarrior', (0, 19, 10)),
              (8, 'SpeedyGamer', (1, 7, 55)),
              (9, 'UltraGamer', (1, 13, 20)),
              (10, 'MasterBlaster', (0, 8, 5))]
}


file = open("TEC/Taller/Proyectos/Proyecto 2/kakuro2023top10.dat", "wb")

pickle.dump(partidas, file)

file.close()


