#Tarea 5 - Ledvin Manuel Leiva Mata
#Coautores - Joseph Arrieta, Alejandro Gutierrez

# para el siguiente codigo se utilizara habitualmente i, j y k como contadores por la convencion ya existente.

#Ejercicio 1

#for
def indices_for(x,y):
    if not isinstance(y, list):
        return "Error, el segundo parametro debe ser una lista"
    indices_finales = []

    for i, element in enumerate(y):
        if element == x:
            indices_finales.append(i)
    return indices_finales
        

#trozos

#funcion inicial donde se dictan los parametros iniciales
def indices_trozos(x,y):
    if not isinstance(y, list):
        return "Error, el segundo parametro debe ser una lista"
    else:
        resultados = buscar(x, y, 0, [])
        if not resultados:
            return []
        else:
            return resultados

#funcion recursiva para encontrar los indices y devolverlo en forma de lista.
def buscar(x,y,start, final_index):
    if not start == len(y):
        indices_finales = final_index
        
        try:
            position = y[start:].index(x)
            indices_finales.append(start + position)
            new_start = start + position + 1
            return buscar(x, y, new_start, indices_finales)
            
        except ValueError:
            return None
    else:
        return final_index
    

#indices 

def indices_indices(x,y):
    if not isinstance(y, list):
        return "Error, el segundo parametro debe ser una lista"
    else:
        i = 0
        indices_finales = []
        while i < len(y):
            
            if x == y[i]:
                indices_finales.append(i)
            i+= 1
        return indices_finales

#Ejercicio 2


def consultar_disciplina(disciplina, lista):

    for element in lista:
        if element[0] == disciplina:
            return element[1]
    return "ERROR: NO SE PUEDE CONSULTAR PORQUE NO EXISTE"

def agregar_disciplina(disciplina, medicion, lista):
    
    if consultar_disciplina(disciplina, lista) == "ERROR: NO SE PUEDE CONSULTAR PORQUE NO EXISTE":
        element = (disciplina, medicion)
        lista.append(element)
        return ""
    else:
        return "ERROR: NO SE PUEDE AGREGAR PORQUE YA EXISTE"

def eliminar_disciplina(disciplina, lista):
    if consultar_disciplina(disciplina, lista) == "ERROR: NO SE PUEDE CONSULTAR PORQUE NO EXISTE":
        return 'ERROR: NO SE PUEDE ELIMINAR PORQUE NO EXISTE'
    else:
        for element in lista:
            if element[0] == disciplina:
                lista.remove(element)
        return ''

def modificar_disciplina(disciplina, medicion, lista):
    if consultar_disciplina(disciplina, lista) == "ERROR: NO SE PUEDE CONSULTAR PORQUE NO EXISTE":
        return 'ERROR: NO SE PUEDE MODIFICAR PORQUE NO EXISTE'
    else:
        for i ,element in enumerate(lista):
            if element[0] == disciplina:
                new_tupla = (element[0], medicion)
                lista[i] = new_tupla
        return ''
    
# Ejercicio 3

def juegos_de_bola(lista):
    
    if not isinstance(lista, list) or len(lista) < 2:
        return False
    else:
        pares_finales = []

        for i in lista:
            for j in lista:
                if not i[0] == j[0]:
                    new_tuple = (i[0], j[0])
                    ups = tuple(reversed(new_tuple))
                    if ups not in pares_finales: 
                        pares_finales.append(new_tuple)
        return pares_finales


# Ejercicio 4

def agrupar(lista):
    
    lista_final = []

    for element in lista:
        string = str(element)
        num = []
        for i in string:
            if i not in num:
                for j in string:
                    if i == j:
                        num.append(j)
        lista_final.append(int(''.join(num)))
        
    return lista_final

            

# Ejercicio 5

def repetir_digito(tupla): #buscar, analizar, reps

    buscar = str(tupla[0])
    analizar = str(tupla[1])
    repeticiones = int(tupla[2])
    numero = []

    for element in analizar:
        i = 0
        if element == buscar:
            while i < repeticiones:
                numero.append(element)
                i += 1
        else:
            numero.append(element)

    return int(''.join(numero))

