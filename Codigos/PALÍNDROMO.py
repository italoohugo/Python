print('TESTE DE PALÍNDROMO')
palavra = input('Digite uma palavra ou frase: ')
L = list(palavra)

# VERIFICAÇÃO PARA APAGAR ESPAÇOS
L2 = []
for h in range(len(L)):
    if L[h] != ' ':
        L2.append(L[h])
print(L2)

tam = (len(L2)-1)//2
tam2 = len(L2)-1
aux = False
for i in range(tam):
    if L2[i] != L2[tam2]:
        aux = True
    tam2-=1
if aux == True:
    print('NÃO É PALÍNDROMO')
else:
    print('É PALÍNDROMO')