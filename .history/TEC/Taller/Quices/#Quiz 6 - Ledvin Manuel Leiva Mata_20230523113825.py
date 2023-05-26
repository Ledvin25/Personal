#Quiz 6 - Ledvin Manuel Leiva Mata

def crear_listas(lista):

    list0 = []
    list1 = []
    asc = desc = False
    act = prev = 0


    for i, num in lista:
        act = num

        if desc:
            list1.append(act)
            if asc:
                list1.pop()
                list0.append(list1)
                list1 = []
                desc = False
        if asc:
            list1.append(act)
            if desc:
                list1.pop()
                list0.append(list1)
                list1 = []
                asc = False

        if lista[i+1] > act:
            asc = True
        elif lista[i+1] < act:
            desc = True

        prev = act

    return list0


print(crear_listas([ 10, 15, 20, 7, 15, 10, 8, -7 ]))
#[ [ 10, 15, 20 ], [ 7, 15 ], [ 10, 8, -7 ] ])