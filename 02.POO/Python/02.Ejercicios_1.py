# Creamos nuestra clase
class Estudiante():
    # Definimos el metodo constructor
    def __init__(self, nombre, edad, genero, grado):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.grado = grado

    # Creamos el metodo "Estudiar" 
    def estudiar(self):
        if self.genero == 'Femenino':
            print(f'La estudiante {self.nombre} esta estudiando.')
        else:
            print(f'El estudiante {self.nombre} esta estudiando.')

# Capturamos los atributos
nombre = input('Introduce el nombre del estudiante: ')
edad = int(input('Introduce la edad del estudiante: '))
genero = input('Introduce el genero del estudiante: ')
grado = int(input('Introduce el grado del estudiante: '))

# Creamos nuestro objeto con los atributos poporcionados
# estudiante_1 = Estudiante('Sandra', 31, 'Femenino', 9)
estudiante_2 = Estudiante(nombre, edad, genero, grado)

accion = input('Qué acción deseas que el estudiante realice?').upper()

# Usamos nuestro metodo
while True:
    
    if accion == 'ESTUDIAR':
        estudiante_2.estudiar()
        break
    else:
        print('No es una acción valida')
        accion = input('Qué acción deseas que el estudiante realice?').upper()