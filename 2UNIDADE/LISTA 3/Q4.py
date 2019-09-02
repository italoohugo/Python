lista = [9,1,3,2,5,2,5,5,7,0,4,1,6,5,9]
soma = 0
for i in (lista):
    soma = soma + i
print('1 - SOMA: ',soma)

lista_ord = sorted(lista, reverse=True)
soma2 = lista_ord[0] + lista_ord[1] + lista_ord[2] + lista_ord[12] + lista_ord[13] + lista_ord[14]
print()
print('2 - SOMA(3 maiores e 3 menores: ',soma2)
