
aluno = []
turma= []

nome = str(input('Digite o nome do aluno: '))
aluno.append(nome)
for l in range(3):
    nota = float(input('Digite a nota: '))
    aluno.append(nota)
media = aluno[1] + aluno[2] + aluno[3]
media = media // 3
aluno.append(media)
print(aluno)
print()
q = len(aluno)
for i in range(q):
    print(aluno[i])

