import pickle

top10 = {
    'FÁCIL': [
        (1, 'Ledvin25', (0,6,25)), 
        (2, 'JuanGamer', (0,8,32)), 
        (3, 'YorchMmn', (0,9,35)), 
        (4, 'ProPlayer', (0,12,45)), 
        (5, 'GamingMaster', (0,16,15)),
        (6, 'EpicGamer123', (0,18,50)),
        (7, 'NinjaWarrior', (0,19,10)),
        (8, 'SpeedyGamer', (1,7,55)),
        (9, 'UltraGamer', (1,13,20)),
        (10, 'MasterBlaster', (2,8,5))
    ],
    'MEDIO': [
        (1, 'TheChamp', (0,25,40)),
        (2, 'ProGamerX', (0,28,15)),
        (3, 'GameMaster', (0,32,20)),
        (4, 'SpeedDemon', (0,35,55)),
        (5, 'NinjaGamer', (1,10,30)),
        (6, 'EpicPlayer', (1,18,0)),
        (7, 'AceGamer', (1,22,50)),
        (8, 'GamingExpert', (2,5,10)),
        (9, 'QuickPlayer', (2,15,40)),
        (10, 'StealthGamer', (2,20,15))
    ],
    'DIFÍCIL': [
        (1, 'TheMastermind', (0,52,5)),
        (2, 'ProGamerZ', (0,56,45)),
        (3, 'GameChanger', (1,5,30)),
        (4, 'SpeedFreak', (1,15,20)),
        (5, 'NinjaAssassin', (1,30,10)),
        (6, 'EpicWarrior', (2,0,25)),
        (7, 'AceStrategist', (2,10,55)),
        (8, 'GamingWizard', (2,25,30)),
        (9, 'QuickThinker', (2,40,45)),
        (10, 'StealthMaster', (3,0,5))
    ],
    'EXPERTO': [
        (1, 'TheLegend', (1,20,15)),
        (2, 'ProGamerElite', (1,40,30)),
        (3, 'GameMaestro', (2,5,45)),
        (4, 'SpeedRacer', (2,25,55)),
        (5, 'NinjaSensei', (2,45,10)),
        (6, 'EpicGod', (3,5,25)),
        (7, 'AceGamerPro', (3,25,40)),
        (8, 'GamingPhenom', (3,45,50)),
        (9, 'QuickMaster', (4,5,0)),
        (10, 'StealthNinja', (4,25,15))
    ]
}


file = open("TEC/Taller/Proyectos/Proyecto 2/kakuro2023top10.dat", "wb")

pickle.dump(partidas, file)

file.close()


