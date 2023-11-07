def mostra_linha():
    print("---+---+---")

def jogo_da_velha():
    while True:
        quant_x = input('JOGUE COM O X: ')
        print(f"{quant_x} | ")
        quant_bolinha = input('JOGUE COM BOLINHA: ')
        print(f"{quant_bolinha} | ")
        break


jogo_da_velha()