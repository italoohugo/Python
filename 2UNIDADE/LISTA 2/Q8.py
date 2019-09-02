print('Somatorio')

n = int(input('Digite um numero: '))
while n > 0:
    for i in range(1000000):
        n = int(input('Digite um numero: '))
        t = n + n
print('Total: %.d' % (t))
print('FIM')
