print('Programa casar ou comprar uma bicicleta')
print()
print('Responda "S" para Sim ou "N" para Não')
gord = input('Você esta gordo(a)? ')
if gord == ('S'):
    ema = input('Quer emagrecer? ')
    if ema == ('S'):
        print('Compre uma bicicleta')
    else:
        print('Case')
elif gord == ('N'):
    eng = input('Quer engordar? ')
    if eng == ('S'):
        print('Case')
    else:
        print('Compre uma bicicleta')
else:
    print('Comando invalido')
