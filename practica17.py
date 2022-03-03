'''
Practica 17
Programa que al recibir un número entero positivo N, permita obtener la lista de número de Keith
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

print("Lista de números Keith")

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

keith=[]
def nkeith(n):
    nstr = [int(i) for i in str(n)]

    v=n
    a=0
    suma = 0

    while suma < n:    
        suma = 0   
        for i in nstr:
            suma += i

        for i, value in enumerate(nstr):
            if i == len(nstr) - 1:
                nstr[i] = suma
            else:
                nstr[i] = nstr[i+1]

    if suma == n:
        return v
    else:
        return a

if 1<=n<=5:
    z=101
elif 6<=n<=8:
    z=1000
elif 9<=n<=17:
    z=10000
elif 18<=n<=25:
    z=100000
else:
    z=10**10

for i in range(14,z): #apartir de n = 25 el programa genera error
    a=nkeith(i)
    keith.append(a)
    try:
        keith.remove(0)
    except:
        a=0

keithstr=[str(a) for a in keith]
keithstr2=[]
for i in range(0,n):
    keithstr2.append(keithstr[i])

print(f"Los {n} numeros keith son:", ', ' . join(keithstr2))