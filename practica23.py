'''
Practica 23
Generar un programa que permita ingresar una frase y también solicite la forma de ordenarla, alfabéticamente directa o inversa
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

print("Orden de una Frase")
user = input("Ingresa una frase:\n")
while True:
    option= input("De que forma quiere que se ordene, Alfabéticamente Directa [d] o Inversa [i]:\n")
    option=option.lower()
    if option=='d' or option=='i':
        break
    else:
        print("Opcion invalida")

user=user.replace(',','')
frasesp=user.split(' ')
if option=='d':
    ordd=sorted(frasesp)
    print("Tu frase ordenada es: ", ' '. join(ordd))
else:
    ordd=sorted(frasesp, reverse=True)
    print("Tu frase ordenada es: ", ' '. join(ordd))