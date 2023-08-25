#Tarea 4 - Ledvin Manuel Leiva Mata
#Ejercicio 1

def factorial(n):

    i = 1 #contador
    x = 1

    while i <= n:
        x = x * i #x variable a retornar
        i += 1

    return x

#Ejericio 2

def calificacion(grade):
    #Evalua los rangos para ver en cual se encuentra la nota
    if 0 <= grade <= 100:
        if grade >= 90:
            return "A - Excelente (Aprobado)"
        elif grade >= 80:
            return "B - Bien (Aprobado)"
        elif grade >= 70:
            return "C - Suficiente (Aprobado)"
        elif grade >= 50:
            return "D - Deficiente (Reprobado)"
        else:
            return "F - Muy deficiente (Reprobado)"

    else:
        return("ERROR: NOTA DEBE ESTAR ENTRE 0 Y 100") #retorna error en caso de haberlo

#Ejercicio 3

def sumatoria(m,n):

    sum_m = 0 # variable de la sumatoria de m se inicializa

    if m > 1: # en caso de que el inicio sea mayor que uno se le da el valor inferior a m
        sum_m = (m-1)*m/2

    sum_n = n*(n+1)/2 # se realiza la sumatoria en n

    return int(sum_n - sum_m) # se retorna el valor de la resta el cual es la sumatoria de los rangos solicitados

#Ejercicio 4

def suma_multiplica_digitos(n):

    if n >= 0:

        x = s = 0 # x digito, s suma
        m = 1 # m multiplicacion

        while n > 0:

            x = n%10

            m = m * x #multiplicacion
            s = s + x #suma

            n = n//10

        return s,m

#ejercicio 5

def contar_pares_impares(n):

    i = p = 0 #pares e impares
    while n > 0:

        x = n%10

        if x%2 == 0:
            p += 1
        else:
            i += 1
        n = n // 10

    return p, i

# ejercicio 6

def pares_impares(n):

    i = p = p_par = p_impar = 0 #pares e impares y sus potencias.

    while n > 0:

        x = n%10

        if x%2 == 0:
            p += x*(10**p_par)
            p_par += 1
        else:
            i += x*(10**p_impar)
            p_impar += 1

        n = n // 10

    if p_par == 0:
        p = "No hay"
    if p_impar == 0:
        i = "No hay"

    return p, i

#ejercicio 7

#7.1 recargas

def recargas(rec):

    monto = int(input("Monto de recarga: "))
    rec += 1

    return rec

#7.2 Consumos

def consumos(rec, cons):

    monto = int(input("Monto de consumo: "))

    if rec - cons != 0:
        cons += 1
    else:
        print("No hay saldo suficiente")

    return cons

#7.3 Estado de cuenta

def estado_Cuenta(rec, cons):
    print("\nTotal de recargas: " , rec, "\nTotal de consumos: " , cons , "\nSALDO DE LA CUENTA DEL TELEFONO: " , rec - cons)

def cuenta_celular():

    total_rec = total_cons = 0
    op = 1

    while op != 0:
        print("\n1. Recargas \n2. Consumos \n3. Estado de la cuenta \n0. Fin")

        op = int(input("\nSelecione una opcion: "))

        if op == 1:
            total_rec = recargas(total_rec)
        elif op == 2:
            total_cons =consumos(total_rec, total_cons)
        elif op == 3:
            estado_Cuenta(total_rec, total_cons)

#Ejercicio 8

def encriptar(e, n):

    #e encriptador, n numero de entrada
    exit_num = e #variable de salida a retornar
    pow = 1 #pow potencia

    while n > 0:

        x = n%10 # x variable para el digito

        exit_num += ((x + e)%10)*10**pow
        pow += 1

        n = n//10

    return exit_num

#Ejercicio 9

