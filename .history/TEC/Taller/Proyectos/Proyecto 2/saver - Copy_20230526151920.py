import pickle

top10 = {
    'FÁCIL': [
        
    ],
    'MEDIO': [
        
    ],
    'DIFÍCIL': [
       
    ],
    'EXPERTO': [
        
    ]
}


file = open("TEC/Taller/Proyectos/Proyecto 2/kakuro2023top10.dat", "wb")

pickle.dump(top10, file)

file.close()


