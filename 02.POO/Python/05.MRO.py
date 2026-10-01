class PrimeraClaseMadre():
    # def quien_eres(self):
        # print('Soy la clase madre 1')
    pass

class SegundaClaseMadre():
    def quien_eres(self):
        print('Soy la clase madre 2')

class PrimeraClaseIntermedia(PrimeraClaseMadre):
    # def quien_eres(self):
        # print('Soy la clase intermedia 1')
    pass

class SegundaClaseIntermedia(SegundaClaseMadre):
    def quien_eres(self):
        print('Soy la clase intermedia 2')
    # pass

class Hija(PrimeraClaseIntermedia, SegundaClaseIntermedia):
    def quien_eres(self):
        print('Soy la clase hija')
    # pass

objeto = Hija()
objeto.quien_eres()

# Method Resolution Order
print(Hija.mro())