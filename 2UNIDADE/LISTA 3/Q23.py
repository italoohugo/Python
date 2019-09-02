import random
aux = 0
lin = 0
col = 0
for l in range(5):
    linha = []
    for c in range(5):
        x = random.randint(1,99)
        while x%2 != 0:
            x = random.randint(1, 99)
        linha.append(x)
        if x>aux:
            aux=x
            lin=l
            col=c
    print(linha)
print('Maior numero: ',aux)
print('Coluna: ',col+1,'Linha: ',lin+1)