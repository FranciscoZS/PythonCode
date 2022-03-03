'''
Practica 24
Desarrollar un programa que permita ingresar una frase solo texto y espacios de no más de 100 caracteres y 
que imprima la frase en cada línea eliminando los espacios, de la siguiente forma:
La frase que se ingreso tiene menos de cien caracteres
La frase que se ingreso tiene menos de cien
La frase que se ingreso tiene menos de
La frase que se ingreso tiene menos
La frase que se ingreso tiene
La frase que se ingreso
La frase que se
La frase que
La frase
La
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

print("Desintregar una Frase")

while True:
    user = input("Ingresa una frase con solo texto y espacios, de no mas de 100 caracteres:\n")
    user=user.lower()
    p=len(user)
    p1=user.count(',')
    p2=user.count('.')
    p3=user.count(';')
    p4=user.count(':')
    if 0<p<=100 and p1==0 and p2==0 and p3==0 and p4==0:
        break
    else:
        print("la frase debe tener menos de 100 caracteres y solo tener texto y espacios nada de carrecteres especiales para separar palabras como , ; . :")

frasesp=user.split(' ')
index=len(frasesp)

for i in range (0,index):
    print(' '. join(frasesp))
    frasesp.pop()