print('Programa média do aluno')
UN1 = (float(input('Digite a nota da primeira unidade: ')))
UN2 = (float(input('Digite a nota da segunda unidade: ')))
UN3 = (float(input('Digite a nota da terceira unidade: ')))

if UN1 > UN2:
    if UN2 > UN3:
        menor1 = (UN2)
        menor2 = (UN3)
        melhor = (UN1)
    elif UN1 > UN3:
        menor1 = (UN2)
        menor2 = (UN3)
        melhor = (UN1)
    else:
        menor1 = (UN1)
        menor2 = (UN2)
        melhor = (UN3)
elif UN3 > UN2:
    menor1 = (UN2)
    menor2 = (UN1)
    melhor = (UN3)
elif UN3 > UN1:
    menor1 = (UN3)
    menor2 = (UN1)
    melhor = (UN2)
else:
    menor1 = (UN1)
    menor2 = (UN3)
    melhor = (UN2)

print('As menores notas deste aluno são: %.f e %.f ' %(menor1,menor2))
print('A maior nota deste aluno é %.f '%(melhor))
print()
media = (menor1 + menor2) // 2
resultado = (media + melhor) // 2

print('Media final do aluno: %.f' %(resultado))


