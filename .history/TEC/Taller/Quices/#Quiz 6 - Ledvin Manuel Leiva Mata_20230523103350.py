#Quiz 6 - Ledvin Manuel Leiva Mata

def crear_listas(lista):

    list1 = []

    for i in lista:
        act = i
        if act > prev:
            list1.append(act)
            break
        prev = act


crear_listas([ 10, 15, 20, 7, 15, 10, 8, -7 ])
[ [ 10, 15, 20 ], [ 7, 15 ], [ 10, 8, -7 ] ]
