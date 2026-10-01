class Animal():
    def comer(self):
        print('Comiendo...')

class Mamifero(Animal):
    def amamantar(self):
        print('Amamantando...')

class Ave(Animal):
    def volar(self):
        print('Volando...')

class Murcielago(Mamifero, Ave):
    def __init__(self):
        pass

Murcielago = Murcielago()
Murcielago.amamantar()
Murcielago.volar()
Murcielago.comer()