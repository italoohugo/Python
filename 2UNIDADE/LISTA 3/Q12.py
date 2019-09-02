import random
n = int(input('Digite o valor de n: '))
inicial = random.randint(1,9)
matriz = []
for l in range(n):
    linha = []
    for c in range(n):
        aux = inicial
        inicial = inicial +1
        linha.append(aux)
    print(linha)
