'''
    Condicinales
    ************

    Indentación
'''

# IF
if 10 > 0:
    print('esto es un if')
elif 0 == 0:
    print('otro if')
else:
    print('y este es el else')

# IF (anidado)
# Calcular la edad
# ****************

edad = int(input('Cuál es tu edad?'))

# if edad >= 0 and edad < 120:
if 0 < edad < 120:
    print('Edad correcta')
    if edad >= 18:
        print('Es mayor de edad')
    if edad < 18:
        print('Es menor de edad')
else:
    print('Se ha equivocado introduciendo su edad, vuelva a intentarlo. Y no mienta más por favor.')


'''
    EJERCICIO DE ENCARGADO
    Tres personas su edad.
    Que persona es la mayor de edad, porque queremos ponerlo al mando de un grupo de trabajo.
'''
# Información
# persona 01
nombre01 = input('Nombre:')
edad01 = input('Edad:')
# persona 02
nombre02 = input('Nombre:')
edad02 = input('Edad:')
# persona 03
nombre03 = input('Nombre:')
edad03 = input('Edad:')

# comprobación
if (0 < edad01 < 120) and (0 < edad02 < 120) and (0 < edad03 < 120):
    print('Todas las edades correctas')


# quien es el de mayor
if edad01 > edad02 and edad01 > edad03:
    print(f'El encargado es {nombre01}')
elif edad02 > edad01 and edad02 > edad03:
    print(f'El encargado es {nombre02}')
elif edad03 > edad01 and edad03 > edad02:
    print(f'El encargado es {nombre03}')
else:
    print('Los tres pueden ser encargados')

# Switch
# No existe
# *****************

caracter = input('Insertar una letra: ').lower()

if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u':
    print('Es una vocal')
else:
    print('No es una vocal')
