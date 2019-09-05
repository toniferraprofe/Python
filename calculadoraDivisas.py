'''
    CALCULADORA Pro
'''

def calculadora(montante):
    libras = 0.9
    return libras * montante

def run():
    print(' C A L C U L A D O R A  D E  D I V I S A S')
    print('Convierte libras a euros')
    print('')

    montante = float(input('¿Cuántas libras?: '))

    resultado = calculadora(montante)

    print(f'{montante:.2f}€ libras son tantos euros: {resultado:.2f}€')

if __name__ == "__main__":
    run()