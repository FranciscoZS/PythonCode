'''
Practica 16
Programa que permita obtener la lista de números narcisistas que existan en un intervalo dado por el usuario 
(verificar que el intervalo sea válido con números enteros y positivos)
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

print("Lista de números narcisistas")

while True:
        user = input("Dame un numero entero y positivo :\n")
        try:
            n= int(user)
        except:
            print("¡¡Debe ser numero entero y positivo!! \n")
        else:
            if n % 1 == 0 and n >0 :
                break
            elif n == 0:
                print("el zero es la mitad de la recta no jala")
            else:
                print("¡¡Debe ser entero y positivo!!")

while True:
        user = input("Dame otro numero entero y positivo :\n")
        try:
            n1= int(user)
        except:
            print("¡¡Debe ser numero entero y positivo!! \n")
        else:
            if n1 % 1 == 0 and n1 >0 and n1>n:
                break
            elif n1 == 0:
                print("el zero es la mitad de la recta no jala")
            elif n1<n:
                print("el segundo numero debe ser mayor al primero crack")
            else:
                print("¡¡Debe ser entero y positivo!!")

print(f"Su intervalo es [{n},{n1}]")

narcisos=[]
def nar(n):
    nstr=str(n)
    m=len(nstr)
    numero=[]
    
    for i in range(0,m):
        numero.append(int(nstr[i]))
        
    suma = 0
    
    for elemento in numero:
        suma += elemento**m
    
    if suma == n or round(suma**(1/m)) == n:
        v=n
    else:
        v=0
    return v

for i in range(n,n1+1):
    a=nar(i)
    narcisos.append(a)
    try:
        narcisos.remove(0)
    except:
        a=0

narcisosstr=[str(a) for a in narcisos]

print(f"Los {n} numeros narcisos son:", ', ' . join(narcisosstr))