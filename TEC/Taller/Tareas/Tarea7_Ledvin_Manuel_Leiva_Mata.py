# Tarea 6 - Ledvin Manuel Leiva Mata

# Ejercicio 1

def suma_digitos(n):
    if isinstance(n, int) and n < 0:
        return -1
    else:
        suma = 0
        while n > 0:
            suma+=n%10
            n //= 10
        return suma
    
# Pila
    
def suma_digitos_p(n):
    if isinstance(n, int) and n < 0:
        return -1
    else:
        return suma_digitos(n//10) + n%10

#Cola
def suma_digitos_c(n, acc=0):
    if isinstance(n, int) and n < 0:
        return -1
    if n == 0:
        return acc
    return suma_digitos_c(n//10, acc+n%10)
    
# Ejercicio 2

def obtiene_divisores(n):
    if not isinstance(n, int) and n >= 1:
        return []
    else: 
        lista = []
        i = 1
        while i <= n:
            if n%i == 0:
                lista.append(i)
            i += 1

        return lista
    
# Pila
def obtiene_divisores_p(n):
    if not isinstance(n, int) and n >= 1:
        return []
    else:
        return obtiene_divisores_p_aux(n,n)


def obtiene_divisores_p_aux(n, i):
    if i == 0:
        return []
    elif n%i == 0:
        prev = obtiene_divisores_p_aux(n, i-1)
        prev.append(i)
        return prev
    else:
        return obtiene_divisores_p_aux(n, i-1)
    
# Cola
def obtiene_divisores_c(n):
    if not isinstance(n, int) and n >= 1:
        return []
    else:
        return obtiene_divisores_c_aux(n,1, [])
    
def obtiene_divisores_c_aux(n, i, lista):
    if i > n:
        return lista
    elif n%i == 0:
        lista.append(i)
    return obtiene_divisores_c_aux(n,i+1,lista)
        
    
# Ejercicio 3

# iteracion
def sumatoria_cuadrados(m,n):

    if n < m:
        return -1
    suma = 0
    for i in range(m,n+1):
        suma += i**2

    return suma

# Pila

def sumatoria_cuadrados_p(m,n):
    if n < m:
        return -1
    elif m == n:
        return m**2
    else:
        return sumatoria_cuadrados_p(m,n-1) + n**2
    
# Cola

def sumatoria_cuadrados_c(m,n, acc = 0):
    if n < m:
        return -1
    elif n == m:
        return acc + n**2
    else:
        acc += n**2
        return sumatoria_cuadrados_c(m,n-1,acc)
    
# Ejercicio 4

def pares_impares(n):
    if not isinstance(n, int):
        return ()
    else:
        pares = 0
        impares = 0
        while n > 0:
            if n%2 == 0:
                pares += 1
            else:
                impares += 1
            n //= 10
        return pares, impares
    
# Pila

def pares_impares_p(n):
    if not isinstance(n, int):
        return ()
    if n == 0:
        return (0,0)
    else:
        pares, impares = pares_impares_p(n//10)
        if n%2 == 0:
            pares += 1
        else:
            impares += 1
        return pares, impares
    
# Cola

def pares_impares_c(n, pares = 0, impares = 0):
    if not isinstance(n, int):
        return ()
    if n == 0:
        return pares, impares
    elif n%2 == 0:
        return pares_impares_c(n//10, pares+1, impares)
    else:
        return pares_impares_c(n//10, pares, impares+1)

# Ejercicio 5

# pila
def multiplos_p(n,a,b,):
    if a > b:
        return []
    
    multiplo = multiplos_p(n,a,b-1)
    multiplo.append(b*n)
    return multiplo
    
# cola

def multiplos_c(n,a,b,lista = []):
    if a > b:
        return lista
    else:
        lista.append(a*n)
        return multiplos_c(n,a+1,b,lista)
    
# Ejercicio 6

# iteracion

def tipo_matriz(matriz, tipo):
    
    new_matriz = []

    # Matriz triangular superior
    if tipo == 1:
        for fila in matriz:
            new_fila = []
            for columna in fila:
                if fila.index(columna) >= matriz.index(fila):
                    new_fila.append(columna)
                else:
                    new_fila.append(0)
            new_matriz.append(new_fila)
    # Matriz triangular inferior
    if tipo == 2:
        for fila in matriz:
            new_fila = []
            for columna in fila:
                if fila.index(columna) <= matriz.index(fila):
                    new_fila.append(columna)
                else:
                    new_fila.append(0)
            new_matriz.append(new_fila)
    # Matriz diagonal
    if tipo == 3:
        for fila in matriz:
            new_fila = []
            for columna in fila:
                if fila.index(columna) == matriz.index(fila):
                    new_fila.append(columna)
                else:
                    new_fila.append(0)
            new_matriz.append(new_fila)
        
    return new_matriz


# Pila
def tipo_matriz_p(matriz, tipo):
    if not matriz:
        return matriz

    fila = len(matriz) - 1
    columna = len(matriz[0]) - 1

    return tipo_matriz_p_helper(matriz, tipo, fila, columna)


def tipo_matriz_p_helper(matriz, tipo, fila, columna):
    if fila < 0:
        return matriz
    
    if columna < 0:
        return tipo_matriz_p_helper(matriz, tipo, fila-1, len(matriz[0])-1)

    if tipo == 1:
        if fila > columna:
            matriz[fila][columna] = 0
    elif tipo == 2:
        if fila < columna:
            matriz[fila][columna] = 0
    elif tipo == 3:
        if fila != columna:
            matriz[fila][columna] = 0

    return tipo_matriz_p_helper(matriz, tipo, fila, columna-1)

# cola
def tipo_matriz_c(matriz, tipo, fila = 0, columna = 0):
    if fila == len(matriz):
        return matriz
    elif columna == len(matriz[0]):
        return tipo_matriz_c(matriz, tipo, fila+1, 0)
    else:
        if tipo == 1:
            if fila > columna:
                matriz[fila][columna] = 0
        elif tipo == 2:
            if fila < columna:
                matriz[fila][columna] = 0
        elif tipo == 3:
            if fila != columna:
                matriz[fila][columna] = 0

        return tipo_matriz_c(matriz, tipo, fila, columna+1)

# Ejercicio 7

def matriz_unitaria(n):
    
    matriz = [[0] * n for i in range(n)]

    for i in range(n):
        matriz[i][i] = 1

    return matriz

# Pila

def matriz_unitaria_p(n, matriz = [], i = 0):
    if i == n:
        return matriz
    else:
        matriz.append([0] * n)
        matriz[i][i] = 1
        return matriz_unitaria_p(n, matriz, i+1)
    
# Cola

def matriz_unitaria_c(n, matriz = None, i = 0):
    if matriz is None:
        matriz = []
    if i == n:
        return matriz
    else :
        matriz.append([0] * n)
        matriz[i][i] = 1
        return matriz_unitaria_c(n, matriz, i+1)

# Ejercicio 8

# Pila - coautor Joseph Arrieta
def extrae_diagonal_p(matriz, numero_diagonal):

    if len(matriz) != len(matriz[0]):
        return "ERROR: NO ES CUADRADA"


    if abs(numero_diagonal) >= len(matriz[0]):
        return "ERROR: NO EXISTE LA DIAGONAL"

    def diagonal(fila, columna, diagonal_actual):
        if fila >= len(matriz) or columna >= len(matriz[0]):
            return diagonal_actual[::-1] 
        else:
            return diagonal(fila + 1, columna + 1, [matriz[fila][columna]] + diagonal_actual) 

    if numero_diagonal >= 0:
        fila_inicial = 0
        columna_inicial = numero_diagonal
    else:
        fila_inicial = abs(numero_diagonal)
        columna_inicial = 0

    return diagonal(fila_inicial, columna_inicial, []) 

# Cola

def extraer_diagonal_c(matriz, diagonal):
    if len(matriz) != len(matriz[0]):
        return "La matriz no es cuadrada"
    if diagonal > len(matriz):
        return "La diagonal no existe"
    else:
        return extraer_diagonal_c_helper(matriz, diagonal)

def extraer_diagonal_c_helper(matriz, diagonal, i = 0, vector = []):
    if i == len(matriz):
        return vector
    else:
        if diagonal >= 0 and i+diagonal < len(matriz):
            diag = matriz[i][i+diagonal]
            vector.append(diag)
        elif diagonal < 0 and i-diagonal < len(matriz):
            diag = matriz[i-diagonal][i]
            vector.append(diag)

        return extraer_diagonal_c_helper(matriz, diagonal, i+1, vector)
    
# Ejercicio 9

# Pila

def lista_unica(lista, i = 0):
        if i+len(lista)-1 < 0:
            return []
        elif type(lista[i+len(lista)-1]) == list:
            return lista_unica(lista, i-1) + lista_unica(lista[i+len(lista)-1])
        else:
            return lista_unica(lista, i-1) + [lista[i+len(lista)-1]]

#Ejercicio 10

# Pila
def ele_p(matriz, inicio, final):
    # Verificar si las filas y columnas existen
    try:
        matriz[inicio[0]][inicio[1]]
        matriz[final[0]][final[1]]
    except IndexError:
        return "ERROR: FILA O COLUMNA NO EXISTE"
    # Verificar si la primera casilla es menor que la segunda
    if inicio[0] >= final[0] or inicio[1] >= final[1]:
        return "ERROR: LA PRIMERA CASILLA ES MAYOR QUE LA SEGUNDA"
    else:
        resultado = ele_p_helper(matriz, inicio, final)
        resultado.reverse()
        resultado.append((final[0], final[1], matriz[final[0]][final[1]]))
        return resultado

def ele_p_helper(matriz, inicio, final):
    if inicio == final:
        return []
    else:
        if inicio[0] < final[0]:
            lista = ele_p_helper(matriz, (inicio[0] + 1, inicio[1]), final)
            lista.append((inicio[0], inicio[1], matriz[inicio[0]][inicio[1]]))
            return lista
        elif inicio[1] < final[1]:
            lista = ele_p_helper(matriz, (inicio[0], inicio[1] + 1), final)
            lista.append((inicio[0], inicio[1], matriz[inicio[0]][inicio[1]]))
            return lista
        
# cola
def ele_c(matriz, inicio, final):
    # Verificar si las filas y columnas existen
    try:
        matriz[inicio[0]][inicio[1]]
        matriz[final[0]][final[1]]
    except IndexError:
        return "ERROR: FILA O COLUMNA NO EXISTE"
    # Verificar si la primera casilla es menor que la segunda
    if inicio[0] >= final[0] or inicio[1] >= final[1]:
        return "ERROR: LA PRIMERA CASILLA ES MAYOR QUE LA SEGUNDA"
    else:
        resultado = ele_c_helper(matriz, inicio, final, [])
        resultado.append((final[0], final[1], matriz[final[0]][final[1]]))
        return resultado

def ele_c_helper(matriz, inicio, final, lista):
    if inicio == final:
        return lista
    else:
        lista.append((inicio[0], inicio[1], matriz[inicio[0]][inicio[1]]))

        if inicio[0] < final[0]:
            return ele_c_helper(matriz, (inicio[0] + 1, inicio[1]), final, lista)
        elif inicio[1] < final[1]:
            return ele_c_helper(matriz, (inicio[0], inicio[1] + 1), final, lista)
        
# Ejercicio 11

# Cola

def pedidos_totales(pedidos):
    cola = []

    for diccionario in pedidos:
        for clave, valor in diccionario.items():
            cola.append((clave, valor))

    total_pedidos = {} 

    def pedidos_t():
        if len(cola) == 0:
            return total_pedidos

        clave, valor = cola.pop(0)
        if clave in total_pedidos:
            total_pedidos[clave] += valor
        else:
            total_pedidos[clave] = valor

        return pedidos_t() 

    return pedidos_t()




    