""" import operadores
import operaciones.resta
import math
import pprint """
""" from operaciones import *  # Esto solo funciona si en el __init__ del paquete coloco los exports correspondientes en __all__ """

# pypi.org   es para buscar 
# dir() devuelve los metodos o todo lo que tenga un modulo o paquete, lo recibe por param
# podria ver todos los metodos de string escribiendo dir("")
# Para usar por ejemplo math (Como en js) debo primero importarlo

# si invoco globals(), va a mostrar la TABLA DE SIMBOLOS seria como el ambiente de ejecucion global
# si invoco locals(), va a mostrar la TABLA DE SIMBOLOS pero del ambiente local donde lo ejecute
""" 
def main():
    print(operadores.suma(5,9))
    print(operaciones.resta.resta(5,2))
    pprint.pprint(math)
    help(math.floor)
    # Es una convencion hacer esto de main, puerta de entrada
if(__name__ == "__main__"):
    main()
     """
     
     
import operaciones.suma
import operaciones.resta
import operaciones.multiplica
import operaciones.divide

def main():
    print(operaciones.suma.suma(5,5))
    print(operaciones.resta.resta(5,5))
    print(operaciones.multiplica.multiplica(5,5))
    print(operaciones.divide.divide(5,5))
if(__name__ == "__main__"):
    main()