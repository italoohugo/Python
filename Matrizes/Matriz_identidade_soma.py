matriz = []
soma = 0
m = int(input('Digite o valor de M: '))

for l in range(m):
    linha = []
    for c in range(m):
        aux = int(input('Digoite o elemento: [%d] [%d]' %(l+1, c+1)))
        if l == c:
            soma = soma + aux
        linha.append(aux)
    matriz.append(linha)
for i in range(len(matriz)):
    print(matriz[i])
print('A soma da Matriz identidade é ',soma)