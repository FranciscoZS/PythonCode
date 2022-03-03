'''
Practica 30
Generar un programa que permita al usuario ingresar una lista de entre 2 y 6 números 
enteros y mostrar todas las posibles permutaciones de la lista
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

from itertools import permutations

print("Permutaciones de una lista")

def number():
    while True:
        user = input("Dame un numero entero:\n")
        try:
            n= int(user)
            break
        except:
            print("¡¡Debe ser numero entero!! \n")
    return n

listan=[]

while True:
    a=number()
    listan.append(a)
    count=len(listan)
    if count==1:
        print("Agrege otro numero, deben ser minimo 2 y un maximo de 6")
        a=number()
        listan.append(a)
    if count==6:
        break
    while True:
        option=input("Desea ingresar otro numero mas, recuerda que deben ser maximo 6.\nsi [s] o no [n]:\n")
        if option=='s':
            break
        elif option=='n':
            break
        else:
            print("opcion invalida")
    if option=='n':
            break

print(f"Tu lista es: {listan}")

permutaciones=list(permutations(listan))
index=len(permutaciones)
permutacionestr=[str(a) for a in permutaciones]

print(f"El total de permitaciones de tu lista es {index} y son:")
print("\n".join(permutacionestr))
