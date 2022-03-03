'''
Practica 8
Programa que permita invertir un número entero positivo ingresado por el usuario, esto es que si se ingresa N = 5243, 
el programa debe mostrar 3425
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

print("Invertir un numero")

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
inv = []

for i in range(0,m):
        inv.append(nstr[m-1])
        m-=1
print(f"El numero que ingresaste fue: {n}.\nSu inverso es: ",''. join(inv))