#Quiz 6 - Ledvin Manuel Leiva Mata

def crear_listas(lista):

    list0 = []
    list1 = []
    asc = desc = False
    act = prev = 0


    for num in lista:
        act = num

        if desc:
            if asc:
                list1.pop()
                list0.append(list1)
                list1 = []
                desc = False
            asc = True
        if asc:
            if desc:
                list1.pop()
                list0.append(list1)
                list1 = []
                asc = False
            desc = True

        list1.append(act)
        prev = act

    return list0


print(crear_listas([ 10, 15, 20, 7, 15, 10, 8, -7 ]))
#[ [ 10, 15, 20 ], [ 7, 15 ], [ 10, 8, -7 ] ])
