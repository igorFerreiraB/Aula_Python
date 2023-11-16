# Metododos em instâncias de classes Python
class Carro:
    def __init__(self, nome):
        self.nome = nome
    
    def acelerar(self):
        print(f"{self.nome} está ligado")

fusca = Carro("Fusca")
print(fusca.nome)
fusca.acelerar()

voyage = Carro("Voyage")
print(voyage.nome)
voyage.acelerar()