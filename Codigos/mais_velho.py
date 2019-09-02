print('Programa Maior Idade')
nome1 = input('Digite o nome do primeiro usuario: ')
idade1 = input('Digite a idade do primeiro usurio: ')
nome2 = input('Digite o nome do segundo usuario: ')
idade2 = input('Digite a idade do segundo usurio: ')

if idade1 > idade2:
    print(nome1,'é mais velho')
    print(nome2,'é mais novo')
elif idade1 < idade2:
    print(nome2,'é mais velho')
    print(nome1,'é mais novo')
else:
    print(nome1,'e',nome2,'Possuem a mesma idade')