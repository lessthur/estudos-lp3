def solicitaNota():
    nota = float(input("Digite a sua nota de 0 a 100: "))
    if (nota > 100 or nota < 0):
        while(nota > 100 or nota < 0):
            nota = float(input("Digite uma nota válida! (0 a 100): "))
    return nota

def conversaoNota(nota):
    if nota == 0:
        return "F"
    elif (nota >= 1 and nota <= 35):
        return "D"
    elif (nota >= 36 and nota <= 60):
        return "C"
    elif (nota >= 61 and nota <= 85):
        return "B"
    elif (nota >= 86 and nota <= 100):
        return "A"
    else:
        print("Erro")
        
nota = float(solicitaNota())
notaConvertida = conversaoNota(nota)

print("Nota no sistema numérico = %.2f | Nota no sistema ABCDEF: %s" % (nota, notaConvertida))
        