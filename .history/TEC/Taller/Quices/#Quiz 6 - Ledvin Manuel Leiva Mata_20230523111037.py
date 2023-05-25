#Quiz 6 - Ledvin Manuel Leiva Mata

def crear_listas(lista):

    list0 = []
    list1 = []
    prev = 0

    for i in range(len(lista)):
        act = lista[i]
        prev = lista[i-1]
        if act < prev and lista[i+1] > lista[i+2]:
            list0.append(list1)
            list1 = []
        elif act < prev and lista[i+1] < lista[i+2]:
        list1.append(act)
            
        

    return list0


print(crear_listas([ 10, 15, 20, 7, 15, 10, 8, -7 ]))
#[ [ 10, 15, 20 ], [ 7, 15 ], [ 10, 8, -7 ] ])
