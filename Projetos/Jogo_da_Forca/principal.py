import random
from boneco import enforcamento

print('---------------------------')
print('------ JOGO DA FORCA ------')
print('---------------------------')
print()

########## LISTAS  E VARIAVEIS PARA LER E GRAVAR #########

usuarios = []
senhas = []
pontos = []
codigos = []

user = ''
codigo = 0
ponts = 0

############# LEITURA ##############

arquivo = open('usuarios.txt','r')
for linha in arquivo:
    linha = linha.replace('\n','')
    usuarios.append(linha)
arquivo.close()

arquivo = open('senhas.txt','r')
for linha in arquivo:
    linha = linha.replace('\n','')
    senhas.append(linha)
arquivo.close()

arquivo = open('pontos.txt','r')
for linha in arquivo:
    linha = linha.replace('\n','')
    linha = int(linha)
    pontos.append(linha)
arquivo.close()

arquivo = open('codigos.txt','r')
for linha in arquivo:
    linha = linha.replace('\n','')
    linha = int(linha)
    codigos.append(linha)
arquivo.close()

###################################################

def validar_tema():
    global tema
    while True:
        numero = (input('RESPOSTA: '))
        if numero == '1' or numero == '2' or numero == '3' or numero == '4' or numero == '5' or numero == '6' or numero == '7' or numero == '8' or numero == '0':
            break
        else:
            print('''COMANDO INVALIDO 
            DIGITE UM NUMERO ENTRE 1 E 8''')
            continue
    tema = int(numero)

######################################################

def validar_jogada():
    global jogada
    COM_ACENTOS = ['Ç', 'Á', 'À', 'Ã', 'Â', 'Ä', 'É', 'È', 'Ê', 'Ë', 'Í', 'Ì', 'Î', 'Ï', 'Ó', 'Ò', 'Õ', 'Ô', 'Ö',
                   'Ú', 'Ù', 'Û', 'Ü']
    SEM_ACENTOS = ['C', 'A', 'A', 'A', 'A', 'A', 'E', 'E', 'E', 'E', 'I', 'I', 'I', 'I', 'O', 'O', 'O', 'O', 'O',
                   'U', 'U', 'U', 'U']
    aux = 0
    while True:
        jogada = str(input('DIGITE SUA JOGADA: ')).upper()
        for acento in COM_ACENTOS:
            if acento == jogada:
                jogada = SEM_ACENTOS[aux]
            aux += 1
        if jogada == 'A' or jogada == 'B' or jogada == 'C' or jogada == 'D' or jogada == 'E' or jogada == 'F' or jogada == 'G' or jogada == 'H' or jogada == 'I' or jogada == 'J' or jogada == 'K' or jogada == 'L' or jogada == 'M' or jogada == 'N' or jogada == 'O' or jogada == 'P' or jogada == 'Q' or jogada == 'R' or jogada == 'S' or jogada == 'T' or jogada == 'U' or jogada == 'V' or jogada == 'X' or jogada == 'W' or jogada == 'Y' or jogada == 'Z':
            break
        else:
            print('''COMANDO INVALIDO 
                DIGITE UMA LETRA DO ALFABETO''')
            continue
    return jogada


######################################################

def validar_login_registrar():
    global login_registrar
    while True:
        login_registrar = (input('RESPOSTA: '))
        if login_registrar == '1' or login_registrar == '2' or login_registrar == '3' or login_registrar == '0':
            break
        else:
            print('''COMANDO INVALIDO 
                DIGITE SOMENTE 1,2,3 OU 0''')
            continue
    return login_registrar

######################################################
def registrar_user(usuarios):
    global user
    while True:
        cond2 = False
        cond = False
        user = (input('USUARIO: ')).upper()
        for letra in user:
            if letra in 'ABCDEFGHIJKLMNOPQRSTUVXWYZ0123456789':
                cond = True
            else:
                cond = False
        for usuario in usuarios:
            if usuario == user:
                cond2 = True
        if cond2 == True:
            print('ERRO: ESTE NOME DE USUARIO JÁ EXISTE')
            continue
        if cond == True:
            break
        if cond == False:
            print('''ERRO: DIGITE APENAS LETRAS OU NUMEROS''')
            continue

    return user

######################################################

def registrar_senha():
    global senha_r
    cond = False
    while True:
        senha_r = (input('SENHA: ')).upper()
        for letra in senha_r:
            if letra in 'ABCDEFGHIJKLMNOPQRSTUVXWYZ0123456789':
                cond = True
            else:
                cond = False
        if cond == True:
            break
        if cond == False:
            print('''ERRO: DIGITE APENAS LETRAS OU NUMEROS''')
            continue
    return user

