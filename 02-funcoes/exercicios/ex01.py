import random

def numeroAleatorio():
    numero_aleatorio = random.randint(1, 100)
    return numero_aleatorio

def adivinhacao():
    palpite = numeroAleatorio()
    while True:
        try:
            numero = int(input("Digite um número: "))
            if numero == palpite:
                print("Parabéns, você ganhou!")
                break
            elif numero > palpite:
                print("Seu palpite foi alto. Informe outro número. ")
            elif numero < palpite:
                print("Seu palpite foi baixo. Informe outro número")
        except ValueError:
                print("Número inválido. ")

adivinhacao()