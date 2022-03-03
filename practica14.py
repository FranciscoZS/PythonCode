'''
Practica 14
Programa que permita obtener una cantidad N de números pseudoaleatorios (donde N es un número entero, mayor a 0) 
utilizando para ello el método/algoritmo de generación de números congruencial.
En el siguiente documento se encuentra información junto con ejemplos para probar el algoritmo --Documento--
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

print("Generacion de numeros congruencial")

while True:
        user = input("Dame un numero entero y positivo que sera la cantidad de numeros a generar:\n")
        try:
            N= int(user)
        except:
            print("¡¡Debe ser numero entero y positivo!! \n")
        else:
            if N % 1 == 0 and N >0 :
                break
            elif N == 0:
                print("el zero es la mitad de la recta no jala")
            else:
                print("¡¡Debe ser entero y positivo!!")

while True:
        user = input("Dame un numero entero y positivo para el multiplicador a:\n")
        try:
            a= int(user)
        except:
            print("¡¡Debe ser numero entero y positivo!! \n")
        else:
            if a % 1 == 0 and a >0 :
                break
            elif a == 0:
                print("el zero es la mitad de la recta no jala")
            else:
                print("¡¡Debe ser entero y positivo!!")

while True:
        user = input("Dame un numero entero y positivo para el sesgo b (puede ser cero):\n")
        try:
            b= int(user)
        except:
            print("¡¡Debe ser numero entero y positivo!! \n")
        else:
            if b % 1 == 0 and b >= 0:
                break
            else:
                print("¡¡Debe ser entero y positivo!!")

while True:
        user = input("Dame un numero entero y positivo para el módulo m:\n")
        try:
            m= int(user)
        except:
            print("¡¡Debe ser numero entero y positivo!! \n")
        else:
            if m % 1 == 0 and m >0 :
                break
            elif m == 0:
                print("el zero es la mitad de la recta no jala")
            else:
                print("¡¡Debe ser entero y positivo!!")

while True:
        user = input("Dame un numero entero y positivo como numero semilla X0:\n")
        try:
            x0= int(user)
        except:
            print("¡¡Debe ser numero entero y positivo!! \n")
        else:
            if x0 % 1 == 0 and x0 >0 :
                break
            elif x0 == 0:
                print("el zero es la mitad de la recta no jala")
            else:
                print("¡¡Debe ser entero y positivo!!")

n=0
u=[]

while n<=N-1:
    u.append(x0/m)
    x0=(a*x0+b)%m
    n +=1

ustr=[str(a) for a in u]

print(f"Los {n} numeros generados por el algoritmo de generación de números congruencial es:", ', ' . join(ustr))
