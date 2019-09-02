print('Programa Media e status do aluno')
nome = input('Digite o nome do aluno:')
matricula = int(input('Digite o numero da matricula: '))
n = 1
soma = 0
unid1 = 1

unid1 = int(input('Digite a nota da unidade %d: ' % (n)))
while unid1 < 0 or unid1 > 10:
    print('Comando inavlido, Tente novamente')
    print()
    unid1 = int(input('Digite a nota da unidade %d: ' % (n)))
n = n + 1

unid2 = int(input('Digite a nota da unidade %d: ' % (n)))
while unid2 < 0 or unid2 > 10:
    print('Comando inavlido, Tente novamente')
    print()
    unid2 = int(input('Digite a nota da unidade %d: ' % (n)))
n = n + 1

unid3 = int(input('Digite a nota da unidade %d: ' % (n)))
while unid3 < 0 or unid3 > 10:
    print('Comando inavlido, Tente novamente')
    print()
    unid3 = int(input('Digite a nota da unidade %d: ' % (n)))
n = n + 1

soma = + unid1 + unid2 + unid3

media = soma //3
print('Soma das unidades: ',soma)
print('Media: %2d' %(media))

if media > 1 and media < 3:
    print(nome, 'esta reprovado')
if media > 4 and media < 6:
    print(nome, 'esta em recuperaçao')
if media > 7 and media < 10:
    print(nome, 'esta Aprovado')
