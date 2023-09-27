
titulo = "SISTEMA DE ALUNOS"

def mostraLinha():
    print ("-" * 25)

mostraLinha()
print(titulo.rjust(21))
mostraLinha()



def titulo(txt):
    print ("-" * 30)
    print (txt)
    print ("-" * 30)

titulo("SISTEMA DE ALUNOS".rjust(23))
titulo("↓↓↓ CADASTRO ↓↓↓".rjust(23))



def soma(a, b):#🠔 Parametro
    a = input("Digite um numero")
    s = a * b
    print(f"A soma A + B = {s}")

# Chamando a função
soma (4, 2)
soma (3, 5)
soma (7, 3)



def contador(*num):
    tam = len(num)
    print(f"Valores {num} Quantidade {tam}")


contador(2, 5, 6)
contador(9, 1)
contador(9, 1, 3, 8, 2)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [3, 4, 5, 2, 1]
dobra(valores)
print(valores)