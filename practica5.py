'''
Practica 5
Programa para generar un triángulo de Pascal (¿Qué es el triángulo de Pascal o Tartaglia?), 
en donde el usuario ingrese el número de filas que desea observar del triángulo. 
Mostrar el triángulo en consola y almacenarlo como lista de listas
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

print("Triangulo de pascal")

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

pascal=[]

for i in range(n):
    pascal.append([])
    pascal[i].append(1)
    for j in range(1,i):
        pascal[i].append(pascal[i-1][j-1]+pascal[i-1][j])
    if(n!=0):
        pascal[i].append(1)
for i in range(n):
    print("   "*(n-i),end=" ",sep=" ")
    for j in range(0,i+1):
        print('{0:6}'.format(pascal[i][j]),end=" ",sep=" ")
    print()