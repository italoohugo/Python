print('Programa Par ou Ímpar')

num = float(input('Digite um numero: '))

test = num % 2

if test != 0:
    print('%.i é ímpar'%(num))
else:
    print('%.i é par'%(num))