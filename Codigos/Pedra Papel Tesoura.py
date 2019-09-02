import random
import os
p_jog = 0
p_pc = 0
print('======Jogo pedra, papel, tesoura======')
print('======================================')
print('''=======Escolha um Modo de Jogo========
	 
	    Responda 'M' para Multiplayer
	    Responda 'C' para Computador ''')
pvp = input('Modo: ')
if pvp == 'C':
	nome = (input('Digite seu nome: '))
	print('Bem-Vindo ao jogo',nome)
	print()
	print(''''==============REGRAS==================
	- Pedra ganha da tesoura (amassando-a ou quebrando-a).
	- Tesoura ganha do papel (cortando-o).
	- Papel ganha da pedra (embrulhando-a).
	
	A cada vitoria vc ganha 3 PONTOS
	A cada empate vc gannha 1 PONTO''')

	jn = 'S'
	while jn == 'S':
		print('''Escolha:
		1 - Pedra
		2 - Papel
		3 - Tesoura
		''')
		pc = random.randint(1, 3)
		jog = 1
		cond = True
		while jog == 1 or 2 or 3 and cond == True:
			jog = int(input('Qual sua jogada? '))
			print()
			cond = False
			if jog == 1:
				print('O Jogador escolheu pedra')
			elif jog == 2:
				print('O Jogador escolheu Papel')
			elif jog == 3:
				print('O Jogador escolheu Tesoura')

		else:
			print('ERRO, Comando invlido, digite novamente')

		if pc == 1:
			print('O PC escolheu pedra')
		elif pc == 2:
			print('O PC escolheu Papel')
		elif pc == 3:
			print('O PC escolheu Tesoura')

		print()

		if jog == pc:
			print('EMPATE')
			p_jog = p_jog + 1
			p_pc = p_pc + 1
		elif jog == 1 and pc == 2:
			print('VOCÊ PERDEU')
			p_pc = p_pc + 3
		elif jog == 1 and pc == 3:
			print('VOCÊ GANHOU')
			p_jog = p_jog +3
		elif jog == 2 and pc == 1:
			print('VOCÊ GANHOU')
			p_jog = p_jog + 3
		elif jog == 2 and pc == 3:
			print('VOCÊ PERDEU')
			p_pc = p_pc + 3
		elif jog == 3 and pc == 1:
			print('VOCÊ PERDEU')
			p_pc = p_pc + 3
		elif jog == 3 and pc == 2:
			print('VOCÊ GANHOU')
			p_jog = p_jog + 3
		print()
		print('==============PONTOS==================')
		print('-',nome,':',p_jog,'PONTOS')
		print('- PC :',p_pc,'PONTOS')
		print('======================================')
		jn = input('Quer jogar novamente?(S/N) ')
		jn = jn.upper()
elif pvp == 'M':
	nome1 = input('Digite o nome do player 1: ')
	nome2 = input('Digite o nome do player 2: ')
	print()
	print(''''==============REGRAS==================
    	- Pedra ganha da tesoura (amassando-a ou quebrando-a).
    	- Tesoura ganha do papel (cortando-o).
    	- Papel ganha da pedra (embrulhando-a).

    	A cada vitoria o jogador ganha 3 PONTOS
    	A cada empate os jogadores gannham 1 PONTO''')

	jn = 'S'
	while jn == 'S':
		print('''Escolha:
    		1 - Pedra
    		2 - Papel
    		3 - Tesoura
    		''')
		jog1 = int(input('-', nome1,',Sua vez de jogar? '))
		os.system('cls')
		jog2 = int(input('Sua vez de jogar,'))

		if jog == 1:
			print('O Jogador escolheu pedra')
		elif jog == 2:
			print('O Jogador escolheu Papel')
		elif jog == 3:
			print('O Jogador escolheu Tesoura')
		else:
			print('ERRO, Comando invlido')

		if pc == 1:
			print('O PC escolheu pedra')
		elif pc == 2:
			print('O PC escolheu Papel')
		elif pc == 3:
			print('O PC escolheu Tesoura')

		print()

		if jog == pc:
			print('EMPATE')
			p_jog = p_jog + 1
			p_pc = p_pc + 1
		elif jog == 1 and pc == 2:
			print('VOCÊ PERDEU')
			p_pc = p_pc + 3
		elif jog == 1 and pc == 3:
			print('VOCÊ GANHOU')
			p_jog = p_jog + 3
		elif jog == 2 and pc == 1:
			print('VOCÊ GANHOU')
			p_jog = p_jog + 3
		elif jog == 2 and pc == 3:
			print('VOCÊ PERDEU')
			p_pc = p_pc + 3
		elif jog == 3 and pc == 1:
			print('VOCÊ PERDEU')
			p_pc = p_pc + 3
		elif jog == 3 and pc == 2:
			print('VOCÊ GANHOU')
			p_jog = p_jog + 3
		print()
		print('==============PONTOS==================')
		print('-', nome, ':', p_jog, 'PONTOS')
		print('- PC :', p_pc, 'PONTOS')
		print('======================================')
		jn = input('Quer jogar novamente?(S/N) ')
		jn = jn.upper()

print ('Fim do programa')
