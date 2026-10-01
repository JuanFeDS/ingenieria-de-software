class Persona():
    # Definimos el metodo constructor
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print(f'{self.nombre} esta hablando.')

# Creamos una clase hija
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        # Especificammos los atributos que se heredaran
        super().__init__(nombre, edad, nacionalidad)
        
        self.trabajo = trabajo
        self.salario = salario
    
    # Agregamos un metodo especifico para esta clase
    def trabajar(self):
        print(f'{self.nombre} esta trabajando como {self.trabajo}')


roberto = Empleado('Roberto', 35, 'colombiano', 'programador', 10000)

# El objeto tendrá atributos de la clase madre
roberto.hablar()

# Y tambien de la clase madre
roberto.trabajar()