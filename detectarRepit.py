'''
    Primer carácter que no se repite
    --------------------------------
    aaeaahaaaaa
'''

# *funciones
def primer_caracter_NO_repetido(secuencia):
    #caracter_sin_repetir = []
    for i in secuencia:
        if secuencia.count(i) > 1:
            continue
        else:
            return i



# *inicio
if __name__ == "__main__":
    secuencia = input('Palabra: ')

    resultado = primer_caracter_NO_repetido(secuencia)

    if resultado == False:
        print('Todos los caracteres se repiten.')
    else:
        print(f'El primer caracter no repetido es: {resultado}')