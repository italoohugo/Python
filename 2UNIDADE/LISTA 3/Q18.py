n = int(input('Digite o valor de N: '))
aux1 = n//2
aux2 = (n//2)-1
if n%2==0:
    tam = n // 2
else:
    tam = (n -1)//2
if n%2!=0:
    for c in range(n):
        linha =[]
        for l in range(n):
            if l==tam and c==tam:
                linha.append(1)
            else:
                linha.append(0)
        print(linha)
else:
    for c in range(n):
        linha =[]
        for l in range(n):
            if l==(aux2) and c==(aux2) or l==(aux1) and c==(aux2) or l==(aux2) and c==(aux1) or l==(aux1) and c==(aux1):
                linha.append(1)
            else:
                linha.append(0)
        print(linha)
    tam+=1

# 22 32
# 23 33