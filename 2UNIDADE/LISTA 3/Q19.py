import random
multiplos = []
n = int(input('Digite um numero: '))
lista = []
for i in range(10):
    x = random.randint(1,100)
    lista.append(x)
for j in range(10):
    m = ((j+1)*n)
    print(j+1,'x',n,'=',m)
    for k in lista:
        if m==k:
            multiplos.append(m)
print('Numeros:',lista)
print('Multiplos: ',multiplos)







#Múltiplos e divisores são números que resultam da multiplicação por um número natural e que dividem um número deixando resto zero