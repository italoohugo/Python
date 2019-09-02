print('*******Programa Peso Ideal*******')

sexo = input('''Queremos saber qual o seu sexo!!
OBS: Responda M maiusculo se for homem.
     Responda F maiusculo se for mulher.
     Qual sua resposta? 
''')

if sexo == (M):
    alt = int(input('Digite sua altura: '))
    pesoI = (alt-100) - (alt - (150/4))
elif sexo == (F):
    alt = int(input('Digite sua altura: '))
    pesoI = (alt - 100) - (alt - (150 / 2))
else:
    print('Comando Invalido')

print('Seu peso Ideal é: ')