# Exemplo de herança de uma classe e subclasses uma herda da outra

class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        print("Au au")

# Uso da herança
dog = Cachorro()
dog.fazer_som()