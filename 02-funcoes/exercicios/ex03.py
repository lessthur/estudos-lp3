vogais = 0
consoantes = 0

def separaVogalConsoante(frase):
    global vogais
    global consoantes
    for letra in frase:
        if(letra.isalpha()):
            letra = letra.capitalize()
            if(letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U"):
                vogais += 1
            else:
                consoantes += 1
            
frase = input("Digite uma frase: ")
frase = frase.strip()

separaVogalConsoante(frase)

print("Quantidade de vogais = ", vogais)
print("Quantidade de consoantes = ", consoantes)
