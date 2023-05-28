import pickle

top10 = {
    'FÁCIL': [[0],[1],[2],
              [3
                [1, 'Ledvin25', 385],
                [2, 'JuanGamer', 512],
                [3, 'YorchMmn', 575],
                [4, 'ProPlayer', 765],
                [5, 'GamingMaster', 975],
                [6, 'EpicGamer123', 1130],
                [7, 'NinjaWarrior', 1150],
                [8, 'SpeedyGamer', 1075],
                [9, 'UltraGamer', 1125],
                [10, 'MasterBlaster', 1245]
                ]
            ],
    'MEDIO': [[0],[1],[2],
              [3
                [1, 'TheChamp', 1540],
                [2, 'ProGamerX', 1695],
                [3, 'GameMaster', 1940],
                [4, 'SpeedDemon', 2155],
                [5, 'NinjaGamer', 6630],
                [6, 'EpicPlayer', 6480],
                [7, 'AceGamer', 5000],
                [8, 'GamingExpert', 7510],
                [9, 'QuickPlayer', 6900],
                [10, 'StealthGamer', 5895]
            ]
        ],
    'DIFÍCIL': [[0],[1],[2],
            [3
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
            ]
        ],
    'EXPERTO': [[0],[1],[2],[3
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


