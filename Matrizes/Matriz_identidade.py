matriz = []
m = int(input('Digite o valor de M: '))
print('Matriz Identidade')
for l in range(m):
    linha = []
    for c in range(m):
        if l == c:
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)
    print(linha)



