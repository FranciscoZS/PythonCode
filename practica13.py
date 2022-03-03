'''
Practica 13
Programa que permita Imprimir los N números de la Serie de Padovan , 
donde N es un número entero positivo que el usuario debe ingresar para obtener los valores de la serie
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

print("Serie de Padovan")

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

padovan = []

for i in range(0,n):
    
    if i == 0:
        padovan.append(1)
    elif i==1:
        padovan.append(1)
    elif i==2:
        padovan.append(1)
    elif i>=3:
        j=(i-2)
        m=(i-3)
        indice=padovan[j]+padovan[m]
        padovan.append(indice)
        
padovastr=[str(a) for a in padovan]

print(f"Los primeros {n} elementos de la serie de Padovan son:", ', ' . join(padovastr))