idade = []
nomes = []
reajuste = []
Valorbase = float(input('digite o valor base de idenização'))
while True:
    nomes.append(str(input('digite o nome do cliente')))
    idade.append(int(input('digite a idade do cliente')))
    s = (str(input('Exite mais clientes? [S/N]')))
    if s in 'N,n':
        break
aux = 0
while aux != len(idade):
    if (idade[aux] <= 12):
        reajuste.append(Valorbase +(30/100 * Valorbase))
        print(f"O nome do cliente é {nomes[aux]}")
        print(f'a idade do cliente é {idade[aux]}')
        print(f'O valor apos o reajuste é {reajuste}')


    if (idade[aux] >=13 and idade[aux] <= 49):
        reajuste = (Valorbase + (10/100 *Valorbase))
        print(f"O nome do cliente é {nomes[aux]}")
        print(f'a idade do cliente é {idade[aux]}')
        print(f'O valor apos o reajuste é {reajuste}')


    if (idade[aux] >=50 and idade[aux] <= 65):
        reajuste = (Valorbase + (15/100 *Valorbase))
        print(f"O nome do cliente é {nomes[aux]}")
        print(f'a idade do cliente é {idade[aux]}')
        print(f'O valor apos o reajuste é {reajuste}')


    if (idade[aux] > 65):
        reajuste = (Valorbase + (35/100 *Valorbase))
        print(f"O nome do cliente é {nomes[aux]}")
        print(f'a idade do cliente é {idade[aux]}')
        print(f'O valor apos o reajuste é {reajuste}')
    aux+=1