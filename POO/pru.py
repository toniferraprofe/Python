# Crear una clase = Molde
class Coche():
    # constructor
    def __init__(self, largo, ancho, color, ruedas):
        self.largoChasis = largo
        self.anchoChasis = ancho
        self.ruedas = 4
        self.enMarcha = False
        self.color = color


    # crear unos métodos
    def arrancar(self, arrancamos):
        self.enMarcha = arrancamos

        if self.enMarcha:
            chequeo = self.chequeoArranque()

        if self.enMarcha and chequeo:
            return 'El coche esta en marcha'
        elif self.enMarcha and chequeo == False:
            return 'Problemas al arrancar'
        else:
            return 'El coche esta parado'

    def estado(self):
        print(f'El coche tiene {self.ruedas} ruedas, un ancho de {self.anchoChasis} y un largo de {self.largoChasis}')

    def chequeoArranque(self):
        print('Realizado el chequeo de puesta en marcha')

        self.gasolina = True
        self.aceite = True
        self.puertasCerradas = True
        self.bateria = True

        if self.gasolina and self.aceite and self.puertasCerradas and self.bateria:
            return True
        else:
            return False




# instancia/Objeto una clase. Crear objeto.
print('--------------------Primer Objeto-------------------')
miCoche = Coche(200,90,'rojo',4)

print(miCoche.arrancar(True))

miCoche.estado()

print('--------------------Segundo Objeto-------------------')

camion = Coche(800,200,'blanco',8)

print(camion.arrancar(False))

camion.ruedas = 8

camion.estado()

print('--------------------Tercer Objeto-------------------')

miCoche02 = Coche(220.5, 99.45,'negro asesino callejero')

print(miCoche02.arrancar(True))

miCoche02.estado()