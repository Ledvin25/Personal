#Quiz 6 - Ledvin Manuel Leiva Mata

def crear_listas(lista):

    list0 = []
    list1 = []
    prev = 0

    for i in enumerate(lista):
        act = i
        if act < prev:
            list0.append(list1)
            list1 = []
            for i in lista[i:]:
                act = i
                if act > prev:
                    list0.append(list1)
                    list1 = []
        list1.append(act)
            
        prev = act


crear_listas([ 10, 15, 20, 7, 15, 10, 8, -7 ])
[ [ 10, 15, 20 ], [ 7, 15 ], [ 10, 8, -7 ] ]
