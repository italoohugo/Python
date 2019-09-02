import random
matriz = []
soma = 0
m = int(input('Digite o valor de m: '))
n = m
for l in range(m):
    linha = []
    for c in range(n):
        aux = random.randint(0,9)
        matriz.append(aux)
        linha.append(aux)
        if l == c:
            soma = soma + aux
    print(linha)
matriz.sort()
print()
tam = len(matriz)
print('Soma da diagonal principal: ',soma)
print('O menor numero da matriz é: ',matriz[0])
print('O maior numero da matriz é: ',matriz[tam-1])
