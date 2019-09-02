maior=0
x=0
while x<10:
    num = int(input('Digite um numero: '))
    x=x+1
    maior=num
    if num>maior:
        maior=num
        print('O maior numero foi %d ' %(maior))