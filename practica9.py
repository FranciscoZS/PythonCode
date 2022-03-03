'''
Practica 9
Programa que permita sumar los dígitos de un número entero positivo ingresado por el usuario,
esto es si se ingresa N = 1521, el resultado a mostrar es: Suma = 1 + 5 + 2 + 1 = 9
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

print("Suma de los digitos de un numero")

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

nstr=str(n)
m=len(nstr)
numero=[]

for i in range(0,m):
    numero.append(int(nstr[i]))
    
suma = 0

numerostr= [str(a) for a in numero]

for elemento in numero:
    suma += elemento
print(f"La suma de los digitos del numero que nos ingresates es: {n}.\nSuma =", ' + '. join(numerostr), f"= {suma}")