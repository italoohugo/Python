contatos = []
numeros = []
cont = 1
n = int(input('Quantos contatos quer cadastrar? '))
for i in range(n):
    print('CONTATO ',cont)
    contato = str(input('Digite o nome do contato: '))
    contatos.append(contato)
    numero = input('Digite o numero: ')
    lista = list(numero)
    while len(lista) <8 or len(lista)> 8:
        numero = input('Digite o numero novamente: Obs. deve conter 8 digitos ')
        lista = list(numero)
    numeros.append(numero)
    cont +=1
print()
for j in range(len(contatos)):
    print('CONTATO %.f:'%(j+1))
    print('NOME:',contatos[j])
    print('NUMERO:',numeros[j])