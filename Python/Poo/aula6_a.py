import json

CAMINHO_ARQUIVO = "minha_classe.json"

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa1 = Pessoa("Igor", 17)
pessoa2 = Pessoa("dulce", 53)
pessoa3 = Pessoa("rodrigo", 49)

todo_mundo = [pessoa1.__dict__, pessoa2.__dict__, pessoa3.__dict__]

# pessoa = Pessoa(nome="igor", idade="16")

# todos = {"nome": pessoa.nome, "idade": pessoa.idade}
def dump():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo_json:
        json.dump(todo_mundo, arquivo_json, ensure_ascii=False, indent=2)