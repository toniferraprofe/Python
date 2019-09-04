'''
    Pelotas en el Deporte
'''

# *CLASE
class Pelota():
    # constructor
    def __init__(self, diametro, peso, material, color, deporte):
        self.diametro = diametro
        self.peso = peso
        self.material = material
        self.color = color
        self.deporte = deporte

    # métodos
    def mostrar(self):
        print(f'TIPO DE PELOTA DE {self.deporte}')
        print('********************************** \n\n')
        print(f'Diametro: {self.diametro} \nPeso: {self.peso} \nMaterial: {self.material} \nColor: {self.color} \nDeporte: {self.deporte}')

# Objetos
pelota_basket = Pelota(50,300,'cuero','marron','baloncesto')

pelota_basket.mostrar()


pelota_tennis = Pelota(10,80,'piel','verde','Tennis')

pelota_tennis.mostrar()