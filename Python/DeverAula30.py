# def data(presente, passado):
#     return passado - presente

def salario(salario_inicial, anos, aumento_percentual):
    for _ in range(anos):
        salario_inicial += salario_inicial * (aumento_percentual / 100)
    return salario_inicial

salario_inicial = int(input("Salario inicial: "))
anos = int(input("Quantos anos de casa ?: "))
aumento_percentual = float(input("Digite o aumento percentual: "))

novo_salario = salario(salario_inicial, anos, aumento_percentual)
print(f"Slário Atual: {novo_salario:.2f}")
# print(f"Tempo de casa {data(1995, 2023)} anos")