def analizar_notas_admision():

    nota = max_nota = promedio = validas = invalidas = i = 0 # i contador
    min_nota = 800

    while nota >= 0:
        nota = int(input("Digite una nota entre 0 y 800: "))

        #nota mas alta
        if nota > max_nota and nota < 800:
            max_nota = nota

        #nota mas baja
        if nota < min_nota and nota >= 0 :
            min_nota = nota

        #notas validas e invalidas y suma promedio
        if nota > 800:
            invalidas += 1
        elif nota >= 0:
            promedio += nota
            validas += 1

    promedio = promedio/validas

    print("\nNota mas alta: ", max_nota, "\nNota mas baja: ", min_nota, "\nNota promedio: ", promedio, "\nCantidad de notas validas (entre 0 y 800): ", validas, "\nCantidad de notas invalidas (>800)", invalidas)

# Ejercicio 10

def combinatoria_1(n,x):
    #n y x variables dadas por el ejercicio
    if x < 0 or x > n:
        return 0
    elif x == 0 or x == n:
        return 1
    else:

        k = 1
        i = n
        j = 1

        while i >= n - x + 1:
            k *= i
            i -= 1

        while j <= x:
            k //= j
            j += 1

        return int(k)

def combinatoria_2(n,x):
    #n y x variables dadas por el ejercicio

    if x < 0 or x > n:
        return 0
    elif x == 0 or x == n:
        return 1
    else:
        return int((factorial(n))/(factorial(x)*factorial(n-x))) #funcion reutilizada

# ejercicio 11

def fibonacci(n):

    i = 2 #contador
    x = 0 #variable 1
    y = 1 #variable 2

    while i <= n:
        z = x + y
        x = y
        y = z
        i += 1

    return x

# ejercicio 12

def numero_al_reves(n):

    result= 0 #potencia
    pow = -1 #potencia a la -1 para comenzar a sumar los numeros del mas grande hasta el mas pequeño
    n1 = n2 = n

    while n1 > 0: #crear la potencia con el valor del numero mas alto
        m = n2%10
        n1 = n1//10
        pow += 1

    while n2 > 0: # acomodar los numeros al reves desde el mas grande al mas pequeño
        m = n2%10
        n2 = n2//10
        result += m*10**pow
        pow -= 1

    return result

#ejercicio 13

def palindromo(n):

    if numero_al_reves(n) == n: #evaulacion de palindromo
        return True
    else:
        return False

#ejercicio 14

def imprimir_palindromos(n):
    if isinstance(n,int) and n >= 1:

        i = pal = 0 #inicia contador y variable para palindromos

        while i < n: #imprimer todos los numeros que cumplan el ser palindromo
            if palindromo(pal):
                print(pal)
                i += 1
            pal += 1

    else:
        print("Los datos proporcionados son invalidos, tiene que ser un numero natural")

#ejercicio 15

def es_numero_bonito(n):

    n1 = n
    n2 = 3*n + 11
    x = y = 0 # x variable de digitos, y variable de digitos

    while n1 > 0: # suma digitos del numero ingresado
        x += n1%10
        n1 = n1 // 10

    while n2 > 0: # suma digitos de la expresion dada
        y += n2%10
        n2 = n2 // 10


    if x == y:
        return True
    else:
        return False

#ejercicio 16

def lista_numeros_bonitos(n):
    i = y = 0 # i contador - y numero a evaluar
    while i < n:

        if es_numero_bonito(y): # reutiliza la funcion e imprime los que devuelven un True
            print(y)
            i+=1
        y+=1

#Ejercicio 17

def igualdad(a,b):

    # Si a o b son cero, devuelve False inmediatamente
    if a == 0 or b == 0:
        return False

    d1 = d2 = 0
    igual = True
    a1 = a

    while a1 > 0 and igual:
        d1 = a1%10
        a1 = a1//10
        b1 = b

        while b1 > 0 :

            d2 = b1%10
            b1 = b1//10
            # Si d1 es igual a d2, se establece "igual" como True y rompemos el bucle interno
            if d1 == d2:
                igual = True
                break
            # Si d1 no es igual a d2, se establece "igual" como False
            else:
                igual = False

    while b > 0 and igual:
        d1 = b%10
        b = b//10
        a1 = a

        while a1 > 0 :

            d2 = a1%10
            a1= a1//10

            # Si d1 es igual a d2, se establece "igual" como True y rompemos el bucle interno
            if d1 == d2:
                igual = True
                break
            # Si d1 no es igual a d2, se establece "igual" como False
            else:
                igual = False

    return igual # Devuelve "igual", que es True si ambos números contienen los mismos dígitos y False si no lo hacen