######################################################
def login_usuario(usuarios):
    global user
    global codigo
    cond = False
    while True:
        user = (input('USUARIO: ')).upper()
        if user == '0':
            break
        cod = -1
        for usuario in usuarios:
            cod+=1
            if user == usuario:
                cond = True
                codigo = cod
        if cond == True:
            break
        if cond == False:
            print('ERRO: DIGITE UM USUARIO EXISTENTE')
            continue
    return codigo,user

######################################################
def login_senha(senhas,codigo):
    global password
    while True:
        password = input('SENHA: ').upper()
        if password == '0':
            break
        if password ==senhas[codigo]:
            break
        else:
            print('ERRO: SENHA INCORRETA, TENTE NOVAMENTE!')
            continue
    return password

######################################################

def jogar_novamente():
    global jogar
    while True:
        jogar = input("QUER JOGAR NOVAMENTE? (S/N)").upper()
        if jogar == 'S' or jogar == 'N':
            break
        else:
            print('ERRO: COMANDO INVALIDO, DIGITE APENAS "S" OU "N" ')
            continue
    return jogar

######################################################

############### LISTAS SEM ACENTOS##################

frutas = ['MELAO','UVA','MANGA','AMENDOA','KIWI','CACAU','CAQUI','BANANA','AMEIXA','MELANCIA','ACEROLA','CAJU','ACAI','MAMAO','MARACUJA','ROMA','GUARANA','JABUTICABA','GOIABA']
peixes = ['SARDINHA','PINTADO','PESCADA','GAROUPA','PIRARUCU','LAMBARI','LINGUADO','PANGA','BARBADO','BAGRE','PARGO','BONITO','BAIACU','NAMORADO','ENGUIA','TRAIRA','CARPA','TRUTA','ATUM','PACU']
cores = ['PRETO','LARANJA','MAGENTA','VINHO','LIMAO','DOURADO','MARROM','AMARELO','CINZA','BEGE','ROSA','CREME','GRENA','VIOLETA','VERDE','LILAS','VERMELHO','BRANCO','AZUL','ROXO']
futebol = ['CLUBE','CHUTE','PENALTI','CHUTEIRA','BOLA','ATACANTE','CAMPEONATO','ESCANTEIO','JOGO','GOL','TITULAR','CAMPO','GOLEIRO','ESTADIO','TRAVE','FRANGO','JUIZ','DRIBLE','TORCEDOR','BANDEIRA']
esportes = ['TIRO','JUDO','VOLEIBOL','TENIS','FUTEBOL','ATLETISMO','PENTATLO','ESGRIMA','TAEKWONDO','NATACAO','VELA','CANOAGEM','BOXE','BADMINTON','REMO','BASQUETE','TRIATLO','CICLISMO','HANDEBOL','HIPISMO']
capitais = ['GOIANIA','CURITIBA','VITORIA','FLORIANOPOLIS','BRASILIA','TERESINA','RECIFE','CUIABA','ARACAJU','NATAL','MACAPA','FORTALEZA','MANAUS','BELEM','PALMAS','MACEIO','SALVADOR']
instrumentos = ['PANDEIRO','BATERIA','PIANO','GUITARRA','MARACA','CAVAQUINHO','TAMBORIM','BAIXO','BANDOLIM','GAITA','BERIMBAU','TAMBOR','VIOLAO','OBOE','CUICA','FLAUTA','BANJO','VIOLINO','CHOCALHO','CLARINETE']
corpo = ['OLHOS','CRANIO','BEXIGA','JOELHO','BOCA','NARIZ','LARINGE','RINS','AXILA','INTESTINO','CÉREBRO','GORDURA','PANTURRILHA','SOBRANCELHAS','ESQUELETO','PELE','COSTELAS','TRAQUEIA','DENTES','UMBIGO']

