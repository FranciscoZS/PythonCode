'''
Practica 12
Escribir un programa que almacene en una lista las letras del abecedario,
elimine de la lista las letras que ocupen las posiciones múltiplos de 3 y muestre en pantalla ambas listas, 
la original y la resultante
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

print("Abecedario")

abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
m=len(abc)
abclist=[]
index = [i for i in range(2,19,2)]

for i in range(0,m):
    abclist.append(abc[i])

print(abclist)

for j in range(9):
    abclist.pop(index[j])

print(abclist)
