class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir_nombre(self):
        print(f'El nombre es: {self.nombre}')

    def imprimir_edad(self):
        print(f'La edad es: {self.edad}')


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)

        self.grado = grado

    def imprimir_grado(self):
        print(f'El grado es: {self.grado}')

persona = Estudiante('Juan', 25, 9)

persona.imprimir_nombre()
persona.imprimir_edad()
persona.imprimir_grado()