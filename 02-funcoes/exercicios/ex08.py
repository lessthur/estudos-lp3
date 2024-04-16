def fraseParaDict(frase):
    dicionario = {}
    palavras = frase.split()
    
    for palavra in palavras:
        '''
        se a palavra já existir na lista (dicionario)
        somar 1 ao número de vezes em que a palavra aparece (valor)
        '''
        if palavra in dicionario:
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1
    
    return dicionario

frase = input("Digite uma frase: ")
dicionario = fraseParaDict(frase)
print(dicionario)