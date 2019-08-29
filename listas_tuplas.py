'''
    LISTAS
    Parecidas alos Arreglos
'''
grupo = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Viernes', ['Sábado', 'Domingo'], 10, True, 10.10]

# Imprimir elementos de una lista
print(grupo,'\n')

# Imprimir elementos seccionados
print(grupo[2:5],'\n')

# Pedir la longitud de una lista
print(len(grupo),'\n')

# Agregar elemtos al final de una lista
grupo.append('FINAL')
print(grupo, '\n')

# Agregar elementos entre partes de un lista
grupo.insert(2,'INSERTAR')
print(grupo, '\n')

# Agregar varios elementos al final
grupo.extend([30,40,50])
print(grupo, '\n')

# Podemos concatenar lista
otroGrupo = ['La Tierra', 'La Luna', 'Neptuno']

grupoFinal = grupo + otroGrupo
print(otroGrupo, '\n')

# Saber si un valor esta dentro de una lista
print(30 in grupoFinal)

# Saber en que índice esta un elemento
print(grupoFinal.index('FINAL'))

# Contar cuantas veces se repite un elemento
print(grupoFinal.count('Viernes'))

# Eliminar el último elemento de la lista
grupoFinal.pop()
print(grupoFinal, '\n')

# Eliminar el elemento de la index de ls lista
grupoFinal.pop(3)
print(grupoFinal, '\n')

# Eliminar un elemento exacto de la lista
grupoFinal.remove('CENTRO')
print(grupoFinal, '\n')

# Voltear una lista
grupoFinal.reverse()

# Ordenar una lista
grupoFinal.sort()
grupoFinal.sort(reverse=True)

# Borrar toda lista
grupoFinal.clear()

# Cambiar contenido de un elemento
grupo[4] = 'Netflix'


'''
    TUPLAS
    - NO PUEDEN CAMBIAR
    Utilizan los mismos métodos de busqueda que las listas
    Consumen menos memoria que una lista
    Son más rápidas en ejecución que las listas
'''

tupla01 = ('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Viernes', ['Sábado', 'Domingo'], 10, True, 10.10)


# Imprimir elementos de una tupla
print(tupla01,'\n')

# Imprimir elementos seccionados
print(tupla01[2:5],'\n')

# Pedir la longitud de una tupla
print(len(tupla01),'\n')

# Saber si un valor esta dentro de una tupla
print(30 in tupla01)

# Saber en que índice esta un elemento
print(tupla01.index('FINAL'))

# Contar cuantas veces se repite un elemento
print(tupla01.count('Viernes'))

# Copiar el contenido de una Tupla a una Lista
nuevaLista = list(tupla01)

# Copiar contenido de una Lista a una Tupla
nuevaTupla = tuple(grupo)