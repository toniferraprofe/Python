'''
    ******************
    CALCULATORpro v0.1
    ******************
'''
# interacción por parte del usuario
num01 = float(input('Primera cantidad:'))
num02 = float(input('Segunda cantidad:'))

operador = input('Qúe tipo de operación quieres realizar (S/R/D/M)?').upper()

# condiciones de Calculo
if operador == 'S':
    suma = num01 + num02
    print(f'El resultado de la Suma: {suma}')
if operador == 'R':
    resta = num01 - num02
    print(f'El resultado de la Resta: {resta}')
if operador == 'D':
    dividir = num01 / num02
    print(f'El resultado de la División: {dividir}')
if operador == 'M':
    multi = num01 * num02
    print(f'El resultado de la Multiplicación: {multi}')
else:
    print('El tipo de operador es incorrecto')



