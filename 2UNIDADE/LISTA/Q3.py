print('Sistema de fila')
print()

GER = []
PRI = []
PAG = []
DEP = []

auxGER = 0
auxPRI = 0
auxPAG = 0
auxDEP = 0
print('--- ESCOLHA UMA OPÇÃO DE FILA--- ')
print('1 – Para atendimento geral')  # GER
print('2 – Para atendimento prioritário')  # PRI
print('3 – Para pagamentos de boleto')  # PAG
print('4 – Para depósitos')  # DEP
print()
print('---ATENDIMENTO---')
print('1 - Excluir todos os elementos de uma determinada sigla')
print('2 - Ver quantos elementos de uma determinada sigla tem na fila')
print('3 - Escolher priorizar um dos tipos de ficha ')

print('5 - Para Sair')
parada = False

cliente = input('Digite sua resposta: ')
while parada == False:
    if cliente == '1':
        auxGER = auxGER + 1
        GER.append(auxGER)
        print('''Você selecionou Atendimento Geral
                SUA SENHA É: %.d ''' % (auxGER))
        cliente = input('Digite sua resposta: ')
    elif cliente == '2':
        auxPRI = auxPRI + 1
        PRI.append(auxPRI)
        print('''Você selecionou Atendimento prioritário
                SUA SENHA É: %.d ''' % (auxPRI))
        cliente = input('Digite sua resposta: ')
    elif cliente == '3':
        auxPAG = auxPAG + 1
        PAG.append(auxPAG)
        print('''Você selecionou pagamentos de boleto
                SUA SENHA É: %.d ''' % (auxPAG))
        cliente = input('Digite sua resposta: ')
    elif cliente == '4':
        auxDEP = auxDEP + 1
        DEP.append(auxDEP)
        print('''Você selecionou depósitos
                SUA SENHA É: %.d ''' % (auxDEP))
        cliente = input('Digite sua resposta: ')
    elif cliente == '5':
        parada = True
    else:
        print('COMANDO INVALIDO, DIGITE NOVAMENTE')
        cliente = input('Digite sua resposta: ')


atender = input('Digite sua resposta: ')
if atender == '1':
    print('ESCOLHA O TIPO DE ATENDIMENTO PARA APAGAR')
    print('1 – Para atendimento geral')  # GER
    print('2 – Para atendimento prioritário')  # PRI
    print('3 – Para pagamentos de boleto')  # PAG
    print('4 – Para depósitos')  # DEP
    if atender == '1':
        DelGER = len(GER)
        for x in range(DelGER):
            del GER[0]
        print('---APAGADO COM SUCESSO---')

