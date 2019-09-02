print('Programa PyIdade, sua idade em anos, meses, semanas e dias')

nome = input('Por favor, Digite seu nome: ')
nasc = int(input('Digite seu ano de nascimento: '))
ano = int(input('Ando meio esquecido, em que anos estamos? '))
idade = ano - nasc
meses = idade * 12
semanas = idade * 52
dias = idade * 365
print(nome,', Pelas minhas contas, neste ano(',ano,') você completa',idade,"anos.")
print(nome,', você tem',meses,'meses de vida.')
print(nome,',você tem',semanas,'semanas de vida.')
print(nome,',você tem',dias,'dias de vida.')
