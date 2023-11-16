# POO Programação Orientada A Objetos

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa("Igor", "Ferreira")
# p1.nome = "Igor"
# p1.sobrenome = "Ferreira"

print(p1.nome)
print(p1.sobrenome)