# Ejercicio 6

def diferencia_simetrica(tuplas):
    
    tupla_final = ()

    for tupla in tuplas:
        num1 = str(tupla[0])
        num2 = str(tupla[1])
        num = []

        for element in num1:
            if element not in num2 and element not in num:
                num.append(element)
        for element in num2:
            if element not in num1 and element not in num:
                num.append(element)
        if num == []:
            num_final = -1
        else:
            num_final = int(''.join(num))
        tupla_final+= (num_final,)

    return tupla_final

# Ejercicio 7

def es_altamente_abundante(lista):
    result = []
    for element in lista:
        suma = 0
        
        for i in range(int(element)):
               i +=1
               if element % i == 0:
                    suma += i
        for i in range(int(element)):
            j = 0
            suma2 = 0
            for j in range(i):
                j+=1
                if i % j == 0:
                    suma2 += j
            if j == i:
                if suma2 > suma:
                    prev_result = False
                    break
                else:
                    prev_result = True
        result.append(prev_result)
    return result

# ejercicio 8

def fibonacci(numero):
    result = []
    fibo1 = 0
    fibo2 = 1

    tupla = (fibo1, fibo2)

    for i in range(numero - 2):
        fibo = fibo1 + fibo2
        tupla += (fibo, )
        fibo1 = fibo2
        fibo2 = fibo
    return tupla
        

# ejercicio 9

def es_numero_keith(lista):

    result = []

    for num1 in lista:
        num2 = str(num1)

        digitos = []

        for digito in num2:
            digitos.append(int(digito))
        
        while True:
            suma = sum(digitos)

            if suma > num1:
                result.append(False)
                break
            elif suma == num1:
                result.append(True)
                break

            digitos.append(suma)
            digitos = digitos[1:]
            
    return result

#Ejercicio 10

def es_palabra_palindromo(word):
    if word == '':
        return 'ERROR: LA ENTRADA DEBE SER UN STRING DIFERENTE DE VACIO'
    else:
        word1 = list(word)
        word1.reverse()
        word1 = str(''.join(word1))

        if word1 == word:
            return True
        else:
            return False

#Ejercicio 11

def extrae_numeros(string0):

    result = []
    i = 0

    while True:
        string = string0
        
        try:
            int(string[i])
            j = len(string)

            while True:
                try:
                    numero = float(string[i:])
                    if (numero % 1) == 0:
                        numero = int(numero)
                    result.append(numero)
                    break
                except:
                    string = string[:j]
                    j -= 1

        except: 
            if len(string0) <= 1:
                return result
            i += 1
            continue
        string0 = string0[(j+1):]
        i = 0
        
#Ejercicio 12

def decimal_a_hexadecimal(lista):

    hexa_conversiones = {'10':'A', '11':'B', '12':'C', '13':'D', '14':'E', '15' : 'F'}
    result = []
    

    for decimal in lista:
        hexa_residuos = []

        while decimal > 0:
            hexa_residuos.append(decimal%16)
            decimal = decimal // 16
        
        for i, numero in enumerate(hexa_residuos):
            if numero >= 10:
                hexa_residuos[i] = hexa_conversiones[str(numero)]
            else:
                hexa_residuos[i] = str(numero)
        hexa_residuos.reverse()
        result.append(str(''.join(hexa_residuos)))

    return result

# Ejercicio 13

def leer_matriz(x,y):
    
    matriz = []

    for i in range(x):
        fila = []
        for j in range(y):
            value = input()
            fila.append(value)
        matriz.append(fila)

    return matriz

# Ejercicio 14

# A
def imprimir_matriz(matriz):
    
    for fila in matriz:
        for columna in fila:
            print("{:>8}".format(columna), end='')
        print()

# B
def es_matriz_nula(matriz):

    for fila in matriz:
        for columna in fila:
            if columna != 0:
                return False
    return True

