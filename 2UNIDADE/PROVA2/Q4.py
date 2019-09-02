import random
soma_l4 = 0
soma_c2 = 0
soma_p = 0
soma_todos = 0
M = 5
for l in range(M):
    linha = []
    for c in range(M):
        x = random.randint(1,10)
        linha.append(x)
        if l ==3:
            soma_l4+=x
        if c==1:
            soma_c2+=x
        if c==l:
            soma_p+=x
        soma_todos+=x
    print(linha)
print('Soma da linha 4: ',soma_l4)
print('Soma da coluna 2: ',soma_c2)
print('Soma da diagonal principal: ',soma_p)
print('Soma de todos os elemnetos: ',soma_todos)