# Ejercicio 18

def lista_numeros_perfectos(n):
    i = num = suma_divisores = 0
    while i < n:
            num += 1
            j = 1
            suma_divisores = 0
            while j < num:
                if num % j == 0:
                    suma_divisores += j
                j += 1
            if suma_divisores == num:
                print(num)
                i += 1

# Ejercicio 19

def base10a258(a,b):

    if isinstance(a, int) and isinstance(b, int) and a >= 0 and b >= 0:
        if b == 2 or b == 5 or b == 8:
            result = pow = 0

            while a%10 != 0 or pow == 0:

                result += (a%b)*10**pow
                pow += 1
                a = a//b

            return result
        else: return "La base final debe ser 2, 5 o 8"
    else: return"Los parametros indicados son incorrectos, revise e intentelo de nuevo"

# Ejercicio 20

def primo(n):
    i = 2
    while i <= n**(1/2):

        if n % i == 0:
            return False
        else: i+=1
    else: return True

# Ejercicio 21

def primos_gemelos():

    inicio = int(input("Inicio del intervalo: "))
    fin = int(input("Fin del intervalo: "))

    print("Primos gemelos: ")

    while inicio < fin:

        if primo(inicio+2) and primo(inicio) and inicio+2 - inicio == 2:
            print(inicio , " y " , inicio+2)

        inicio+=1

# Ejercicio 22

def buscar_biprimos(a,b):

    a1 = biprimos = 0
    i = a

    while i <= b:
        fp1 = 2
        fp2 = i // fp1
        while fp1 <= fp2:
            if primo(fp1) and primo(fp2) and fp1*fp2==i:
                print(i, " = ", fp1, " X ", fp2)
                biprimos += 1
                break
            fp1 += 1
            fp2 = i//fp1
        i += 1
    print("Total de biprimos: ", biprimos)

# Ejercicio 23

def factores_primos(n):

    i=2
    residuo = n

    while residuo > 1:
        if primo(i) and residuo % i == 0:
            print(i)
            residuo = residuo // i
            i = 1
        i+=1

# Ejercicio 24

def agrupar_dígitos(n):

    if isinstance(n, int) and n > 0:

        d1 = 0
        n1 = n2 = n
        r = i = i2 = i3 = 0
        result = 0

        while n1 > 0:
            if not igualdad(n1, result):
                d1 = n1%10
                n1 = n1//10
                n2 = n
                while n2 > 0:
                    if n2%10 == d1:
                        i+=1
                    n2 = n2//10
                i2 = i
                if i3 != 0:
                    r = i3
                i3 = i
                while i2 > r:
                    result += d1*10**(i2-1)
                    i2 -= 1
            else:
                break

    return result

# Ejercicio 25

def determinar_numeros_amistosos(n,m):
    if isinstance(n, int) and isinstance(m, int) and n >= 2 and m >=2:
        div1 = div2 = 0
        i1 = i2 = 1
        n1 = n
        m1 = m

        while i1 < n:
            if n%i1 == 0:
                n1 = n1 //i1
                div1 += i1
            i1+= 1
        while i2 < m:
            if m%i2 == 0:
                m1 = m1 //i2
                div2 += i2
            i2+= 1

        if div1 == m and div2 == n:
            return True
        else: return False

    else: return "Los valores indicados no son validos, por favor compruebe e intente de nuevo"

# Ejercicio 26
def contar_apariciones(a,b):

    #variables necesarias
    a1 = a
    i = pow = 0 #i contador

    #longitud de a para crear potencia
    while a1 > 0:
        a1 = a1//10
        pow += 1

    #loop para generar resultado
    while b > 0:
        if b%10**pow == a: #solamente el contador si los ultimos digitos a la potencia son iguales a "a"
            b = b//10**pow
            i +=1
        else:
            b = b//10 # le quita la unidad al numero para ver si esta esta estorbando al verificar el numero

    return i