# Ejercicios 15

def sumar_resta_matrices(A,B,operacion):

    if len(A) != len(B):
        return 'Las matrices deben tener la misma cantidad de filas'
    else:
        if len(A[0]) != len(B[0]):
            return 'Las matrices deben tener la misma cantidad de columnas'
        else:

            new_matrix = []

            for fila_A, fila_B in zip(A, B):
                new_fila = []
                for columna_A, columna_B in zip(fila_A, fila_B):
                    if operacion == '+':
                        result = columna_A + columna_B
                    elif operacion == '-':
                        result = columna_A - columna_B
                    new_fila.append(result)
                new_matrix.append(new_fila)       
      

# Ejercicio 16

def triángulo_de_pascal(n):
    
    if n < 1:
        return "Debe ingresar un numero mayor o igual a 1"
    triangulo = [[1]]
   
    for i in range(n-1):
        nivel_anterior = triangulo[-1]
        nuevo_nivel = [1]
        for j in range(len(nivel_anterior)-1):
            nuevo_nivel.append(nivel_anterior[j] + nivel_anterior[j+1])
        nuevo_nivel.append(1)
        triangulo.append(nuevo_nivel)
    return tuple(map(tuple, triangulo))

# Ejercicio 17
def multiplica_matrices(matriz_a, matriz_b):

    # Verificar que las entradas sean matrices
    if not all(isinstance(matriz, list) for matriz in (matriz_a, matriz_b)):
        return "Ambas entradas deben ser matrices representadas como listas de listas."
    # Verificar que ambas matrices sean no vacías
    if not all(matriz_a and matriz_b):
        return "Ambas matrices deben contener elementos."
    # Verificar que la cantidad de columnas de la primera matriz sea igual a la cantidad de filas de la segunda matriz
    if len(matriz_a[0]) != len(matriz_b):
        return "La cantidad de columnas de la primera matriz debe ser igual a la cantidad de filas de la segunda matriz."

    # Inicializar la matriz resultante con ceros
    m, n, p = len(matriz_a), len(matriz_a[0]), len(matriz_b[0])
    matriz_resultante = [[0] * p for _ in range(m)]

    # Calcular los elementos de la matriz resultante
    for i in range(m):
        for j in range(p):
            for k in range(n):
                matriz_resultante[i][j] += matriz_a[i][k] * matriz_b[k][j]

    return matriz_resultante

# Ejercicio 18
def lista_cercanos(matriz):
    if not isinstance(matriz, list) or not all(isinstance(fila, list) and len(fila) == len(matriz[0]) for fila in matriz) or len(matriz) < 2 or len(matriz[0]) < 2:
        return "Error: la matriz debe ser una lista de listas de tamaño m x n (m y n >= 2)"
    resultados = []
    #recorrec cada lista de la matriz
    for fila in matriz: 
        cercano = None
        distancia = float('inf')
        #recorre los digitos n-1 de la fila
        for i in range(len(fila) - 1): 
            diff = abs(fila[i] - fila[-1])
            # Si la diferencia es menor que la distancia actual, actualizamos las variables
            if diff < distancia:
                cercano = fila[i]
                distancia = diff
            # Si la diferencia es igual a la distancia actual, comparamos los números y actualizamos cercano con el número más pequeño
            elif diff == distancia:
                cercano = min(cercano, fila[i])
        resultados.append((fila[-1], cercano))
    return resultados

# Ejercicio 19
def extrae_diagonal(matriz, diagonal):
    # Validamos que la matriz sea cuadrada
    if len(matriz) != len(matriz[0]):
        return "Error, la matriz que ingreso no es cuadrada"
    
    # Validamos que la diagonal exista
    if diagonal > len(matriz)-1 or diagonal < -len(matriz)+1:
        return "Error la diagonal no existe"
    
    # Obtenemos la diagonal correspondiente al número indicado
    diagonal_values = []
    if diagonal >= 0:
        for i in range(len(matriz) - diagonal):
            diagonal_values.append(matriz[i][i+diagonal])
    else:
        for i in range(len(matriz) + diagonal):
            diagonal_values.append(matriz[i-diagonal][i])
    
    return diagonal_values

