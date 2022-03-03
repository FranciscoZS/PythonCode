'''
Practica 6
Programa que permita el ingreso de un número entero positivo, en el intervalo de 0 a 1,000,000, 
y representarlo como la suma de sus unidades, decenas, centenas..., esto es, 
si se ingresa el valor de 1942 este debe de ser igual a: 1942 = 1000 + 900 + 40 + 2
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

print("Descomposición de un numero")

while True:
        user = input("Dame un numero entero y positivo en el intervalo de 0 a 1,000,000:\n")
        try:
            n= int(user)
        except:
            print("¡¡Debe ser numero entero y positivo en el intervalo de 0 a 1,000,000!! \n")
        else:
            if n % 1 == 0 and n >0 and n<1000000:
                break
            elif n == 0:
                print("el zero es la mitad de la recta no jala")
            else:
                print("¡¡Debe ser entero y positivo dentro del intervalo!!")

nstr=str(n)
m=len(nstr)
m2=m-1
year=[]

for i in range(0,m):
    year.append(int(nstr[i])*10**m2)
    m2=m2-1

yearstr= [str(a) for a in year]

print(f"{n} = ",' + '. join(yearstr))