'''
    Cajero Automático
    *****************
    Saldo = 1000€
    Ingresar/Retirar/Mostrar/Salir
'''
saldo = 1000

print('\t..:MENU..')
print('1. Ingresar dinero en la cuenta')
print('2. Retirar dinero de la cuenta')
print('3. Mostrar dinero de la cuenta')
print('4. Salir')
opcion = int(input('Elija una opción del menú:'))

print()
if opcion == 1:
    extra = float(input('Cuánto dinero desea ingresar ->'))
    saldo += extra
    print(f'Dinero en la cuenta: {saldo}')
if opcion == 2:
    extra = float(input('Cuánto dinero desea retirar ->'))
    saldo -= extra
    print(f'Dinero en la cuenta: {saldo}')


