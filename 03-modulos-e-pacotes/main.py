# Modulos e Pacotes
# importar tudo de matematica
import matematica

# importar apenas os elementos (constantes, funções, classes) necessários
# nesse caso não precisa colocar "nomeModulo" antes da constante, função ou classe
from matematica import PI, somar, subtrair
from matematica import *

# caso tenha conflito de nome
from matematica import PI as PI_MAT, somar as soma

#importar a fn media do pacote estatistica e modulo descritiva
from estatistica.descritiva import media
from estatistica.inferencial import VALOR


PI = 3.141592653589793238462643383279502884197169399375105820974944592307816406

print(PI)
print("soma:", matematica.somar(10.0, 3.45))
print("subtração:", matematica.subtrair(12.7, 5.4))

