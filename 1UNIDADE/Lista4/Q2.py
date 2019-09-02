print('Programa Diferença de Idade')

nome1 = input('Digite o primeiro nome: ')
idade1 = float(input('Digite a idade do primeiro nome: '))
nome2 = input('Digite o segundo nome: ')
idade2 = float(input('Digite a idade do segundo nome: '))

dif = idade1 - idade2
dif = dif * -1
if dif > 1:
    print(nome1,'e',nome2,'tem diferença de %.i anos'%(dif))
else:
    print(nome1, 'e', nome2, 'tem diferença de %.i ano' % (dif))
