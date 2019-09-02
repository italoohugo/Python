import math

print('Calculo da raiz quadrada')
num = float(input('Digite um numero: '))
if num >=0:
    raiz = math.sqrt(num)
    #raiz = num ** 0.5
    print('A raiz de %.2f é %.2f'%(num,raiz))
else:
    print('Não existe raiz quadrada para esse valor dentro dos numeros reais')
print('Fim do programa')