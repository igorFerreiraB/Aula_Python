class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
pessoa1 = Pessoa("igor", 16)
pessoa2 = Pessoa("jose", 28)
    
print(pessoa1.ano_nascimento())
print(pessoa2.ano_nascimento())