rot = 1
aux1 = 0
aux2 = -3
aux3 = 2
x = 'X'
for i in range(8):
    for l in range(3):
        linha = []
        for c in range(3):
            if rot ==1 or rot ==2 or rot==3:
                if l == aux1:
                    linha.append(x)
                else:
                    linha.append('O')
            elif rot ==4 or rot ==5 or rot==6:
                if c == aux2:
                    linha.append(x)
                else:
                    linha.append('O')
            elif rot ==7:
                if c == l:
                    linha.append(x)
                else:
                    linha.append('O')
            elif rot ==8:
                if l==2 and c==0 or l==1 and c==1 or l==0 and c==2:
                    linha.append(x)
                else:
                    linha.append('O')
        print(linha)
    aux1+=1
    aux2+=1
    aux3-=1
    print()
    rot = rot + 1


# 0 1 2
# 0 1 2
# 0 1 2

# L=2 C=0
# L=1 C=1
# L=0 C=2