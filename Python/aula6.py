def maior(x, y):
    x = int(input("Digite o primeiro numero: "))
    y = int(input("Digite o segundo numero: "))

    if x > y:
        print(f"O primeiro numero digitado {x} e maior que o segundo{y}.")
    elif x == y:
        print(f"O primeiro numero digitado {x} e igual ao segundo {y}.")
    else:
        print(F"O segundo valor digitado {y} e maior que o primeiro {x}.")

maior(x=0, y=0)

x = 0
y = 0