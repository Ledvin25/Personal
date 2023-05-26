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
    
def suma_digitos_p(n):
    if isinstance(n, int) and n < 0:
        return -1
    else:
        return suma_digitos(n//10) + n%10

def suma_digitos_c(n, acc=0):
    if isinstance(n, int) and n < 0:
        return -1
    if n == 0:
        return acc
    else:
        return suma_digitos_c(n//10, acc+n%10)
    
# Ejercicio 2

obtiene_divisores():