palavra = "celular"
letras_usuario = []
chances = 6
ganhou = False
tentativa = ''

def verificaExibeLetras():
    global palavra
    global letras_usuario
    global chances
    global ganhou
    global tentativa

    for letra in palavra:
        if letra.lower() in letras_usuario:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print(f"Você tem {chances} chances")

    tentativa = input("Escolha uma letra para adivinhar: ")
    letras_usuario.append(tentativa.lower())

def gameVitoriaDerrota():
    global palavra
    global letras_usuario
    global chances
    global ganhou
    global tentativa

    '''
    - se a letra não está contida na palavra, diminuir uma chance
    - o jogo é encerrado quando a pessoa ganha ou perde
    - caso as chances forem esgotadas, o jogo é encerrado em derrota
    '''

    while True:
        verificaExibeLetras()
        if tentativa.lower() not in palavra.lower():
            chances -= 1
        ganhou = True

        for letra in palavra:
            if letra.lower() not in letras_usuario:
                ganhou = False

        if chances == 0 or ganhou:
            break

    if ganhou:
        print(f"Parabéns, você ganhou. A palavra era: {palavra}")
    else:
        print(f"Você perdeu! A palavra era: {palavra}")

gameVitoriaDerrota()
