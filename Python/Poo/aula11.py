class Caneta:
    def __init__(self, cor):
        self.pigmento = cor

    @property
    def cor(self):
        print('RETORNANDO TINTA')
        return self.pigmento