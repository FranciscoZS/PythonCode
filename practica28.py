'''
Practica 28
Desarrollar un programa que permita el ingreso de números por parte del usuario 
(dejar que ingrese un número indefinido de números y 
en cada uno de ellos preguntar si se desea agregar más o ya es el último a agregar), 
guardarlos en una lista y mostrar en pantalla, el número de datos ingresados, el promedio, y la desviación estándar de los datos
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

import math

print("Promedio, Numero de datos y desviación estandar")

def number():
    while True:
            user = input("Dame un numero:\n")
            try:
                n= float(user)
                break
            except:
                print("¡¡Debe ser numero \n")
    return n

listan=[]
listas=[]

while True:
    a=number()
    listan.append(a)
    b=str(a)
    listas.append(b)
    while True:
        option=input("Desea ingresar otro dato mas si [s] o no [n]:\n")
        if option=='s':
            break
        elif option=='n':
            break
        else:
            print("opcion invalida")
    if option=='n':
            break

ndatos=len(listas)
promedio = sum(listan) / len(listan)
varianza = sum((l-promedio)**2 for l in listan) / len(listan)
desviacion = math.sqrt(varianza)

print(f"Tu lista esta conformado por {ndatos} datos. Los daos que conforman tu lista son:",", ".join(listas), f"\nDe estos datos su promedio es: {promedio}.\nY su desviación estándar es: {desviacion}")