# Ejercicio 20
def transpuesta(matriz):
    # Obtener dimensiones de la matriz
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Crear una matriz vacía con las dimensiones intercambiadas
    matriz_transpuesta = [[0 for j in range(filas)] for i in range(columnas)]
    
    # Recorrer la matriz original y asignar los valores a la matriz transpuesta
    for i in range(filas):
        for j in range(columnas):
            matriz_transpuesta[j][i] = matriz[i][j]
    
    return matriz_transpuesta

# Ejercicio 21
def máximos_y_mínimos(matriz):
    # Obtenemos la cantidad de filas y columnas de la matriz
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Inicializamos la lista de resultados
    resultados = []
    
    # Recorremos la matriz
    for i in range(filas):
        for j in range(columnas):
            # Comprobamos si el elemento es el máximo de su fila
            if matriz[i][j] == max(matriz[i]):
                # Comprobamos si también es el mínimo de su columna
                if matriz[i][j] == min([matriz[k][j] for k in range(filas)]):
                    # Añadimos los índices a la lista de resultados
                    resultados.append((i, j))
    
    return resultados

#Ejercicio 22
def estudiantes_y_materias(calificaciones):
    # Construir lista final con información de cada estudiante
    lista_estudiantes = []
    for materia in calificaciones:
        nombre_materia = materia[0]
        for estudiante in materia[1:]:
            carnet, nombre, nota = estudiante
            # Buscar si el estudiante ya está en la lista de estudiantes
            estudiante_encontrado = False
            for est in lista_estudiantes:
                if est[0] == carnet:
                    est[2].append((nombre_materia, nota))
                    estudiante_encontrado = True
                    break
            # Si el estudiante no está en la lista, añadirlo
            if not estudiante_encontrado:
                lista_estudiantes.append([carnet, nombre, [(nombre_materia, nota)]])
    
    return lista_estudiantes

#Programa numero 23
def mcd(numeros):
    if not isinstance(numeros, list) or not all(isinstance(numero, int) and numero >= 1 for numero in numeros):
        return "Error: la entrada debe ser una lista de números naturales"
    # Paso 1: obtener los divisores de cada número
    divisores = []
    for n in numeros:
        divisores_n = []
        for i in range(1, n+1):
            if n % i == 0:
                divisores_n.append(i)
        divisores.append(divisores_n)
    print("Paso 1: Divisores de cada número")
    print(divisores)
    
    # Paso 2: obtener los divisores comunes
    divisores_comunes = []
    for d in divisores[0]:
        divisor_encontrado = True
        for otros_divisores in divisores[1:]:
            if d not in otros_divisores:
                divisor_encontrado = False
                break
        if divisor_encontrado:
            divisores_comunes.append(d)
    print("Paso 2: Divisores en común")
    print(divisores_comunes)
    
    # Paso 3: obtener el máximo común divisor
    mcd = 1
    for d in divisores_comunes:
        es_divisor_de_todos = True
        for n in numeros:
            if n % d != 0:
                es_divisor_de_todos = False
                break
        if es_divisor_de_todos and d > mcd:
            mcd = d
    print("Paso 3: Máximo común divisor", mcd)
    return mcd

#Programa numero 24
def triangulo_simetrico(matriz, codigo):
    n = len(matriz)
    #verificacion de datos de entrada
    if n != len(matriz[0]):
        return "La matriz debe ser cuadrada"
    if codigo not in ["A", "D"]:
        return "Código de triángulo inválido"
    
    triangulo = []
    #creacion del triangulo A o B depende de la eleccion del usuario
    for i in range(n):
        fila = []
        for j in range(n):
            if codigo == "A" and j > i:
                fila.append(matriz[i][j])
            elif codigo == "D" and j < i:
                fila.append(matriz[i][j])
        if fila:
            triangulo.append(tuple(fila))
    return tuple(triangulo)