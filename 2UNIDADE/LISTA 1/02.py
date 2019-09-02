numeros = int(input('Quantos numeros serão informados? '))
v = 0
num = 1
n = 0
soma = 0
while v < numeros:
    n = int(input('Digite o numero %d:'%num))
    v = v + 1
    num = num + 1
    soma = soma + n
resultado = soma // numeros
print('O resultado da media:',resultado)
