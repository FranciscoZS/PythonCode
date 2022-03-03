'''
Practica 15
Programa que obtenga el Máximo Común Divisor (MCD) y el mínimo común múltiplo (mcm) de un par de números enteros positivos. 
(Existe un algoritmo ya establecido para este caso, se le conoce como algoritmo de Euclídes)
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

print("Máximo Común Divisor y Mínimo Común Múltiplo")

while True:
        user = input("Dame un numero entero y positivo:\n")
        try:
            n= int(user)
        except:
            print("¡¡Debe ser numero entero y positivo!! \n")
        else:
            if n % 1 == 0 and n >=0 :
                break
            else:
                print("¡¡Debe ser entero y positivo!!")

while True:
        user = input("Dame otro numero entero y positivo:\n")
        try:
            m= int(user)
        except:
            print("¡¡Debe ser numero entero y positivo!! \n")
        else:
            if m % 1 == 0 and m >=0 :
                break
            else:
                print("¡¡Debe ser entero y positivo!!")

p = 1

if ((n == 0) & (m == 0)):
        mcd = 0
elif n == 0:
        mcd = m
elif m == 0:
        mcd = n
else:
    if n < m:
        n, m = m, n     
    n1 = n
    m1 = m

    while p != 0:
        p = n1 % m1
        mcd, n1, m1 = m1, m1, p

try:
    mcm = (n * m)//mcd
except:
    print("No existe un Minimo comun multiplo para un Maximo comun Divisor de 0")
    mcm="N/A"

print(f"Tus numeros son {n} y {m}.\nEl máximo común divisor (MCD) es: {mcd}.\nY el mínimo común múltiplo (mcm) es: {mcm}")