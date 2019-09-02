print('TABUADA')
n = int(input('Digite o numero para a tabuda: '))
aux = int(input('Em qual numero vc quer começar? '))
auxx = aux + 1
i = 0

for i in range(auxx):
    tab = n * aux
    print(n, 'x', aux, '=', tab)
    aux = aux + 1