print('Salario do João')
v = 1000
p = 1.5
ano = 2010
print('Ano: 2010 = R$ 1025.00')
for i in range(1, 9):
    aux = p + i + 0.5
    t = v * aux //100
    tt = v + t
    ano = ano + 1
    print('Ano: %.f   X %5.1f = R$ %5.2f'%(ano,aux,tt))
