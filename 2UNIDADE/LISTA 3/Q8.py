n = int(input('Digite o valor de N: '))
for c in range(n):
    linha = []
    for l in range(n):
        if c==l:
            linha.append(1)
        else:
            linha.append(0)
    print(linha)