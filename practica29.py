'''
Practica 29
Generar una pequeña calculadora de números complejos que le permita al usuario seleccionar 
si realizar operaciones con un par de números complejos o un solo número complejo. 
En el caso de un solo número complejo, la calculadora permitirá mostrar tanto la parte real, 
como la compleja,. el valor absoluto o módulo y la fase . En el caso de que se permita ingresar un par de números complejos, 
estos podrán o sumarse, restarse, multiplicarse, dividirse o realizar el producto escalar. 
(Notar que en este ejercicio es necesario el uso de una instrucción switch, encontrar la forma de sustituir dicha instrucción, 
pues en Python no se dispone de ella)
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

import math, cmath
from pickletools import read_long1

print("Calculadora de numero complejos")

def ncomplejo():
    while True:
            user = input("Dame un numero complejo recuerda que debe ser de la forma:\na+bj:\n")
            try:
                n= complex(user)
                break
            except:
                print("¡¡Debe ser numero complejo de la forma: a+bj\n")
    return n

def realn():
    print("Elejiste la Opcion 1. Mostar la parte real del numero complejo")
    n=ncomplejo()
    nreal=n.real
    print(f"Tu numero complejo es: {n}\nLa parte real de tu numero complejo es: {nreal}")

def imagn():
    print("Elejiste la Opcion 2. Mostar la parte compleja del numero complejo")
    n=ncomplejo()
    nimg=n.imag
    print(f"Tu numero complejo es: {n}\nLa parte imaginaria o compleja de tu numero complejo es: {nimg}")

def partes():
    print("Elejiste la Opcion 3. Mostar la parte real e imaginaria del numero complejo")
    n=ncomplejo()
    nreal=n.real
    nimg=n.imag
    print(f"Tu numero complejo es: {n}\nLa parte real de tu numero complejo es: {nreal}\nLa parte imaginaria de tu numero complejo es: {nimg}")

def modu():
    print("Elejiste la Opcion 4. Calcular el modulo o valor absoluto de tu numero complejo")
    n=ncomplejo()
    modn=math.sqrt((n.real**2)+(n.imag**2))
    print(f"El modulo de {n} es: {modn}")

def fase():
    print("Elejiste la Opcion 5. Calcular la fase de tu numero complejo")
    n=ncomplejo()
    fasen=cmath.phase(n)
    fasend=math.degrees(fasen)
    print(f"La fase de {n} es: {fasen} radianes o {fasend}")

def pescalar1():
    print("Elejiste la Opcion 6. Calcular el producto escalar de tu numero complejo")
    n=ncomplejo()
    r=float(input("Dame el numero por el cual se va a multiplicar tu numero complejo:\n"))
    complejoc=r*n
    print(f"Tu numero complejo se mmultiplico por {r}.\nEl producto escalar es: {r} * {n} = {complejoc}")

def error():
    print("error, opcion invalida")    

def sumc():
    print("Elejiste la Opcion 1. Calcular la suma de tus numero complejos")
    n=ncomplejo()
    m=ncomplejo()
    sumc=n+m
    print(f"la suma de tus numeros complejos es: {n} + {m} = {sumc}")

def resc():
    print("Elejiste la Opcion 2. Calcular la resta de tus numero complejos")
    n=ncomplejo()
    m=ncomplejo()
    resc=n-m
    print(f"La resta de tus numeros complejos es: {n} - {m} = {resc}")

def multc():
    print("Elejiste la Opcion 3. Calcular la multiplicación de tus numero complejos")
    n=ncomplejo()
    m=ncomplejo()
    multc=n*m    
    print(f"La multiplicación de tus numeros complejos es: {n} * {m} = {multc}")

def divc():
    print("Elejiste la Opcion 4. Calcular la división de tus numero complejos")
    n=ncomplejo()
    m=ncomplejo()
    divc=n/m
    print(f"La división de tus numeros complejos es: {n} / {m} = {divc}")

def pescalar2():
    print("Elejiste la Opcion 5. Calcular el producto escalar de tus numero complejos")
    n=ncomplejo()
    m=ncomplejo()
    r=float(input("Dame el numero por el cual se va a multiplicar tus numeros complejos:\n"))
    complejoc1=r*n
    complejoc2=r*m
    print(f"Tus numeros complejos se mmultiplicaron por {r}.\nEl producto escalar de {n} es: {r} * {n} = {complejoc1}\nEl producto escalar de {m} es: {r} * {m} = {complejoc2}")


opt1={
    '1':realn,
    '2':imagn,
    '3':partes,
    '4':modu,
    '5':fase,
    '6':pescalar1
    }

opt2={
    '1':sumc,
    '2':resc,
    '3':multc,
    '4':divc,
    '5':pescalar2
}



while True:
    while True:
        option=input("Cuantos numeros complejos desea operar, uno [1] o dos [2]:\n")
        if option=='1':
            break
        elif option=='2':
            break
        else:
            print("opcion invalida")
    if option=='1':
        sw=input('''Elije como quieres operar el numero complejo.
        Mostrar parte real [1]
        Mostrar parte imaginaria [2]
        Mostrar tanto parte real como imaginaria [3]
        Calcular el modulo [4]
        Calcular la fase [5]
        Calcular el producto escalar [6]
        Teclea el numero asociado a la opción:
        ''')
        opt1.get(sw, error)()
    elif option=='2':
        sw=input('''Elije como quieres operar Los numeros complejos, recuerda que el orden de tipeo.
        Suma de los numeros [1]
        Resta de los numeros [2]
        Multiplicacion de los numeros [3]
        Division de los numeros [4]
        Producto escalar a los numeros [5]
        Teclea el numero asociado a la opción:
        ''')
        opt2.get(sw, error)()
    option=input("Si deseas volver a comenzar pon s y enter; si no teclea otra cosa y da enter o enter solito\n")
    if option=='s':
        print("Vale, empezemos otra vez\n")
    else:
        break
    

