def quebra_linhas():
    print ("-" * 30)

ultimo = 10
fila = list(range(1, ultimo + 1))
while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    quebra_linhas()
    print(f"\nFila atual: {fila}")
    quebra_linhas()
    print("Digite F para adiciona um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair")

    operacao = input("Operaçãao (F, A OU S): ")

    if operacao == "A":
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f"Cliente {atendido} atendido")
        else:
            print("Fila vazia! Ninguem para atender.")
    elif operacao == "F":
        ultimo += 1 # incrementa o ticket do novo cliente
        fila.append(ultimo)
    elif operacao == "S":
        break
    else:
        print ("Operção invalida! Digite apenas F, A ou S")


