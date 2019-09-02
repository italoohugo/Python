nomes = []
vendas = []
comissoes = []
porc = []
Tt_vendas = 0

n = int(input('QUANTOS CORRETORES: '))
for i in range(n):
    nome = str(input('Digite o nome: '))
    venda = int(input('Digite o volor a venda: '))
    nomes.append(nome)
    vendas.append(venda)
    if venda>50000:
        comissao = (venda*12)//100
        porc.append('12%')
    elif venda > 30000 and venda<50000 :
        comissao = (venda*9.5)//100
        porc.append('9,5%')
    else:
        comissao = (venda*7)//100
        porc.append('7%')
    comissoes.append(comissao)
    Tt_vendas+=venda
print()
for j in range(n):
    print(nomes[j],'- R$',vendas[j],'- Comissão R$',comissoes[j],porc[j])