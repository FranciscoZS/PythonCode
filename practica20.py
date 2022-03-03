'''
Practica 20
Desarrollar un programa que permita el cálculo del valor de π/4 por medio de una fracción continua Fracción continua
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

import math

print("Fracción continua")

while True:
        user = input("Dame un numero entero y positivo sera el numero limite de la fraccion continua:\n")
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

cuadrados=[]

for i in range(1,n+1):
        cuadrados.append(i**2)

impares=[i for i in range(1,n*2,2)]

resto=0

for i in range(0,n):
    resto = cuadrados[i] / (impares[i] + resto)

pi4=resto/4

comprosen=math.sin(pi4)

print(f"El valor de pi aproximado es: {pi4}. Y la comprobación con el seno es: {comprosen}")