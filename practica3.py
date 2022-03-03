'''
Practica 3
Programa que indique si al ingresar un año como un número entero positivo N mayor a cero, este sea
o no bisiesto. Un año es bisiesto si es múltiplo de 4, exceptuando los múltiplos de 100, 
que sólo son bisiestos cuando son múltiplos además de 400, por ejemplo el año 1900 no fue bisiesto,
pero el año 2000 si lo es
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

print("Año bisiesto o no bisiesto.")

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

if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
	print(f"El año {n} es bisiesto")
else:
	print(f"El año {n} no es bisiesto")

