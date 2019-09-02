lista = []
soma = 0
aux = []
condicao = False
for i in range(10):
    n = int(input('Digite um numero inteiro positivo: '))
    for x in aux:
        while x == n:
            for x in aux:
                n = int(input('DIGITE UM NUMERO DIFERENTE: '))
    lista.append(n)
    aux.append(n)
    soma = soma + n


media = soma //10
lista.sort()
print('Media:', media)
for j in (lista):
    if j < media:
        print(j,'esta abaixo da media')
print(lista)
print(aux)