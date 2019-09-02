print('Programa data em que cairá o Domingo de Páscoa')

ano = float(input('Digite o ano entre 1982 e 2048: '))
if ano >= 1982 and ano <= 2048:
    # Calculo
    a = ano % 19
    b = ano % 4
    c = ano % 7
    d = ((a * 19) + 24) % 30
    e = ((b*2)+(c*4)+(d*6)+5) % 7
    f = d + e
    resultado = 22 + f
    if resultado > 31:
        pascoa = resultado - 31
        mes = 4
    else:
        pascoa = resultado
        mes = 3
    #print('O domingo de pascoa será dia',pascoa,'/',mes,'/',ano)
    print('O domingo de pascoa será dia %.f / %.f / %.f' %(pascoa,mes,ano))
else:
    print('Ano invalido')