# Exercicio de mostrar o resto da divisão de 10 por 3
# def resto_divisao(a, b):
#     return a ** b

# print(resto_divisao(10, 3))

# Exercicio de fazer a tabuada do 13

# tabuada = [item * 13 for item in range(11)]

# print(tabuada)

# Davinir não gosta de ir às aulas. Mas ele é obrigado a comparecer a pelo menos 75% delas. Ele quer saber quantas aulas pode faltar, sabendo que tem duas aulas por semana, durante quatro meses. Ajude o Davinir!. Claro a seguir quantas vezes podera faltar

# Sabendo que um mês tem 4 semanas 4 meses tem 16 semanas certo ?

# Função recursiva com fatorial
# Call stack pilha de chamadas
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
       
print(fatorial(6))

# Função recursiva com fibonacci que também
# usa o esquema de pilha de chamadas
def fibonacci(n):
    if n <= 0:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(20))