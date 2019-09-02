########################################################################
# Programa para calcular a nota do aluno/a no SISU-UFRN para cada uma  #
# das área de conhecimento, a partir das notas obtidas pelo/a aluno/a  #
# na prova do ENEM. O/A aluno/a deve informar as notas obtidas em cada #
# uma das provas para o cálculo da nota final em cada área.            #
#                                                                      #
# Desenvolvido por @flgorgonio, Fev/2017 - UFRN/CERES/DCT              #
########################################################################

print('Programa para Calcular a sua Nota no SISU-UFRN')
print('A seguir, informe suas notas do ENEM, em cada prova: ')
print()
notaLinguagens = float(input('Qual a sua nota em Linguagens? '))
notaMatematica = float(input('Qual a sua nota em Matemática? '))
notaHumanas = float(input('Qual a sua nota em Ciências Humanas? '))
notaNatureza = float(input('Qual a sua nota em Ciências da Natureza? '))
notaRedacao = float(input('Qual a sua nota em Redação? '))
print()
print('= = = = = = = = = = Área de Biomédicas = = = = = = = = = =')
pesoLinguagens = 1.5
pesoMatematica = 1.0
pesoHumanas = 1.5
pesoNatureza = 3.0
pesoRedacao = 1.5
biomedica = (notaLinguagens * pesoLinguagens + notaMatematica * pesoMatematica + notaHumanas * pesoHumanas + notaNatureza * pesoNatureza + notaRedacao * pesoRedacao) / (pesoLinguagens + pesoMatematica + pesoHumanas + pesoNatureza + pesoRedacao)
print('Sua nota final para a área de Biomédicas é: ', biomedica)
print()
print()
print('= = = = = = = = = = Área de Humanística I = = = = = = = = = =')
pesoLinguagens = 2.0
pesoMatematica = 2.0
pesoHumanas = 2.0
pesoNatureza = 1.0
pesoRedacao = 1.5
humanistica1 = (notaLinguagens * pesoLinguagens + notaMatematica * pesoMatematica + notaHumanas * pesoHumanas + notaNatureza * pesoNatureza + notaRedacao * pesoRedacao) / (pesoLinguagens + pesoMatematica + pesoHumanas + pesoNatureza + pesoRedacao)
print('Sua nota final para a área de Humanística I é: ', humanistica1)
print()
print()
print('= = = = = = = = = = Área de Humanística II = = = = = = = = = =')
pesoLinguagens = 2.5
pesoMatematica = 1.0
pesoHumanas = 2.5
pesoNatureza = 1.0
pesoRedacao = 1.5
humanistica2 = (notaLinguagens * pesoLinguagens + notaMatematica * pesoMatematica + notaHumanas * pesoHumanas + notaNatureza * pesoNatureza + notaRedacao * pesoRedacao) / (pesoLinguagens + pesoMatematica + pesoHumanas + pesoNatureza + pesoRedacao)
print('Sua nota final para a área de Humanística II é: ', humanistica2)
print()
print()
print('= = = = = = = = = = Área de Tecnológica I = = = = = = = = = =')
pesoLinguagens = 1.0
pesoMatematica = 2.0
pesoHumanas = 2.0
pesoNatureza = 2.0
pesoRedacao = 1.5
tecnologica1 = (notaLinguagens * pesoLinguagens + notaMatematica * pesoMatematica + notaHumanas * pesoHumanas + notaNatureza * pesoNatureza + notaRedacao * pesoRedacao) / (pesoLinguagens + pesoMatematica + pesoHumanas + pesoNatureza + pesoRedacao)
print('Sua nota final para a área de Tecnológica I é: ', tecnologica1)
print()
print()
print('= = = = = = = = = = Área de Tecnológica II = = = = = = = = = =')
pesoLinguagens = 1.0
pesoMatematica = 3.0
pesoHumanas = 1.0
pesoNatureza = 2.0
pesoRedacao = 1.5
tecnologica2 = (notaLinguagens * pesoLinguagens + notaMatematica * pesoMatematica + notaHumanas * pesoHumanas + notaNatureza * pesoNatureza + notaRedacao * pesoRedacao) / (pesoLinguagens + pesoMatematica + pesoHumanas + pesoNatureza + pesoRedacao)
print('Sua nota final para a área de Tecnológica II é: ', tecnologica2)
print()
print()
