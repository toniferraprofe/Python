
'''
    El Juego del Ahorcado
'''
# * LIBRERIAS
import os
import random

# * ACSII ART
# constante
IMAGENES = ['''

    +---+
    |   |
        |
        |
        |
        |
        ==========''','''

    +---+
    |   |
    O   |
        |
        |
        |
        ==========''','''

    +---+
    |   |
    O   |
    |   |
        |
        |
        ==========''','''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        ==========''','''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        ==========''','''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        ==========''','''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        ==========''','''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        ==========''','''

''']

# * JUEGO
# palabras para el juego
PALABRAS = [
    'sillas',
    'ordenador',
    'cursos',
    'desarrollador',
    'papelera'
]

# funciones
# elegir una palabra aleatoria
def palabraAleatoria():
    lista = random.randint(0, len(PALABRAS) - 1)
    return PALABRAS[lista]
    

# imprimir el escenario para poder jugar
def tablero(esconderPalabra, intentos):
    print(f'{IMAGENES[intentos]}\n')
    print(esconderPalabra)
    print('----*----*----*----*----*----*----*----*')



# arrancar
def run():
    palabra = palabraAleatoria()
    esconderPalabra = ['-'] * len(palabra)
    intentos = 0

    # bucle infinito
    while True:
        os.system('clear')
        tablero(esconderPalabra, intentos)
        print(f'\n\tINTENTOS: {intentos}')
        print(palabra)
        pedirLetras = input('Adivina una letra: ')

# * LOGICA del Juego
        indexarLetra = []
        for i in range(len(palabra)):
            if palabra[i] == pedirLetras:
                indexarLetra.append(i)
        
        if len(indexarLetra) == 0:
            intentos += 1

            # * Perder
            if intentos == 7:
                tablero(esconderPalabra, intentos)
                print('')
                print(f'¡Perdiste! La palabra correcta es {palabra}')
                break

        # * Acertar
        else:
            for i in indexarLetra:
                esconderPalabra[i] = pedirLetras
        
        # Vaciar al final
            indexarLetra = []

        # Ganar
        try:
            esconderPalabra.index('-')
        except ValueError:
            print('')
            print(f'¡Felicidades! La palabra ganadora es: {palabra}')
            # break







# * INICIO
if __name__ == "__main__":
    run()