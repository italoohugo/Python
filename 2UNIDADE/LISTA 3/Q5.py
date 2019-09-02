candidatos = [22,45,78,5,45,63,99,2,51,8]
aprovados = []
em_espera = []
for i in candidatos:
    if i >= 50:
        print(i,"= aprovado")
        aprovados.append(i)
    elif i > 10 and i < 50:
        print (i,"= lista de espera")
        em_espera.append(i)
    else:
        print (i,"= foi reprovado")
print()
print('Lista de aprovados',aprovados)
print('Lista de em espera',em_espera)
print("FIM!")