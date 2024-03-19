# if 
# if condicao:
#    codigo
#    codigo

idade = 20
if idade >= 18:
    print ("maior de idade")

# if/else
if idade >= 18:
    print ('maior de idade')
else:
    print ('menor de idade')

# if/elif/else 
# criança de 0 a 12, adolescente 13 a 17, 
# adulto 18 a 59, idoso 60+


idade2 = int(input('digite sua idade: '))

if idade2 > 0 and idade2 <= 12:
    print ('criança')
elif idade2 > 12 and idade2 <= 17:
    print ('adolescente')
elif idade2 > 17 and idade2 <= 59:
    print ('adulto')
elif idade2 > 59:
    print ('idoso')
else:
    print ('ta morto entao?kkkjkkkk')

# condições aninhadas
email = 'sla@email.com'
senha = '123'

if email == 'sla@email.com':
    if senha == '123':
        print ('liberado')
    else:
        print ('erro')
else:
    print('erro')

if email == 'sla@email.com' and senha == '123':
    print ('liberado')
else:
    print ('erro')

# entrada email, senha 
# saída True ou False
def liberar_acesso(email, senha):
    if email == 'sla@email.com' and senha == '123':
        return True 
    else:
        return False

def liberar_acesso(email, senha):
    return email == 'sla@email.com' and senha == '123'

# entrada hora_atual 
# sim ou nao
def horario_comercial(hora_atual):
    if hora_atual >= 8 and hora_atual <= 18:
        return True
    else:
        return False
    
def dentro_horario_comercial(hora_atual):
    return hora_atual >= 8 and hora_atual <= 18

# dia 1, 2, 3, 4, 5, 6, 7
# palavra domingo, segunda, terça, quarta, quinta, sexta, sábado

dia = 3

dias = {
    1: 'domingo',
    2: 'segunda',
    3: 'terça',
    4: 'quarta',
    5: 'quinta',
    6: 'sexta', 
    7: 'sábado'
}

if dia in dias:
    print (dias[dia])

for chave in dias.keys():
    print(chave)

for valor in dias.values():
    print(valor)

# operador ternário
idade = 20
# maior ou menor
status = ''

if idade >= 18:
    status = 'maior'
else:
    status = 'menor'

satus = 'maior' if idade >= 18 else 'menor'
 

# match
dia = 3
match dia:
    case 1:
        print('Domingo')
    case 2: 
        print('Segunda')
    case 3: 
        print('Terça')
    case 4:
        print('Quarta')
    case 5: 
        print('Quinta')
    case 6:
        print('Sexta')
    case 7:
        print('Sábado')
    case _:
        print('Dia inválido')

match dia:
    case 1 | 7:
        print('Fim de semana')
    case 2| 3 | 4 | 5 | 6:
        print('Dia útil')
    case _:
        print('Dia inválido')

