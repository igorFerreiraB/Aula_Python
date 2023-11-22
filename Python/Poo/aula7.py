# Metodos de classes + factories (fabricas)
# são metodos onde 'self' será 'cls', ou seja,
# ao invés de receber a instancia no primeiro
# parâmetro, receberemos a própipa classe.

class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_pessoa_qualquer(cls, idade):
        return cls('PessoaQualquer', idade)
    

pessoa1 = Pessoa.criar_pessoa_qualquer(20)
pessoa2 = Pessoa.metodo_de_classe('igor')
print(pessoa1.nome, pessoa1.idade)
print(pessoa2.nome, pessoa2.idade)
