#Made by Ledvin M Leiva M
#Tarea 2, taller de programacion

def calificacion(grade):
    
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
        return("ERROR: NOTA DEBE ESTAR ENTRE 0 Y 100")

def pares_impares(num):
    
    par = impar = 0

    if 0 <= num < 10000:
        
        digito1 = int(num % 10)
        digito2 = int(((num % 100) - digito1)/10)
        digito3 = int(((num % 1000) - (num % 100))/100)
        digito4 = int((num - (num % 1000))/1000)

        #return digito1, digito2, digito3, digito4

        #digito 1
        if (digito1 % 2) == 0:
            par = digito1
        else:
            impar = digito1
        
        #digito2
        if (digito2 % 2) == 0:
            if par < 10 and par == 0:
                par = digito2
            else: 
                par += digito2*10
        else:
            if impar < 10 and impar == 0:
                impar = digito2
            else: 
                impar += digito2*10
        
        #digito3

        if (digito3 % 2) == 0:
            if 10 < par < 100:
                par += digito3*100
            elif par < 10 and par != 0:
                par += digito3*10
            else:
                par = digito3
        else:
            if 10 < impar < 100:
                impar += digito3*100
            elif impar < 10 and impar != 0:
                impar += digito3*10
            else:
                impar = digito3

        #digito 4

        if(digito4 % 2) == 0:
            if par > 100:
                par += digito4*1000
            elif 10 < par < 100:
                par += digito4*100
            elif par < 10 and par != 0:
                par += digito4*10
            else:
                par = digito4
        else:
            if impar > 100:
                impar += digito4*1000
            elif 10 < impar < 100:
                impar += digito4*100
            elif impar < 10 and impar != 0:
                impar += digito4*10
            else:
                impar = digito4

        if par == 0:
            par = -1
        if impar == 0:
            impar = -1

        return (par, impar)

    else:
        return "ERROR: DEBE SER UN NUMERO NATURAL DE 4 DIGITOS"
    
def bisiesto(year):
    
    if year >= 1800 and year%4 == 0:
        return True
    else:
        False
        

def valida_fecha(date):

    year = int(date%10000)
    month = int((date%1000000 - year)/10000)
    day = int((date - date%1000000)/1000000)

    if year >= 1800 and 1<= month <= 12 and 1<= day <= 31:
        if (month == 2 and bisiesto(year) and day <= 29) or (month == 2 and not bisiesto(year) and day <= 28):
            return True
        elif (month + (month // 8))% 2 + 30 == 31 and 1<= day <= 31 and month != 2:
            return True
        elif (month + (month // 8))% 2 + 30 == 30 and 1<= day <= 30 and month != 2:
            return True
        else: 
            return False
    

def paridad(num1, num2):

    par1 = par2 = False

    if num1 % 2 == 0:
        par1 = True
    if num2 % 2 == 0:
        par2 = True
    
    if par1 and par2:
        return "Paridad par"
    elif not par1 and not par2:
        return "Paridad impar"
    else:
        return "DIFERENTE PARIDAD"
    
def doble_de_iImpar(n):

    if n%2 == 0 and (n//2)%2 == 1:
        return True
    else:
        return False
    
def cuenta_bancaria(actbalance, operation, opbalance):

    if actbalance >= 0 and opbalance > 0 and opbalance%1000 == 0 and 1 <= operation <= 2:
        if operation == 1:
            return actbalance + opbalance
        elif operation == 2 and opbalance <= actbalance:
            return actbalance - opbalance
        else: 
            return False
    else: 
        return False


def pago_celular(callmin, msgsent, netplan):
    
    amount = 2750

    if callmin >= 0 and msgsent >= 0 and 0<= netplan <= 3:

        if 60 < callmin <= 120:
            amount += (callmin - 60)*50
        elif callmin > 120:
            amount += (callmin - 120)*35 + 50

        amount += msgsent*3

        if netplan == 1:
            amount += 12000
        elif netplan == 2:
            amount += 15000
        elif netplan == 3:
            amount += 25000
        
        amount += amount*0.13 + 200
    else:
        return "Los valores ingresados no son permitidos."
    
    return amount
    
def nombre_dia(date):

    if valida_fecha(date):
        year = int(date%10000)
        month = int((date%1000000 - year)/10000)
        day = int((date - date%1000000)/1000000)
        
        if month == 1 or month == 2:
            month += 12
            year -= 1
        
        k = day
        m = month
        D = year % 100
        C = year // 100
        f = (k + 13*(m+1)//5 + D + D//4 + C//4 - 2*C) % 7

        if f == 0:
            return "Sabado"
        elif f == 1:
            return "Domingo"
        elif f == 2:
            return "Lunes"
        elif f == 3:
            return "Martes"
        elif f == 4:
            return "Miercoles"
        elif f == 5:
            return "Jueves"
        elif f == 6:
            return "Viernes"

    else: return False

def al_reves(n):

    u = n%10
    d = ((n%100)-u)/10
    m = (n-(n%1000))/1000
    c = -(m*10 - ((n-(n%100))/100))

    num = u * 1000 + d * 100 + c *10 + m

    return int(num)

def palindromo(x):
    
    if x == al_reves(x):
        return True
    else:
        return False
