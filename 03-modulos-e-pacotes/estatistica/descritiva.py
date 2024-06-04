from .inferencial import VALOR
from ..matematica import somar

def media(valores):
    return sum(valores) / len(valores)

def minimo(valores):
    return min(valores)

def maximo(valores):
    return max(valores)

def minha_funcao():
    print(VALOR)
    print(somar(3.5, 9.0))