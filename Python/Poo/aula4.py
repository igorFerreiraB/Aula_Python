# Mantendo estados dentro da classe
class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando is True:
            print(f"{self.nome} ja está filmando...")
            return

        print(f"{self.nome} está filmando...")
        self.filmando = True

camera1 = Camera("Canon")
camera2 = Camera("Sony")

camera1.filmar()
camera1.filmar()
print(camera1.filmando)
print(camera2.filmando)