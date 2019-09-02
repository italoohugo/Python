print('Programa PyIdade em anos e meses')

nome = input('Por favor, Digite seu nome: ')
nasc = int(input('Digite seu ano de nascimento: '))
ano = int(input('Ando meio esquecido, em que anos estamos? '))
idade = ano - nasc
meses = idade * 12

print(nome,', Pelas minhas contas, neste ano(',ano,') você completa',idade,"anos")
print(nome,', você tem',meses,'meses de vida')