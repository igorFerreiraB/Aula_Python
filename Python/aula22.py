palavra1 = [15, 7, 27, 39]
palavra2 = [16, 8, 28, 40]

valor_a_procurar = int(input("Digite o valor a procurar: "))
x = 0
while x < len(palavra1 and palavra2):
    if palavra1[x] == valor_a_procurar:
        print(f"{valor_a_procurar} achado na posição {x} da primeira lista")
        break
    elif palavra2[x] == valor_a_procurar:
        print(f"{valor_a_procurar} achado na posição {x} da segunda lista")
        break
    x += 1
else:
    print(f"{valor_a_procurar} não encontrado")


