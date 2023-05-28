import pickle

top10 = {
    'FÁCIL': [
        
    ],
    'MEDIO': [
        
    ],
    'DIFÍCIL': [
        [1, 'TheMastermind', 3125],
        [2, 'ProGamerZ', 3405],
        [3, 'GameChanger', 3930],
        [4, 'SpeedFreak', 4520],
        [5, 'NinjaAssassin', 5410],
        [6, 'EpicWarrior', 7225],
        [7, 'AceStrategist', 6990],
        [8, 'GamingWizard', 5200],
        [9, 'QuickThinker', 5745],
        [10, 'StealthMaster', 6805]
    ],
    'EXPERTO': [
        [1, 'TheLegend', 4815],
        [2, 'ProGamerElite', 7230],
        [3, 'GameMaestro', 6545],
        [4, 'SpeedRacer', 6555],
        [5, 'NinjaSensei', 5710],
        [6, 'EpicGod', 5325],
        [7, 'AceGamerPro', 4240],
        [8, 'GamingPhenom', 5650],
        [9, 'QuickMaster', 3700],
        [10, 'StealthNinja', 3915]
    ]
}


file = open("TEC/Taller/Proyectos/Proyecto 2/kakuro2023top10.dat", "wb")

pickle.dump(top10, file)

file.close()


