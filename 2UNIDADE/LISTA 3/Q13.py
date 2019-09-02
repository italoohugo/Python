taxa_final = 0
nome_final = ''
for i in range(3):
    pro = input("Digite o nome do provedor %.f :"%(i+1))
    velo = int(input('Digite a velocidade: '))
    if velo > taxa_final:
        taxa_final = velo
        nome_final = pro
print("Provedor : %s , Velocidade : %d" %(nome_final, taxa_final))
