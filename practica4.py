'''
Practica 4
Escribir un programa que pida al usuario un número entero y muestre en pantalla 
un triángulo como el siguiente (número ingresado 5):
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

print("Triangulo de numeros impare")

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

triangulo=[]

for i in range(1,n+1):
    fila = []
    for j in range(0,i):
        fila.insert(0,2*j+1)
    filastr=[str(a) for a in fila]
    print(' '. join(filastr))
    triangulo.append(fila)

