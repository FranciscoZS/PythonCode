'''
Practica 26
Desarrollar un programa que permita ingresar cualquier tipo de texto y 
que lo encripte utilizando para ello la Encriptación o Cifrado César, 
por lo que se debe también solicitar cuántas posiciones se debe mover en el alfabeto para realizar la encriptación
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''
print("Cifrado César")

user = input("Ingresa una frase:\n")
user=user.lower()
userstr=[str(a) for a in user]
index=len(userstr)
abc="abcdefghijklmnñopqrstuvwxyz"
abcstr=[str(b) for b in abc]
print(f"Tu texto es: {user}")

while True:
        user = input("Dame un numero entero y positivo que sea lasposiciones que se debe mover el alfabeto:\n")
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

abcstrc=abcstr.copy()
cifradoc=abcstr

for i in range(0,n):
    cifradoc.sort(key = abcstr[0] .__eq__)

textoc=[]
dic={}

for j in range(0,27):
    dic[abcstrc[j]]=cifradoc[j]

for k in range(0,index):
    value=userstr[k]
    try:
        textoc.append(dic[value])
    except:
        textoc.append(value)

print("Tu acordeon de cifraado es:\n")

for key in dic:
  print(key, ":", dic[key])

print("Tu texto cifrado con un desplazamiento de {n} espacios a la derecha es:\n", ''. join(textoc))