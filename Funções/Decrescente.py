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
        print(lista)
lista = [4,5,1,2,3]
decrescente(lista)
print(lista)