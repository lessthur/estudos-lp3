votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0

def votacao():
    global votos_candidato1, votos_candidato2, votos_candidato3
    votos_candidato1 = 0 
    votos_candidato2 = 0
    votos_candidato3 = 0
    for i in range(1,8):
        print("Digite o número do candidato em que deseja votar: ")
        voto = int(input("1 - Candidato 1 | 2 - Candidato 2 | 3 - Candidato 3\n"))
        if(voto == 1 or voto == 2 or voto == 3):
            i = i + 1
            if(voto == 1):
                print("Voto para Candidato 1")
                votos_candidato1 += 1
            elif(voto == 2):
                print("Voto para Candidato 2")
                votos_candidato2 += 1
            elif(voto == 3):
                print("Voto para Candidato 3")
                votos_candidato3 += 1
            else:
                print("Erro")
        else: 
            print("Digite um número válido! (1, 2 ou 3)")
    print("Votação finalizada.")
    
def comparacao():
    if(votos_candidato1 > votos_candidato2 and votos_candidato1 > votos_candidato3):
        print("O candidato 1 ganhou! Quantidade de votos: ", votos_candidato1)
    elif(votos_candidato2 > votos_candidato1 and votos_candidato2 > votos_candidato3):
        print("O candidato 2 ganhou! Quantidade de votos: ", votos_candidato2)
    elif(votos_candidato3 > votos_candidato1 and votos_candidato3 > votos_candidato2):
        print("O candidato 3 ganhou! Quantidade de votos: ", votos_candidato3)
    else:
        print("Houve um empate! Haverá outra votação.")
        votacao()
        comparacao()
        
votacao()
comparacao()