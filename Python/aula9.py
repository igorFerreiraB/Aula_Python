# args retornam uma tupla que suporta quantos argumentos for necessário (não nomeados)
# Contadores

def soma(*args):
    total = 0
    for numero in args:
        print(total, numero)
        total += numero

soma(3, 5, 8, 1, 6, 3)

print(sum((3000434,34242,3423131,432345)))
