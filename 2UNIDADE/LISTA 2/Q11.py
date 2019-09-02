import random
print('Programa advinhe o numero')
print()
print('---Digite o intervalo dos numeros q vc quer advinhar---')
inter1 = int(input('Digite o primeiro Intevalo: '))
inter2 = int(input('Digite o segundo Intevalo: '))
print()
s = int(input('Digite o numero de tentativas: '))

n = int(input('Digite o seu palpite: '))
x = random.randint(inter1,inter2)
for i in range(s):
    if n != x:
        print('NUMEROS DIFERENTES, TENTE NOVAMENTE')
        print('Seu numero:', n)
        print('Numero do PC:', x)
        print()
        x = random.randint(inter1, inter2)
        n = int(input('Digite o seu palpite: '))
    else:
        print('PARABENS, VC ACERTOU O PALPITE')
        print('Seu numero:', n)
        print('Numero do PC:', x)
        break
