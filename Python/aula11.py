# Fazer uma função que identifica se um numero e par ou impar

'''
def par_impar(*args):
    multiplo = args
    if multiplo % 2 == 0:
        print("Este numero e par")
    else: 
        print("Este numero e impar")

par_impar(2)
par_impar(5)
par_impar(6)
par_impar(7)
'''

# Suponha que você tenha uma tupla com um número
tupla = (4,)

# Acessa o elemento da tupla e armazena em uma variável
numero = tupla[0]

# Verifica se o número é par ou ímpar
if numero % 2 == 0:
    print(f"{numero} é um número par.")
else:
    print(f"{numero} é um número ímpar.")