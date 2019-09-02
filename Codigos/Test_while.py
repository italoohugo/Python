contador = 0
while contador < 4:
    a = int(input('Digite um numero: '))
    if a % 2 == 1:
        print('O numero é impar')
    else:
        print('O numero é par')
    contador+=1