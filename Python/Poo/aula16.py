# Exemplo de composição uma classe compõe a outra

class Motor:
    def ligar(self):
        print("Motor ligado")

class Carro:
    def __init__(self):
        self.motor = Motor()

    def ligar(self):
        print("Carro ligado")
        self.motor.ligar()

# Uso da composição
carro = Carro()
carro.ligar()