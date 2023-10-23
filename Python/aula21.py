# Convertendo funçôes def() comuns em lambda

def executa(funcao, *args):
    return funcao(*args)

def soma(x,y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero): 
        return numero * multiplicador
    return multiplica

print(executa(soma, 5, 5))
