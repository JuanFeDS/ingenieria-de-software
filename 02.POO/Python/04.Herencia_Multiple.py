class Persona():
    # Definimos el metodo constructor
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print(f'{self.nombre} esta hablando.')

# Creamos una clase independiente
class Artista():
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return (f'Mi habilidad es: {self.habilidad}')

# Creamos una clase hija de la clase Persona
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        # Especificammos los atributos que se heredaran
        super().__init__(nombre, edad, nacionalidad)
        
        self.trabajo = trabajo
        self.salario = salario
    
    def trabajar(self):
        print(f'{self.nombre} esta trabajando como {self.trabajo}')

# Vamos a crear una clase que hereda de Persona y de Artista
class EmpleadoArtista(Persona, Artista):
    # Especificamos los atributos que se heredaran de cada clase
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, trabajo):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)

        # Añadimos los atributos propios de la clase
        self.salario = salario
        self.trabajo = trabajo

    def presentarse(self):
        return (f'Hola, soy {self.nombre} y {self.mostrar_habilidad()}. Trabajo como {self.trabajo}')

roberto = EmpleadoArtista(
            nombre='Roberto', 
            edad=35, 
            nacionalidad='colombiano', 
            habilidad='cantar',
            trabajo='programador', 
            salario=10000
        )

print(roberto.presentarse())