#Quiz 6 - Ledvin Manuel Leiva Mata

def crear_listas(lista):

    list0 = []
    list1 = []
    asc = desc = False
    act = prev = 0
 
    # 1. Crear una lista de listas
    for num in lista:
        act = num

        # 
        if act > prev:
            if desc:
                list0.append(list1)
                list1 = []
                desc = False
            asc = True
        elif act < prev:
            if asc:
                list0.append(list1)
                list1 = []
                asc = False
            desc = True

        list1.append(act)
        prev = act

    list0.append(list1)
    return list0


print(crear_listas([ 10, 15, 20, 7, 15, 10, 8, -7 ]))
#[ [ 10, 15, 20 ], [ 7, 15 ], [ 10, 8, -7 ] ]
