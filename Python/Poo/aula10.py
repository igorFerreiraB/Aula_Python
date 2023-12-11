# Property são metodos que podem se comportar com atributos
# dentro de uma classe 
class Pessoa:
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        if len(novo_nome) > 5:
            self._nome = novo_nome
        else:
            print('O nome deve ter mais de 5 caracteres.')

    @nome.deleter
    def nome(self):
        print('Deletando o nome...')
        del self._nome

pessoa = Pessoa('Maria')
print(pessoa.nome)

pessoa.nome ='João'
print(pessoa.nome)

del pessoa.nome