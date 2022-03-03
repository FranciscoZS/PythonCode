'''
Practica 21
Desarrollar un programa que muestre al usuario si un número entero positivo ingresado por el es un número feliz , 
en caso de serlo mostrar el por que se trata de uno de ellos 
(mostrar la relación de recurrencia que se muestra en la página de referencia para el 7)
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

print("Numero feliz o infeliz")

while True:
        user = input("Dame un numero entero y positivo:\n")
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

n0=1
ni=4
nc=n
def nf(n):
    nstr=str(n)
    m=len(nstr)
    numero=[]
    
    for i in range(0,m):
        numero.append(int(nstr[i]))
        
    suma = 0
    
    for elemento in numero:
        suma += elemento**2
    
    return suma

def digitos(n):
    nstr=str(n)
    m=len(nstr)
    numero=[]
    
    for i in range(0,m):
        numero.append(int(nstr[i]))
        
    suma = 0
    
    numerostr= [str(a) for a in numero]
    
    for elemento in numero:
        suma += elemento**2
    print("La suma de los digitos del numero elevados al cuadrado es es:", '^2 + '. join(numerostr), f"^2 = {suma}")
    
suma=0

while True:
    a=nf(n)
    digitos(n)
    n=a
    if n==n0:
        print(f"El numero {n} es un numero feliz por que su iteracion de la suma de sus digitos en algun momento da 1")
        break
    elif n==nc:
        print(f"El numero {n} no es un numero feliz (numero infeliz) por que su iteracion de la suma de sus digitos en algun momento da el mismo numero")
        break
    elif n==ni:
        print(f"El numero {n} cae en un bucle de numeros infleices de tal forma que siempre suman 4")
        break