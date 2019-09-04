'''
    Métodos de Formato
'''

# Convetir a mayúscula la primera letra

# * capitalize()

cadena = 'bienvenido a mi aula'
print(cadena.capitalize())

# Convertir un cadena en minúsculas

# * lower()

cadena = 'AULA'
print(cadena.lower())

# Convertir un cadena en mayúsculas

# * upper()

cadena = 'aula'
print(cadena.upper())

# Convertir un cadena si esta mayúsculas a minúsculas y viceversa

# * swapcase()

cadena = 'aula'
print(cadena.swapcase())

# Convertir un cadena en formato Título

# * title()

cadena = 'hola mundo'
print(cadena.title())

# Alineacion de un texto en consola con un relleno

# * center(longitud, "carácteres de relleno")

cadena = 'hola mundo'
print(cadena.center(50,'*'))
print(cadena.ljust(50,'*'))
print(cadena.rjust(50,'*'))


# Contar cantidad de subcadenas

# * count()

cadena = 'hola mundo'
print(cadena.count('a'))



# Buscar subcadenas

# * find()

cadena = 'hola mundo'
print(cadena.find('mun'))


# SLICES
# Obtener un substring

         #012345
cadena = 'ibecon'

cadena[1:] # becon

cadena[1:3] # be

cadena[1:6:2] # bcn

cadena[::-1] # nocebi
