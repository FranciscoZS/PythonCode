'''
Practica 2
Programa que muestre la tabla de multiplicar de un número entero positivo N dado por el usuario 
(mostrar la tabla del 1 al 10 con un formato adecuado de tabla), almacenar los datos como un diccionario, 
donde se tenga el número a multiplicar y el resultado
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

print("Tabla de multiplciar")

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
                  
n_txt = str(n)
tabla = {}

for i in range(1,11):
    i_txt = str(i)
    r=n*i
    tabla.setdefault(f"{n_txt} x {i_txt}",r )

for key in tabla:
    print(key, "=", tabla[key])
