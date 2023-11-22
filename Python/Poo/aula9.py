# Getter
class Exemplo:
    def __init__(self):
        self._valor_privado = 'Ola'  # Atributo privado comum em Python, indicado por um sublinhado no início

    # Getter usando uma propriedade
    @property
    def valor_privado(self):
        return self._valor_privado


objeto = Exemplo()
print(objeto.valor_privado)  # Chamando o getter