# Ejercicio 27

def numeros_abundantes(a,b):

    num = a

    while num <= b:
        sum = 0
        i = 1
        while i <= num:
            if num%i==0:
                sum += i
            i+=1
        if sum > num*2:
            print(num)
        num += 1


# Ejercicio 28

def determinar_orden(n):
    i = 0
    d2 = n%10
    result = result1 = 0

    while n > 0:
        d1 = n%10
        n = n//10

        if d1 > d2:
            result = 2
        elif d1 < d2:
            result = 1

        if result != result1 and result1 != 0:
            result = 0
            break
        d2 = d1
        result1 = result

    return result

# Ejercicio 29

def analizar_tipo_de_cambio():

    i = 0
    s2 = 0

    n = int(input("Cantidad de tipos de cambio a leer: "))

    while i+1 < n:

        if i == 0:
            print("Tipo de cambio ", i+1, ":")
            c1 = int(input())

        print("Tipo de cambio ", i+2, ":")
        c2 = int(input())

        i += 1

        if c2 - c1 > 0:
            print("Diferencia con tipo de cambio anterior: aumento de ", c2-c1)
            s1 = c2-c1
        elif c2 - c1 < 0:
            print("Diferencia con tipo de cambio anterior: disminución de ", c1-c2)
            s1 = c1-c2

        if s1 > s2:
            max_diff = s1
            max_diff_i = i
        elif s1 < 0 and abs(s1) > s2:
            min_diff = s1
            min_diff_i = i
        s2 = s1
        c1 = c2


    print("Resultados finales:")
    print("Mayor diferencia: ", max_diff)
    if c2 - max_diff < c2:
        print("Entre los tipos de cambio:", c2, "y", c2 + max_diff)
    else:
        print("Entre los tipos de cambio:", c2 - max_diff, "y", c2)

# Ejercicio 30

def reemplazar_numero(a,b,c):
    #Validar restricciones
    if isinstance(a, int) and isinstance(b, int) and isinstance(c, int) and a >= 0 and b >= 0 and c >= 0:

        #Creacion de variables necesarias
        pow = result = lenc = 0
        pow2 = 1
        a1 = a
        c1 = c

        #medir la longitud del numero a para crear la potencia a multiplicar
        while a1 > 0:
            a1 = a1//10
            pow += 1
        #medir la longitud de c para sumar lo necesario a la potencia a multiplicar
        while c1 > 0:
            c1 = c1//10
            lenc += 1

        #Crear el numero a trabajar al reves para leerlo tecnicamente de izquierda a derecha
        b1 = numero_al_reves(b)

        #Loop para la creacion del resultado
        while b1 > 0:
            if b1%10**pow == numero_al_reves(a): # valida si el numero a se encuentre en los proximos digitos de b, y como como el numero se esta trabajando al reves, todos los digitos deben trabajarse al reves
                b1 = b1//10**pow
                result += numero_al_reves(c)*10**(pow2-1) #como el numero se esta trabajando al reves, todos los digitos deben trabajarse al reves
                pow2 += lenc # se aumenta la potencia segun la longitud de c para que los 0 calcen al sumar
            else: # le quita el ultimo digito para comprobar nuevamente si ese era el que estaba estorbando y le suma 1 a la potencia
                result += (b1%10)*10**(pow2-1)
                b1 = b1 // 10
                pow2 += 1
        if c == 0: # si c es igual a 0 al numero originalmente estar al reves comenzaria con 0, como le damos la vuelta solo se le agrega al final con aritmetica
            result = numero_al_reves(result) * 10**(lenc+1)
        else: # en caso de ser diferente de 0, se devuelve el resultado al reves para devolverlo a su forma original
            result = numero_al_reves(result)
        return result
    else: return"Valores invalidos, por favor compruebe e intente de nuevo."