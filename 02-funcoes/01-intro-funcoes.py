# Função

# Quero somar uma lista de números 
# Usar a função sum()

# Quero calcular a média de notas dos alunos
# 1. Tem no Python?
# 2. Alguém já programou? (copiar ou adocopmar dependência)
# 3. Declarar 

# 1. Declaração
# def nome_funcao(parametro1, parametro2)
#       return valor 


# 2. Chamada
print ('olá')
sum ([1, 3, 5])
# nome_funcao('dad', 1)

# Função sem retornos e sem parâmetros
def imprimir_mensagem():
    print('Opa')

print("Função imprimir mensagem: ")
imprimir_mensagem()
imprimir_mensagem()

# Função sem retornos e com parâmetros
# parâmetros vs argumentos
def saudacoes(nome):
    print(f'Bom dia {nome}')

print("Função saudações: ")
# Argumento para parâmetro nome 'thur'
saudacoes('thur')

# Argumento para parâmetro nome 
nome_sla = 'tutu'
saudacoes(nome_sla)

# Função com retornos e sem parâmetros
def obter_mensagem():
    return "opaaaaa"

mensagem = obter_mensagem
print(mensagem)

print (obter_mensagem)

# Função com retornos e com parâmetros
def gerar_saudacao(nome):
    return f'Bom dia {nome}'

print(gerar_saudacao('thurzin'))
print(gerar_saudacao('tuts'))

# Retorno   &   Parâmetro
# não           não
# sim           não
# não           sim
# sim           sim (adequado)

# Imprimir saudação 
# Saudação = frase (dinâmica) nome (dinâmico)
# "Bom dia Pedro"
# "Boa tarde Maria"
# "Boa noite Maria"

def saudacao(nome, frase):
    print(f'{frase} {nome}')

saudacao('thur', 'bom dia')

def saudacao(nome, frase):
    return f'{frase} {nome}'

print(saudacao('thur', 'bom dia')) # melhor

# Enviar email saudacao
# Criar uma carta em pdf

# Entrada
todas_as_notas = [
    [9.0, 7.0, 3.0],
    [10.0, 4.0, 5.0],
    [8.0, 8.0, 2.0]
]

# Saída [5.5, 1.0, 6.6]

def calcular_media(notas):
    return sum(notas) / len(notas)

def calcular_media_alunos(notas_alunos):
    #medias = []

    #for notas in notas_alunos:
    #    media = calcular_media(notas)
    #    medias.append(media)

    #return medias
    return [calcular_media(notas) for notas in notas_alunos]

notas_alunos = [
    [9.0, 7.0, 3.0],
    [10.0, 4.0, 5.0],
    [8.0, 8.0, 2.0]
]

medias = calcular_media_alunos(notas_alunos)
print(medias)

def imprimir_medias(notas_alunos):
    medias = calcular_media_alunos(notas_alunos)
    print(medias)

def enviar_media_por_email(notas_alunos):
    medias = calcular_media_alunos(notas_alunos)
    # logica de enviar por email as medias

imprimir_medias(todas_as_notas)
enviar_media_por_email(todas_as_notas)

# Argumentos nomeados 
def saudacao(nome, frase):
    return f'{frase} {nome}'

print(saudacao('Arthur', 'Boa noite'))
print(saudacao(nome = 'Arthur', frase = 'Boa noite'))
print(saudacao(frase = 'Boa noite', nome = 'Arthur'))
print(saudacao('Arthur', frase = 'Boa noite'))

# Parâmetro com valor padrão(default)
def saudacao (nome, frase = 'Bom dia'):
    return f'{frase} {nome}'

print(saudacao('tutuu'))
print(saudacao('tuthur', 'Bom tarde'))



