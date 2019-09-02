palavra = input('Digite uma palavra: ')
L = list(palavra)
V = []
C = []

for i in L:
    if i=='A' or i=='E' or i=='I' or i=='O' or i=='U' or i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        V.append(i)
    else:
        C.append(i)
print('VOGAIS:',V)
print('CONSOANTES: ',C)