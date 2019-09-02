palavra = str(input('Digite uma palavra: '))
lista = list(palavra)
aux = []
print(lista)
cont = len(lista)
for i in range(cont):
    aux.append(lista[cont-1])
    cont-=1
print(aux)