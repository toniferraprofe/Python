'''
    FUNCIONES en PYTHON
    Las funciones son un concepto fundamental en la programación.
    Una función es una secuencia de comanandos que realizan una acción ó un computo.

    Palabra reservada en python es DEF y cuando queremos que una función retorne un valor la palabra reservada es RETURN
'''

# definimos una función con sus parámetros
def suma(num1,num2):
    sumar = num1 + num2
# devuelver el valor
    return sumar

#---- Como llamar a una función
print(suma(6,90))






# EJEMPLO con Tortuguita
# ----------------------

import turtle

def main():
    window = turtle.Screen()
    tortuguita = turtle.Turtle()

    haz_rentangulo(tortuguita)
    turtle.mainloop()

def haz_rentangulo(tortuguita):
    largo = int(input('Largo: '))
    alto = int(input('Alto: '))

    for i in range(2):
        haz_linea(tortuguita, largo)
        haz_alto(tortuguita, alto)

def haz_linea(tortuguita, largo):
    tortuguita.forward(largo)
    tortuguita.left(90)

def haz_alto(tortuguita, alto):
    tortuguita.forward(alto)
    tortuguita.left(90)


# Para definir donde comienza el código usamos esta línea
if __name__ == "__main__":
    main()
