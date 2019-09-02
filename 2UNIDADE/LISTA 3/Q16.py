frase = list ("o rato roeu a roupa do rei de roma")
print ("frase:", frase)
for x in range(len(frase)):
    if (frase[x] == ' '):
        frase[x] = '-'
print ("frase:", frase)

#RESPOSTA:  O programa substitui os espaços na frase por traços