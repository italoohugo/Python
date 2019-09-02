print('Programa série Fibonacci')

n = int(input('Digite o numero: '))
aux = 1
AUX = 1
while aux > 0:
    for i in range(n):
        AUX = i + n
        
        print('%.d + %.d = %.d' %(i,n,AUX))
        aux = aux -1
