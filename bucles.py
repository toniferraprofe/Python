'''
    Bucle FOR
'''

# El For lo vamos a utilizar en colecciones
for i in [1,2,3,4,5,6]:
    print(i)

for i in [34, 'Pepe', 8.23]:
    print(i)

# Crear la colección fuera del FOR
coleccion = (1,2,3,4,5,6,7)

for i in coleccion:
    print(f'Elemento: {i}')


# Con un Diccionario

coleccion = {
    'Pepe' : 34,
    'Maria' : 67,
    'Joselito' : 44
}

# Mostrar las keys del diccionario
for i in coleccion:
    print(f'Nombre: {i}')

# Mostrar las valores del diccionario
for i in coleccion:
    print(f'Edades: {coleccion[i]}')

# Mostrar las key/valor del diccionario
for i in coleccion:
    print(f'{i} -> {coleccion[i]}')

# Metodo diccionario muy utilizado
for llave, valor in coleccion.items():
    print(f'{llave} -> {valor}')

# Bucle que pase por todos los caracteres de una frase
frase = 'Hola mundo'

for i in frase:
    print(i)

for i in frase:
    print(f'{i}', end = '')


'''
    Bucle While
'''
# Bucle indeterminado de iteraciones
# while numero < 0:

import math

numero = int(input('Escribe un número:'))

# El bucle comprueba con una condición, si el numero insertado por el usuario es negativo. Si es negativo, itera el contenido.
# Sino se cumple la condición, pasa a la siguiente línea y final

while numero < 0:
    print('¡Error, debe escribir un número positivo')
    numero = int(input('Intentalo otra vez:'))

print(f'\n Su raiz cuadrada es: {(math.sqrt(numero)):.2f}')

# variable iteradora

i = 0

while i < 7:
    print('Hola Mundo')
    i += 1