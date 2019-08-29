''' 
    Tipos de datos que acepta Python
'''

# String - str
# Cadena de texto, se colocan entre comillas simples
print("Hello World")
print('12')
print(''' tengo 23 años ''')
print(""" aprendiendo """)
print(' Esto tiene comillas "" ')

# La función TYPE nos devuleve el tipo de dato ingresado
print(type('hola mundo'))

# Integers(Enteros) - int
# números enteros
print(30)
print(type(30))

# Floats (decimales)
# números con decimales
print(30.6)
print(type(30.6))

# boleans - bool
# datos lógicos - definen tipos de estado
print(False)
print(type(False))
print(True)
print(type(True))

# Listas - lists
# Conjunto de datos definidos. Esta conformada por elementos de diferentes tipos
[5, 7, 46, 4, 23]
print([5, 7, 46, 4, 23])
print(type([5, 7, 46, 4, 23]))
['Hola', 'Hello', 'Bye']
["Hola", 30, 30.4, False]

# Tuplas / Tuples
# Es como una lista, pero los datos no pueden mdificarse
(10, 20, 30, 55)
print((10, 20, 30, 55))
print(type((10, 20, 30, 55)))

# Diccionarios - dict
# Se utilizan para agrupar datos que pertenecen a una misma entidad
# key : value
print(
    {
        'nombre' : 'Pepe',
        'appellido' : 'Gustavo',
        'apodo' : 'Cosa',
        'movil' : 678678687678
    }
)
print(type(
    {
        'nombre' : 'Pepe',
        'appellido' : 'Gustavo',
        'apodo' : 'Cosa',
        'movil' : 678678687678
    })
)


# None - NoneType
# tipo de dato no definido
print(type(None))