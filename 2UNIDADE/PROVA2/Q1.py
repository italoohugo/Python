nomes = []
nota1 = []
nota2 = []
nota3 = []
M = []
status = []
n = int(input('Quantos candidatos? '))
for i in range(n):
    nome=str(input('Digite o nome: '))
    N1 = int(input('Digite a n ota de Português: '))
    N2 = int(input('Digite a n ota de Matematica: '))
    N3 = int(input('Digite a n ota de Conhecimentos Gerais: '))
    nomes.append(nome)
    nota1.append(N1)
    nota2.append(N2)
    nota3.append(N3)
    media = ((N1+N2+N3)//3)
    M.append(media)
    if media>7 and N1>5 and N2>5 and N3>5:
        status.append('APROVADO')
    else:
        status.append('REPROVADO')
    print()
for j in range(len(nomes)):
    print('CANDIDATO: ',nomes[j])
    print('NOTA DE MATEMATICA: ',nota1[j])
    print('NOTA DE PORTUGUÊS: ', nota2[j])
    print('NOTA DE CONHECIMENTOS GERAIS: ',nota3[j])
    print('MEDIA: ',M[j])
    print('Status: ',status[j])
    print()