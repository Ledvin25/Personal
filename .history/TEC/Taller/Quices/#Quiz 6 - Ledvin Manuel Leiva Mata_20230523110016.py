#Quiz 6 - Ledvin Manuel Leiva Mata

def crear_listas(lista):

    lista.append(0)
    list0 = []
    list1 = []
    prev = 0

    for i, num in enumerate(lista):
        act = num
        if act < prev:
            for num in lista[i:]:
                act = num
                if lista[i+1] > act and len(list1) == 0:
                    break
                list1.append(act)
                prev = act
                if lista[i+1] > act:
                    list0.append(list1)
                    list1 = []
                    break
                
        if act > prev:        
            list1.append(act)
            prev = act

    return list0


crear_listas([ 10, 15, 20, 7, 15, 10, 8, -7 ])
[ [ 10, 15, 20 ], [ 7, 15 ], [ 10, 8, -7 ] ]