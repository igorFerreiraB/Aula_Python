from time import sleep


def mostraLinhas():
    print ("-" * 40)

def maior(*num):
    cont = 0
    maior = 0
    print("\nAnalisando valores passados...")
    for numero in num:
        print(f"{numero} ", end="", flush=True)
        sleep(0.4)
        if cont == 0:
            maior = numero
        else:
            if numero > maior:
                maior = numero
        cont += 1

    print(f"Foram indormado {cont} valores ao todo.")
    print(f"O maior valor informado foi {maior}.")


maior(93,39,91,100)
mostraLinhas()
maior(4, 6, 2)
mostraLinhas()
maior(4, 1, 7, 3, 9)

'''
def soma(*num):
    maior = 0
    
    tam = len(num)
    print("Analisando valores passados...")
    sleep(0.5)
    print(f"{num} Foram informados {tam} valores ao todo.")
    print(f"O maior valor informado foi {}")
    sleep(0.5)

soma(1, 2, 3, 4, 7)
mostraLinhas()
soma(9, 1, 5, 2)
mostraLinhas()
soma(1, 4, 7)
'''