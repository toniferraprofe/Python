"""
    ENCRIPTACIÓN
    ------------
    Encriptar un mensaje es modificar de forma que si alñguien que no conoce la clave intenta leerlo no va poder.
    La criptografia se usa desde hace años, un gran ejemplo de tenéis es Julio Cesar.
    Hay API's de cifrado de mensajes muy concretos.
"""
import os

KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
    'á': '&',
    'é': '&s'
}

# logica
def cifrado(mensaje):
    palabras = mensaje.split(' ')
    cifrado_mensaje = []

    for palabra in palabras:
        cifrado_palabra = ''
        for letra in palabra:
            cifrado_palabra += KEYS[letra]
        
        cifrado_mensaje.append(cifrado_palabra)

    return ' '.join(cifrado_mensaje)


def descifrado(mensaje):
    palabras = mensaje.split(' ')
    descifrar_mensaje = []

    for palabra in palabras:
        descifrar_palabra = ''

        for letra in palabra:

            for key, value in KEYS.items():
                if value == letra:
                    descifrar_palabra += key

        descifrar_mensaje.append(descifrar_palabra)

    return ' '.join(descifrar_mensaje)






# desarrollo
def run():
    os.system('clear')

    while True:

        comando = input("""---*---*---*---*---*---*------*---*---*---*---*---*---
        
            Bienvenido a criptografía IBECON
            ¿Qué quieres hacer?

            [c]ifrar mensaje
            [d]escifrar un mensaje
            [s]alir        
        """)
        
        if comando.lower() == 'c':
            mensaje = input('Escribe tu mensaje: ')
            cifrado_mensaje = cifrado(mensaje)
            print(cifrado_mensaje)

        elif comando.lower() == 'd':
            mensaje = input('Escribe tu mensaje cifrado: ')
            descifrado_mensaje = descifrado(mensaje)
            print(descifrado_mensaje)

        elif comando.lower() == 's':
            break
        else:
            print('Comando no encontrado')




# inicio
if __name__ == "__main__":
    print('M E N S A J E S   C I F R A D O S')
    run()