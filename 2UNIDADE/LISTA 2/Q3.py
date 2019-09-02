print('TABUADA')
n = int(input('Digite o numero para a tabuda: '))
aux = 1
i = 0
for i in range(10):
    tab = n * aux
    print(n, 'x', aux, '=', tab)
    aux = aux + 1