'''
Practica 1
Programa que indique si al ingresar un número entero positivo N, este es par o impar
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

print("Numero par o Impar")

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

if n % 2 == 0:
    print(f"el numero {n} es par")
else:
    print(f"el numero {n} es impar")