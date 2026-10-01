# Definiendo la clase
class Celular:
    # Definiendo el metodo constructor
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    # Agregamos un metodo
    def llamar(self):
        print(f'Llamando desde un {self.marca}')

# Creamos nuestros objetos
celular_1 = Celular('Samsung', 'A23', '48')
celular_2 = Celular('LG', 'L31', '48')

# Exploramos los atributos de nuestro objeto
print(celular_1.marca)

# Utilizamos los metodos del objeto
celular_2.llamar()