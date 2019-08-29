'''
    CONJUNTOS
*****************
'''

# Preparar una variable para almacenar un conjunto vacio. En los casos que insertemos ya de entrada contenido, no es necesario set()

conjuntos = set()

# Crear un conjunto
conjuntos = {1,2,3,4,5,'HOLA', 7.9}

# Agregar nuevos elementos. Nos lo va a insertar en un lugar desordenado
conjuntos.add('ADIOS')
print(conjuntos, '\n')

# Eliminar un valor
conjuntos.discard('ADIOS')
print(conjuntos, '\n')

# Buscar un elemento
print('ADIOS' in conjuntos)
print('ADIOS' not in conjuntos)

# Borrar todo el contenido
conjuntos.clear()

# Comprobar si ambos conjuntos son iguales
conjunto01 = {1,2,3}
conjunto02 = {4,2,5}

print(conjunto01 == conjunto02)

# Unión de dos conjuntos
union = conjunto01 | conjunto02
print('*****************')
print(union, '\n')

# Intersección de dos conjuntos. Lo elementos que se repiten.
union = conjunto01 & conjunto02

# La diferencia. Elementos que estan solo en el conjunto A
union = conjunto01 - conjunto02

# La diferencia simetrica. Elementos que estan A y B, pero no en ambos.
union = conjunto01 ^ conjunto02


'''
    DICCIONARIOS
**********************
    Son elementos desordenados
    Se utiliza la llave -> valor
'''

# diccionario vacio
diccionario = {}

# Diccionario
diccionario = {
    #(key) : (value)
    'cama' : 'bend',
    'rojo' : 'red',
    'lápiz' : 'pencil'
}
print('********DICCIONARIOS*************')
print(diccionario, '\n')

# Sacar el resultado de una llave(key)
print(diccionario['rojo'], '\n')

# Agregar nuevos elemtos
diccionario['perro'] = 'dog'

# Modificar un elemento
diccionario['rojo'] = 'RED'

# Eliminar elemento
del(diccionario['rojo'])

'''
Ejemplo
'''

agenda01 = {
    'Pepe' : [33, 1.72],
    'Maria' : [24, 1.80],
    'Juan' : [44, 1.64],
    'Eva' : [14, 1.30]
}
print(agenda01['Maria'])

agenda02 = {
    'Pepe' : {'edad': 33, 'altura' : 1.72},
    'Maria' : {'edad': 24, 'altura' : 1.80},
    'Juan' : {'edad': 44, 'altura' : 1.64},
    'Eva' : {'edad': 14, 'altura' : 1.30}
}
print(agenda02['Maria'])

equipoNBA = {
    23 : 'Michael Jordan',
    00 : 'Robert Parish',
    21 : 'Dominique Wilkins',
    33 : 'Larry Bird',
    10 : 'Dennis Rodman',
    24 : 'Moses Malone',
    34 : 'Shaquile ONeal'
}

# Sacar un valor, sabiendo que existe la llave
print(equipoNBA[00])

# Sino sabes que la llave puede existir, aqui nos ayuda la función get()
print(equipoNBA.get(89, 'No existe este jugador'))

# Busqueda directa
print(33 in equipoNBA)

# Enseñar solo las llaves
print(equipoNBA.keys())

# Enseñar solo los valores
print(equipoNBA.values())

# Enseñar llave-valor
print(equipoNBA.items())

# Limpiar Diccionario
equipoNBA.clear()
