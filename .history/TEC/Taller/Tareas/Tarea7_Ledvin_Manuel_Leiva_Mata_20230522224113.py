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
    
def obtiene_divisores_c(n):
    if not isinstance(n, int) and n >= 1:
        return []
    else:
        return obtiene_divisores_c_aux(n,1, [])
    
def obtiene_divisores_c_aux(n, i, lista):
    if i == 0:
        return lista
    elif n%i == 0:
        lista.append(i)
    return obtiene_divisores_c_aux(n,i+1,lista)
        
    

print(obtiene_divisores_c(24))