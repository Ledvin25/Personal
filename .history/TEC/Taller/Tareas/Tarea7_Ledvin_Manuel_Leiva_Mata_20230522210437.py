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
        suma = 0