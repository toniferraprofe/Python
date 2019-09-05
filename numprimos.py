'''
    Números Primos
    --------------
    Son aquellos que se pueden dividir entre 1 y entre uno mismo
'''

# *funciones
# Lógica
# como saber si un número cumple las condiciones de ser primo
def si_es_primo(numero):
    if numero < 2:
        return False
    elif numero == 2:
        return True
    elif numero > 2 and numero % 2 == 0:
        return False
    else:
        for i in range(3, numero):
            if numero % i == 0:
                return False
    
    return True


# desarrollo
def run():
    # pedimos al usuario que nos de el número que quiere que examinemos si es primo o no
    numero = int(input('Escribe un número: '))

    resultado = si_es_primo(numero)

    if resultado is True:
        print('Tu número es primo!!!')
    else:
        print('Tu número no es primo')


# *inicio
if __name__ == "__main__":
    for i in range(1, 100):
        cont = abs(i - 100)
        print(f'Intento nº {i} te quedan {cont}')
        run()
