'''
Practica 11
Programa que permita calcular el dígito de control del código de barras EAN-8, 
las instrucciones para generarlo se encuentran en: Instrucciones disponibles
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

print("Dígito de control del código de barras EAN-8")

while True:
    while True:
        user = input("Dame un numero entero y positivo de 8 digitos del 1 al 8 y sin repetir:\n")
        if user.count('0') == 0 and user.count('1')==1 and user.count('2') == 1 and user.count('3') == 1 and user.count('4') == 1 and user.count('5') == 1 and user.count('6') == 1 and user.count('7') == 1 and user.count('8') == 1 and len(user) == 8:
            break
        else:
            print("¡¡Debe ser numero entero y positivo de 8 digitos del 1 al 8 y sin repetir!! \n")
    try:
        n= int(user)
    except:
        print("¡¡Debe ser numero entero y positivo de 8 digitos del 1 al 8 y sin repetir!! \n")
    else:
        if n % 1 == 0 and n >0 :
            break
        elif n == 0:
            print("el zero es la mitad de la recta no jala")
        else:
            print("¡¡Debe ser entero y positivo de 8 digitos del 1 al 8 y sin repetir!!")

nstr=str(n)
numero = 0
sumapar = 0
sumaimpar = 0


for i, val in enumerate(nstr):
    numero = int(val)
    if i % 2 != 0:
        sumapar += numero
    else:
        sumaimpar += numero
    
sumapar *= 3
numerocontrol = 10 - ((sumaimpar + sumapar) % 10)

print(f"Tu codigo de barras que ingresaste fue: {n}.\nSu numero de control es: {numerocontrol}.\nTu codigo de barras completo es: {n} {numerocontrol}")