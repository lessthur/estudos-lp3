def exibeTabuada(numero):
    for i in range (1,11):
        print(numero, "*", i, "=", (numero * i))

numero = int(input("Digite um número para ver sua tabuada de 1 a 10: "))
exibeTabuada(numero)