tarefas = []
print('CADASTRO DE TAREFAS')
quant = int(input('Quantas tarefas irá cadastrar? '))
cont = 1
for i in range(quant):
    tarefa = []
    print('TAREFA ',cont)
    ident = str(input('Digite o identificador da tarefa: '))
    descricao = str(input('Digite uma descrição para a tarefa: '))
    status = int(input('Digite o status: (1 para “Realizada” e 0 para “Pendente)'))
    print()
    tarefa.append(ident)
    tarefa.append(descricao)
    tarefa.append(status)
    tarefas.append(tarefa)
    cont += 1

print('MOSTRAR TAREFAS')
for j in range(len(tarefas)):
    print(tarefas[j])