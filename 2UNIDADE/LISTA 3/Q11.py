import random
n = int(input('Digite a quant de Dados: '))
dados = []
n1 = []
n2 = []
n3 = []
n4 = []
n5 = []
n6 = []
dado = 0
for i in range(n):
    dado = random.randint(1,6)
    dados.append(dado)
for j in dados:
    if j == 1:
        n1.append(j)
    elif j == 2:
        n2.append(j)
    elif j == 3:
        n3.append(j)
    elif j == 4:
        n4.append(j)
    elif j == 5:
        n5.append(j)
    elif j == 6:
        n6.append(j)
print('O numero 1 foi sorteado',len(n1),'vezes')
print('O numero 2 foi sorteado',len(n2),'vezes')
print('O numero 3 foi sorteado',len(n3),'vezes')
print('O numero 4 foi sorteado',len(n4),'vezes')
print('O numero 5 foi sorteado',len(n5),'vezes')
print('O numero 6 foi sorteado',len(n6),'vezes')



