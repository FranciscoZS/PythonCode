'''
Practica 27
Desarrollar un programa que permita ingresar una palabra o frase y verificar si se trata de un palíndromo o no
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''
print("Palíndromo o no")

while True:
    user = input("Ingresa una frase con solo texto y espacios, de no mas de 100 caracteres:\n")
    user=user.lower()
    p=len(user)
    p1=user.count(',')
    p2=user.count('.')
    p3=user.count(';')
    p4=user.count(':')
    if p1==0 and p2==0 and p3==0 and p4==0:
        break
    else:
        print("Solo tener texto y espacios nada de carrecteres especiales para separar palabras como , ; . :")

userstr=user.split(' ')
print(f"Tu texto es: {user}")
fraseu="".join(userstr)
fraseus=[str(a) for a in fraseu]
index=len(fraseus)
frasei=[]
for i in range(0,index):
    frasei.insert(0,fraseus[i])
fraseiu="".join(frasei)
if fraseu==fraseiu:
    print(f"Tu palabra o frase '{user}' es un palindromo ")
else:
    print(f"Tu palabra o frase '{user}' no es un palindromo")