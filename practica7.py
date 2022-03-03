'''
Practica 7
Programa que permita ingresar un intervalo mediante dos números enteros y positivos [a,b] 
y que obtenga tanto la suma como el producto de todos los números intermedios,
 incluyendo a & b (el programa debe verificar que el intervalo ingresado sea válido)
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

print("Suma y multiplicacion de un intervalo")

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

print(f"su intervalo es [{n},{n1}]")

numeros=[]
for i in range(n,n1+1):
    numeros.append(i)

suma = 0

for elemento in numeros:
    suma += elemento

multi = 1

for elemento in numeros:
     multi *= elemento

print(f"La suma del intervalo es: {suma} \nY la multiplicación es: {multi}")