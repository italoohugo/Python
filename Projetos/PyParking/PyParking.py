contatos = {}
clientes = {}
opcao = 0

def veriNome(nome,aux):
	if aux == 2:
		for i in range(len(nome)):
			if (ord(nome[i])) in range(65,91) or (ord(nome[i])) in range(97,123) or ord(nome[i]) == 45 or ord(nome[i]) == 231 or ord(nome[i]) == 32 or (nome == ""):
				print("\n-----------------------------------------------")
				print("      Nome do cliente só pode conter letras      ")
				print("-----------------------------------------------\n")
				aux = 2
	else:
		aux = 1
	return (aux,nome)

def menu_inicial ():
	print("1 - Cadastrar cliente")
	print("2 - Cadastrar entrada de veiculo")
	print("3 - listar veiculos")
	print("4 - Registrar saida de veiculo")
	print("5 - Busca por veiculo")
	print("6 - Dados do cliente:")
	print("7 - Sair")
	print('')

while opcao !="5":
	menu_inicial()
	opcao = input("Digite sua opção: ")
	if opcao == '1': #Cadastrar clientes
		aux = 2

		while aux == 2:
			nome = input('Digite o nome do cliente:')
			veriNome(nome,aux)

		modelo =input("Digite o modelo do veiculo: ")
		cor= input('Digite a cor do veiculo:')
		clientes[nome] = [modelo,cor]
		print("Veiculo cadastrado com sucesso!")
		
		
	elif opcao == "2": #Cadastrar veiculos 
		placa = input("Digite a placa do veiculo: ")
		modelo =input("Digite o modelo do veiculo: ")
		cor= input('Digite a cor do veiculo:')
		marca=input('Digite a marca do veiculo: ')
		hora=input('Digite a hora de entrada do veiculo:')
		contatos[placa] = [modelo,cor,marca,hora]
		print('-------------------------------')
		print("Veiculo cadastrado com sucesso!")
		print('-------------------------------')
		print('')
	elif opcao == '3': #Listar veiculos
		placa = input("Digite a placa do veiculo: ")		
		if placa not in contatos:
			print('-----------------------')
			print("veiculo não cadastrado!")
			print('-----------------------')
		else:
			print('Placa do veiculo:',placa)
			print('Modelo do veiculo:',contatos[placa][0])
			print('Cor do veiculo:',contatos[placa][1])
			print('Marca do veiculo:',contatos[placa][2])
			print('Hora de entrada do veiculo na estacionamento:',contatos[placa][3])
			print('-----------------------')
			print("Veiculo cadastrado!")
			print('-----------------------')
			print('')
	elif opcao == '4': #Registrar saída de veiculo 
		placa = input("Digite a placa do veiculo: ")
		if placa in contatos:
			del contatos[placa]
			print('--------------------------------')
			print(placa, " saiu do estacionamento!")
			print('--------------------------------')
			print('')
		else:
			print('-----------------------')
			print(placa,'Não cadastrado')
			print('-----------------------')
	elif opcao=='5': #Buscar veiculo 
		placa1=input('Qual a placa do veiculo a procurar:')
		for placa in contatos:
			print('placa do veiculo:',placa)
			print('modelo do veiculo:',contatos[placa][0])
			print('cor do veiculo:',contatos[placa][1])
			print('marca do veiculo:',contatos[placa][2])
			print('hora de entrada do veiculo na estacionamento:',contatos[placa][3])
	elif opcao== '6': #Dados do cliente
		print()
	elif opcao == '7': #sair
		print('-------------------------------------------------------')
		print("Usuário saiu do programa de controle de estacionamento!")
		print('-------------------------------------------------------')
		opcao='5'
	else:
		print('-------------------------------')
		print('Voçê digitou um valor invalido!')
		print('-------------------------------')
