# Metododos em instâncias de classes Python

# Class é um molde (geralmente sem dados)
class Carro:
    def __init__(self, nome):
        self.nome = nome
    
    def ligar(self):
        print(f"{self.nome} está ligado...")

    def acelerar(self):
        acelerar = input("Deseja acelerar s/n ?: ")
        entrada_minuscula = acelerar.lower()
        if entrada_minuscula == "s":
            return f"{self.nome} está acelerando..."
        else:
            return f"O {self.nome} está somente ligado"

fusca = Carro("Fusca")
print(fusca.nome)
fusca.ligar()
fusca.acelerar()

# voyage = Carro("Voyage")
# print(voyage.nome)
# voyage.acelerar()