############### LISTAS COM ACENTOS##################
A_frutas = ['MELÃO','UVA','MANGA','AMÊNDOA','KIWI','CACAU','CAQUI','BANANA','AMEIXA','MELANCIA','ACEROLA','CAJU','AÇAÍ','MAMÃO','MARACUJÁ','ROMÃ','GUARANÁ','JABUTICABA','GOIABA']
A_peixes = ['SARDINHA','PINTADO','PESCADA','GAROUPA','PIRARUCU','LAMBARI','LINGUADO','PANGA','BARBADO','BAGRE','PARGO','BONITO','BAIACU','NAMORADO','ENGUIA','TRAÍRA','CARPA','TRUTA','ATUM','PACU']
A_cores = ['PRETO','LARANJA','MAGENTA','VINHO','LIMÃO','DOURADO','MARROM','AMARELO','CINZA','BEGE','ROSA','CREME','GRENÁ','VIOLETA','VERDE','LILÁS','VERMELHO','BRANCO','AZUL','ROXO']
A_futebol = ['CLUBE','CHUTE','PENALTI','CHUTEIRA','BOLA','ATACANTE','CAMPEONATO','ESCANTEIO','JOGO','GOL','TITULAR','CAMPO','GOLEIRO','ESTÁDIO','TRAVE','FRANGO','JUIZ','DRIBLE','TORCEDOR','BANDEIRA']
A_esportes = ['TIRO','JUDÔ','VOLEIBOL','TÊNIS','FUTEBOL','ATLETISMO','PENTATLO','ESGRIMA','TAEKWONDO','NATAÇÃO','VELA','CANOAGEM','BOXE','BADMINTON','REMO','BASQUETE','TRIATLO','CICLISMO','HANDEBOL','HIPISMO']
A_capitais = ['GOIÂNIA','CURITIBA','VITÓRIA','FLORIANÓPOLIS','BRASÍLIA','TERESINA','RECIFE','CUIABÁ','ARACAJÚ','NATAL','MACAPÁ','FORTALEZA','MANAUS','BELÉM','PALMAS','MACEIÓ','SALVADOR']
A_instrumentos = ['PANDEIRO','BATERIA','PIANO','GUITARRA','MARACA','CAVAQUINHO','TAMBORIM','BAIXO','BANDOLIM','GAITA','BERIMBAU','TAMBOR','VIOLÃO','OBOÉ','CUÍCA','FLAUTA','BANJO','VIOLINO','CHOCALHO','CLARINETE']
A_corpo = ['OLHOS','CRÂNIO','BEXIGA','JOELHO','BOCA','NARIZ','LARINGE','RINS','AXILA','INTESTINO','CÉREBRO','GORDURA','PANTURRILHA','SOBRANCELHAS','ESQUELETO','PELE','COSTELAS','TRAQUEIA','DENTES','UMBIGO']

