'''
Practica 22
Programa que permita obtener los números primos inferiores a un número entero positivo N proporcionado por el usuario, 
en donde N es un número entero positivo, el cual ingresa el usuario, esto es si N = 20, 
el programa debe desplegar la lista 2,3,5,7,11,13,17,19. El programa debe seguir el algoritmo propuesto por el matemático 
S.P. Sundaram: La criba de Sundaram
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

print("Numeros primos por la Cibra de Sundaram")

while True:
        user = input("Dame un numero entero y positivo:\n")
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

i=1
j=i
numeros=[i for i in range(1,n+1)]
primos=[]
for i in range(1, (n-j)//(1+2*j)):
        for j in range(1, (n-i)//(1+2*i)):
            numeroe = i + j + (2*i*j)
            if numeroe in numeros:
                numeros.remove(numeroe)
        j = i + 1

for i in numeros:
    primo = (2*i) + 1
    primos.append(primo)

primostr= [str(a) for a in primos]

print(f"Los {n} numeros primos por la Criba de Sudaram =", ' , '. join(primostr))