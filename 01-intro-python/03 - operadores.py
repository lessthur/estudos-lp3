# Operadores aritméticos
# +, -, *, //, **

# numero elevado a outro
# e elevado a n
# 10 elevado a 2
n = 10
numero_elevado = n**2

# Operadores lógicos 
# and, or, not
print (3 + 2) # 5
print (True and True) # True
print (True and False) # False
print (False and True) # False
print (False and False) # False

print (True or True) # True
print (True or False) # True
print (False or True) # True
print (False or False) # False

print (not True) # False
print (not False) # True

# Permitir entrada 
# - o usuário for funcionário E
# - o usuário não estiver bloqueado E
# - hora atual estiver entre 8h e 18h

# Permitir entrada
# - admin

usuario_funcionario = True
usuario_bloqueado = False
hora_atual = 17
usuario_admin = False

horario_comercial = hora_atual >= 8 and hora_atual <= 18
funcionario_ativo = usuario_funcionario and not usuario_bloqueado

if usuario_admin or (funcionario_ativo and horario_comercial):
    print("Entrada Permitida. ")

idade = 22
maior_idade = idade >= 18

if maior_idade:
    pass

# Operadores de comparação 
# ==, !=, >, <, >=, <=
# == comparando valores iguais
# != comparando valores diferentes
# = atribuindo 

idade = 25 
maior_idade = idade >= 18 # True

nota1 = 10.0
nota2 = 5.2
nota3 = 8.9

media = (nota1 + nota2 + nota3) / 3

if media >= 6.0:
    print ('aprovado')

# is, is not
# operador de identidade
# comparar se os objetos ocupam o mesmo espaço de memória

a = [1, 2, 3]
b = [1, 2, 3]
print (a == b) # True 
print (a is b) # False]

c = b
print (b is c) # True 

# Operador in 
# Verificar se um elemento existe ou não em uma sequência 
# str, list, tuple 
opcoes = ('sim', 'não', 'talvez')
opcao = input('Digite uma opção') # '    Sim      '
opcao = opcao.lower()             # '    sim      '
opcao = opcao.strip()             # 'sim'

opcoes = {
    "sim": ['s', 'y', 'yes', 'sim'],
    "não": ['n', 'no', 'não', 'nao']
}
if opcao in opcoes:
    print('ok')
else:
    print('essa nao tem amigo')

numeros = [1, 3, 5, 6]
for numero in numeros:
    print(numero)
