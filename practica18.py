'''
Practica 18
Programa que al ingresar un número entero positivo en un intervalo de 1 a 3999, muestre su representación en números romanos
@utor: Francisco Zamora Saldaña
Programación avanzada 2MM3
'''

print("Representacion romana de un numero")

while True:
        user = input("Dame un numero entero y positivo en el intervalo de 1 a 3999:\n")
        try:
            n= int(user)
        except:
            print("¡¡Debe ser numero entero y positivo en el intervalo de 0 a 3999!! \n")
        else:
            if n % 1 == 0 and n >0 and n<=3999:
                break
            elif n == 0:
                print("el zero es la mitad de la recta no jala")
            else:
                print("¡¡Debe ser entero y positivo dentro del intervalo!!")

romanos={'1':'I', '5':'V', '10':'X', '50':'L', '100':'C', '500':'D', '1000':'M'}
nstr=str(n)
m=len(nstr)
m2=m-1
year=[]
romanon=[]


for i in range(0,m):
    year.append(int(nstr[i])*10**m2)
    m2=m2-1

yearstr= [str(a) for a in year]
z=len(yearstr)

for i in range(0,z):
    if year[i]%1000==0:
        if year[i]//1000<4:
            p=year[i]//1000
            romanon.append(p*romanos['1000'])
    elif year[i]%100==0:
        if year[i]//100<4:
            p=year[i]//100
            romanon.append(p*romanos['100']) 
        elif year[i]//100==4:
            p=year[i]//100
            romanon.append(romanos['100']+romanos['500'])
        elif year[i]//100==5:
            romanon.append(romanos['500'])
        elif 5<year[i]//100<9:
            p=year[i]//100
            romanon.append(romanos['500']+((p-5)*romanos['100']))
        elif year[i]//100==9:
            romanon.append(romanos['100']+romanos['1000'])
    elif year[i]%10==0:
        if year[i]//10<4:
            p=year[i]//10
            romanon.append(p*romanos['10']) 
        elif year[i]//10==4:
            p=year[i]//10
            romanon.append(romanos['10']+romanos['50'])
        elif year[i]//10==5:
            romanon.append(romanos['50'])
        elif 5<year[i]//10<9:
            p=year[i]//10
            romanon.append(romanos['50']+((p-5)*romanos['10']))
        elif year[i]//10==9:
            romanon.append(romanos['10']+romanos['100'])
    elif year[i]%1==0:
        if year[i]//1<4:
            p=year[i]//1
            romanon.append(p*romanos['1']) 
        elif year[i]//1==4:
            p=year[i]//1
            romanon.append(romanos['1']+romanos['5'])
        elif year[i]//1==5:
            romanon.append(romanos['5'])
        elif 5<year[i]//1<9:
            p=year[i]//1
            romanon.append(romanos['5']+((p-5)*romanos['1']))
        elif year[i]//1==9:
            romanon.append(romanos['1']+romanos['10'])

a=romanon.count('')

for i in range(0,a):
    romanon.remove('')
    yearstr.remove('0')
    
print(f"El numero {n} se descompone en:",' '. join(yearstr), "Y su representacion en numeros romanos es:", ''.join(romanon))
