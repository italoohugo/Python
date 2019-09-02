lista = []
nome = []
while nome != 'fim':
    nome = input('Digite o nome: ')
    lista.append(nome)
tam = len(lista)
del lista[tam-1]
lista.sort()
print(lista)


