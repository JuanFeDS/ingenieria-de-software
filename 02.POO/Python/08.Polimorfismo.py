class Gato():
    def __init__(self):
        pass

    def sonido(self):
        print('Miau')

class Perro():
    def __init__(self):
        pass

    def sonido(self):
        print('Guau')


Gato_1 = Gato()
Perro_1 = Perro()

# Polimorfimsmo de Objetos
Gato_1.sonido()
Perro_1.sonido()

# Polimorfismo funcional
def hacer_sonido(animal):
    animal.sonido()

hacer_sonido(Gato_1)
hacer_sonido(Perro_1)