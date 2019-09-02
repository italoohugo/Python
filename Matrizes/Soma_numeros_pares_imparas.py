matriz = []
somaI = 0
somaP = 0
m = int(input('Digite o valor de M: '))
pares = []
impares = []
for l in range(m):
    linha = []
    for c in range(m):
        aux = int(input('Digoite o elemento: [%d] [%d]' %(l+1, c+1)))
        if aux % 2 == 0:
            pares.append(aux)
            somaP = somaP + aux
        else:
            impares.append(aux)
            somaI = somaI + aux
        linha.append(aux)
    matriz.append(linha)
for i in range(len(matriz)):
    print(matriz[i])
print()

print('OS NUMEROS PARES DA MATRIZ: ',pares)
print('A soma dos numeros PARES é ',somaP)
print()
print('OS NUMEROS IMPARES DA MATRIZ: ',impares)
print('A soma dos numeros IMPARES é ',somaI)
