'''
Practica 19
Desarrollar un programa que muestre la serie de números de Pell que el usuario solicite
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

print("Serie de números de Pell")

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

pell = []

for i in range(1,n+1):
    p=(((1+(2**(0.5)))**i)-((1-(2**(0.5)))**i))/(2*(2**(0.5)))
    pell.append(round(p))
        
pell=[str(a) for a in pell]

print(f"Los primeros {n} elementos de la serie de Pell son:", ', ' . join(pell))