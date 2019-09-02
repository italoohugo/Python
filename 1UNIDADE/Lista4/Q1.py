print('Programa mais velho e mais novo')

nome1 = input('Digite o primeiro nome: ')
idade1 = float(input('Digite a idade do primeiro nome: '))
nome2 = input('Digite o segundo nome: ')
idade2 = float(input('Digite a idade do segundo nome: '))

if idade1 > idade2:
    print(nome1,'é mais velho')
    print(nome2,'é mais novo')
else:
    print(nome2,'é mais velho')
    print(nome1,'é mais novo')