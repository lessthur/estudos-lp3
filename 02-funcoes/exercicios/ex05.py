def verificaPalindromo(palavra):
    #invertendo a palavra utilizando fatiamento reverso
    palindromo = palavra[::-1] 
    if palavra == palindromo:
        print("A palavra é um palíndromo!")
    else:
        print("A palavra não é um palíndromo!")
        
palavra = input("Digite uma palavra: ")
verificaPalindromo(palavra)