'''
    Palindromo es una palabra que se lee igual del derecho como del revés
'''

import os

# funciones
def palindromo(palabra):
    os.system('clear')
    palabraInvertida = palabra[::-1]

    if palabraInvertida == palabra:
        return True
    else:
        return False



# inicio
if __name__ == "__main__":
    while True:
        palabra = input('Escribe tu palabra favorita: ')

        resultado = palindromo(palabra)

        if resultado == True:
            print('Tu palabra es un ¡Palindromo!')
            
        else:
            print('NO es un palindromo...Eres un triste.')


        pregunta = input('¿Quieres seguir jugando (S/N)? ')
        if pregunta.upper() != 'S':
            break
            