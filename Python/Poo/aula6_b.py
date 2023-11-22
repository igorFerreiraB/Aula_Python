import json

from aula6_a import CAMINHO_ARQUIVO, Pessoa, dump

dump()

with open(CAMINHO_ARQUIVO, "r") as arquivo:
    pessoas = json.load(arquivo)
    pessoa1 = Pessoa(**pessoas[0])
    pessoa2 = Pessoa(**pessoas[1])
    pessoa3 = Pessoa(**pessoas[2])

    print(pessoa1.nome, pessoa1.idade)
    print(pessoa2.nome, pessoa1.idade)
    print(pessoa3.nome, pessoa1.idade)