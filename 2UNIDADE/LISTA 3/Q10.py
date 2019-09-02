import random
lista = []
n_pares = []
n_impares = []
print('----SEPARAR PARES DE IMPARES----')
print()
n = int(input('Digite qunatos numeros vc quer testar: '))

for i in range(n):
    add = random.randint(0,100)
    lista.append(add)
print(lista)

for i in lista:
    if i%2 == 0:
        n_pares.append(i)
    else:
        n_impares.append(i)
print()
print('PARES: ',n_pares)
print('IMPARES: ',n_impares)