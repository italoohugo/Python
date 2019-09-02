lista = []

for i in range(10):
    n = int(input('Digite o numero par positivo: '))
    if n % 2 ==0:
        lista.append(n)
lista.sort()
print('Lista Crescente: ', lista)

lista_ord = sorted(lista, reverse=True)
print('Lista Decrescente: ', lista_ord)