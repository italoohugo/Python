lista = []
lista_inversa = []
def decrescente (lista):
    elementos = len(lista)-1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if lista[i] < lista[i+1]:
                lista[i],lista[i+1] = lista[i+1],lista[i]
                ordenado = False
        elementos -= 1
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
for i in range(10):
    x = int(input('DIGITE NUMERO INTEIRO: '))
    lista.append(x)
print(lista)
aux = 9
for j in range(10):
    lista_inversa.append(lista[aux])
    aux-=1
print(lista_inversa)
crescente(lista)
print(lista)
decrescente(lista)
print(lista)
