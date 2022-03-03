'''
Practica 25
Desarrollar un programa que permita ingresar cualquier tipo de texto y 
que cuente la frecuencia de aparición de cada letra del alfabeto latino, 
esto el número de cuántas a, b, c, d, ... hay en el texto ingresado
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

print("Conteo de letras en un texto")

user = input("Ingresa una frase:\n")
user=user.lower()
userstr=[str(a) for a in user]
index=len(userstr)
abc="abcdefghijklmnñopqrstuvwxyz"
abcstr=[str(b) for b in abc]
print(f"Tu texto es: {user}")
for i in range(0,27):
    add=userstr.count(abcstr[i])
    value=abcstr[i]
    if add!=0:
        print(f"Este caracter {value} se encuentra {add} veces en el texto.")
        
