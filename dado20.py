"""
    El Juego del DADO20
    -------------------
    El usuario tiene que descubri que número a salido al tirar el dado de 20 caras. Y se le van a dar intentos infinitos con pistas.
"""

import os
import random


def run():
    os.system('clear')

    encontrar_numero = False
    numero_aleatorio = random.randint(1, 20)

    while not encontrar_numero:
        numero = int(input('Adivina el número: '))

        if numero == numero_aleatorio:
            print('Felicidades! Encontrate el número')
            encontrar_numero = True
        elif numero > numero_aleatorio:
            print('El número es más pequeño')
        else:
            print('El número es más grande')


if __name__ == "__main__":
    run()
