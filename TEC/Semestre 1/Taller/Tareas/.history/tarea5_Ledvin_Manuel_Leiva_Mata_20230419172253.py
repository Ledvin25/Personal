#Tarea 5 - Ledvin Manuel Leiva Mata

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
        for j in range(y):
            matriz

