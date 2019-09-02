import random
lista = []
def crescente (lista):
    elementos = len(lista)-1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if lista[i] > lista[i+1]:
                lista[i],lista[i+1] = lista[i+1],lista[i]
                ordenado = False
        elementos -= 1
print('DADOS')
for i in range(20):
    x = random.randint(1,6)
    lista.append(x)
print(lista)
crescente(lista)
maior=lista[19]
menor=lista[0]
quantmaior = 0
quantmenor = 0
for j in lista:
    if j ==menor:
        quantmenor=quantmenor+1
    elif j ==maior:
        quantmaior=quantmaior+1


print('Menor numero sorteado: ',menor,'e foi sorteado',quantmenor,'vezes')
print('Maior numero sorteado: ',maior,'e foi sorteado',quantmaior,'vezes')



