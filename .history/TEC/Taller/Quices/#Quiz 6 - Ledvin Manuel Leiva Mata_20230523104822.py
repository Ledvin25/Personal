#Quiz 6 - Ledvin Manuel Leiva Mata

def crear_listas(lista):

    list0 = []
    list1 = []
    prev = 0

    for i, num in enumerate(lista):
        act = num
        if act < prev:
            list0.append(list1)
            list1 = []
            for num in lista[i:]:
                act = num
                if act > prev:
                    list0.append(list1)
                    list1 = []
                    break
                list1.append(act)
                prev = act
        list1.append(act)
            
        prev = act


crear_listas([ 10, 15, 20, 7, 15, 10, 8, -7 ])
[ [ 10, 15, 20 ], [ 7, 15 ], [ 10, 8, -7 ] ]
