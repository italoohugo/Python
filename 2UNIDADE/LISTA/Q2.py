lista = []
aux = 1
for i in range(7):
    temp = int(input('Digite a temperatura do %.d ° dia: ' %(aux)))
    lista.append(temp)
    aux = aux + 1
lista.sort()
menor = lista[0]
maior = lista[6]
print('A menor temperatura é ', menor,'°')
print('A menor temperatura é ', maior,'°')