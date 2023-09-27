def multiplica_com_soma(vezes, valor):
    if vezes and valor == 0:
        return 0
    elif vezes == 1:
        return valor
    else:
        return valor + multiplica_com_soma(vezes-1, valor)
    
print(multiplica_com_soma(3, 2))
    