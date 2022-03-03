'''
Practica 10
Programa que calcule el doble factorial (n!!) de un número entero positivo (Información del doble factorial)
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

print("Doble Factorial")

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

doblefactorial = 1

if n % 2 == 1:
    for i in range(1, n + 1, 2):
            doblefactorial *= i
else:
    for i in range(2, n + 1, 2):
            doblefactorial *= i
            
print(doblefactorial)