################# MENU PRINICPAL ######################
login_registrar = '3'
tema = 0
while tema == 0:
    print('''--------------------LOGIN-----------------------------
- ANTES DE COMEÇAR A JOGAR FAÇA LOGIN OU REGISTRE-SE -
------------------------------------------------------''')
    print('1 - ENTRAR')
    print('2 - REGISTRAR')
    print('3 - PONTUAÇÕES')
    print()
    print('0 - SAIR')
    print()
    validar_login_registrar()
    if login_registrar =='0':
        break
                ##################  LOGIN ##################
    if login_registrar == '1':
        print()
        print('''----------------------ENTRAR--------------------------''')
        print('---------DIGITE 0 PARA VOLTAR AO MENU PRINCIPAL---------')
        login_usuario(usuarios)
        if user =='0':
            continue
        login_senha(senhas, codigo)
        if password == '0':
            continue
                ################# REGISTRO DE USUARIO ######################
    if login_registrar == '2':
        print()
        print('''--------------------REGISTRAR-------------------------''')
        registrar_user(usuarios)
        usuarios.append(user)
        registrar_senha()
        senhas.append(senha_r)
        codigos.append(len(codigos))
        pontos.append(0)
        codigo = len(codigos)-1
        print('USUARIO CADASTRADO COM SUCESSO')

        ###################SALVAR#######################
        arquivo = open('usuarios.txt', 'w')
        for linha in usuarios:
            linha = linha.upper()
            arquivo.write(linha + '\n')
        arquivo.close()

        arquivo = open('senhas.txt', 'w')
        for linha in senhas:
            linha = linha.upper()
            arquivo.write(linha + '\n')
        arquivo.close()

        arquivo = open('pontos.txt', 'w')
        for linha in pontos:
            linha = str(linha)
            arquivo.write(linha + '\n')
        arquivo.close()

        arquivo = open('codigos.txt', 'w')
        for linha in codigos:
            linha = str(linha)
            arquivo.write(linha + '\n')
        arquivo.close()
        ################################################

    if login_registrar == '3':
        print()
        print('''---------------------PONTUAÇÕES------------------------''')
        tamanho = len(usuarios)
        aux = 0
        while tamanho != aux:
            print('- NOME:',usuarios[aux],';',pontos[aux],'PONTOS')
            aux+=1
        print('-------------------------------------------------------')
        print()
        continue



    ################# MENU DO JOGO ######################
    while True:
        print('------------------------------------------------------')
        print('------------------------------------------------------')
        print(' ',user,', BEM VINDO AO JOGO DA FORCA')
        print('''
            - O jogo da forca é um jogo em que o jogador tem que acertar qual é a palavra proposta,
            tendo como dica o número de letras e o tema ligado à palavra. 
            - A cada letra errada, é desenhada uma parte do corpo do enforcado.
            - Você só pode errar no maximo 6 vezes.
            - A cada vez que você errar irá perder 1 ponto.
            - Se não errar irá ganhar 6 pontos.
            - Se você for enforcado ficará com 0 pontos.
               ''')
        print('''-------------------ESCOLHA UM TEMA--------------------
        1 - Frutas
        2 - Peixes
        3 - Cores
        4 - Futebol
        5 - Esportes
        6 - Capitais
        7 - Instrumentos
        8 - Corpo 
        
        0 - VOLTAR P/ MENU PRINCIPAL
        ''')
        #################  ######################
        tema = 1
        validar_tema()

        #tema = int(input('TEMA: '))
        print()

        sorteio = 0
        if tema == 0:
            break
        if tema == 1:
            print()
            sorteio = random.randint(0,len(frutas))
            L = (frutas[sorteio-1])
            palavra_sorteada = (A_frutas[sorteio - 1])
            TEMA = 'FRUTAS'
        elif tema == 2:
            print()
            sorteio = random.randint(0,len( peixes))
            L = (peixes[sorteio-1])
            palavra_sorteada = (A_peixes[sorteio - 1])
            TEMA = 'PEIXES'
        elif tema == 3:
            print()
            sorteio = random.randint(0,len( cores))
            L = (cores[sorteio-1])
            palavra_sorteada = (A_cores[sorteio - 1])
            TEMA = 'CORES'
        elif tema == 4:
            print()
            sorteio = random.randint(0,len( futebol))
            L = (futebol[sorteio-1])
            palavra_sorteada = (A_futebol[sorteio - 1])
            TEMA = 'FUTEBOL'
        elif tema == 5:
            print()
            sorteio = random.randint(0,len( esportes))
            L = (esportes[sorteio-1])
            palavra_sorteada = (A_esportes[sorteio - 1])
            TEMA = 'ESPORTES'
        elif tema == 6:
            print()
            sorteio = random.randint(0,len( capitais))
            L = (capitais[sorteio-1])
            palavra_sorteada = (A_capitais[sorteio - 1])
            TEMA = 'CAPITAIS'
        elif tema == 7:
            print()
            sorteio = random.randint(0,len( instrumentos))
            L = (instrumentos[sorteio-1])
            palavra_sorteada = (A_instrumentos[sorteio - 1])
            TEMA = 'INSTRUMENTOS'
        elif tema == 8:
            print()
            sorteio = random.randint(0,len( corpo))
            L = (corpo[sorteio-1])
            palavra_sorteada = (A_corpo[sorteio - 1])
            TEMA = 'CORPO'

        #######################################################


        #INICIO DO JOGO
        acertos = []
        digitados = []
        forca = 6
        ponts_jogo = 6
        vitoria = 0
        letras =0
        for quant in L:
            letras += 1
        while True:
            senha = ""

            #########################
            for j in L:
                senha += j if j in acertos else '_ '

            #########################
            print('--- TEMA:',TEMA,'---')
            print('LETRAS:',letras)
            print('>',senha,'<')
            print()

            #########CONDIÇÃO DE VITORIA########
            if L == senha:
                ponts += ponts_jogo
                print('---PARABÉNS, VOCÊ VENCEU---')
                break

            validar_jogada()


            ##########################
            if jogada in digitados:
                print("Você já tentou esta letra!")
                print()
                continue
            else:
                digitados+=jogada
                if jogada in L:
                    acertos+=jogada
                else:
                    forca-=1
                    ponts_jogo-=1
                    print('---VOCÊ ERROU---')
            enforcamento(forca)


            ####CONDIÇÃO DE DERROTA####

            if forca == 0:
                print('---ENFORCADO---')
                print('---PALAVRA CORRETA: ',palavra_sorteada)
                ponts +=ponts_jogo
                break

        #############JOGAR NOVAMENTE###############
        print()
        jogar_novamente()
        if jogar == 'S':
            continue
        else:
            break

    ############CONTABILIZADOR DE PONTOS############
    pontos[codigo] = ponts + pontos[codigo]

    ##################PONTUAÇÃO#####################
    print('-----PONTUAÇÃO DESSA PARTIDA-----')
    print('- NOME:',user)
    print('- PONTOS:',ponts,'PONTOS')
    print('---------------------------------')

    ################################################

###################SALVAR#######################
arquivo = open('usuarios.txt','w')
for linha in usuarios:
    linha = linha.upper()
    arquivo.write(linha+'\n')
arquivo.close()

arquivo = open('senhas.txt','w')
for linha in senhas:
    linha = linha.upper()
    arquivo.write(linha+'\n')
arquivo.close()

arquivo = open('pontos.txt','w')
for linha in pontos:
    linha = str(linha)
    arquivo.write(linha+'\n')
arquivo.close()

arquivo = open('codigos.txt','w')
for linha in codigos:
    linha = str(linha)
    arquivo.write(linha+'\n')
arquivo.close()
################################################