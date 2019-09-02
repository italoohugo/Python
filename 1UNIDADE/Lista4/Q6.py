print('Programa teste de numero maior e menor')
print('Digite 3 numeros ')
a = float(input('Digite o primeiro numero: '))
b = float(input('Digite o segundo numero: '))
c = float(input('Digite o terceiro numero: '))

if a > b:
    if b > c:
        print(a,c)
    elif a > c:
        print(a,b)
    else:
        print(c,b)
elif c > b:
    print(c,a)
elif c > a:
    print(b,a)
else:
    print(b,c)