#Quiz 6 - Ledvin Manuel Leiva Mata

def crear_listas(lista):

    # 0. Inicializar variables
    list0 = []
    list1 = []
    asc = desc = False
    act = prev = sig = 0
 
    # 1. Crear una lista de listas
    for i, num in enumerate(lista):
        act = num

        # 2. Comparar el número actual con el anterior
        if act > prev:
            if desc:
                list0.append(list1)
                list1 = []
                desc = False
        # 3. Si el número actual es menor que el anterior
        elif act < prev:
            if asc:
                list0.append(list1)
                list1 = []
                asc = False

        # 4. Agregar el número actual a la lista actual
        list1.append(act)
        prev = act

        # 5. 

    # 6. Agregar la última lista a la lista de listas
    list0.append(list1)

    # 7. Retornar la lista de listas
    return list0


print(crear_listas([ 10, 15, 20, 7, 15, 10, 8, -7 ]))
#[ [ 10, 15, 20 ], [ 7, 15 ], [ 10, 8, -7 ] ]
