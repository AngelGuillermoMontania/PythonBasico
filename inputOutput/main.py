import pprint
import pickle

# forma menos usada print("%s me llamo %s".format("Hola", "Angel"))
"""
saludo = "Hola"
nombre = "Guille"

print(f"{saludo} me llamo {nombre}")
 """
""" 
    DIFERENCIA ENTRE STR Y REPR
    
    str es para salida informal, produccion
    repr es para depuracion y desarrollo
    
"""

# f = open('/etc/passwd', "r")
# r = read
# w = write
# a = append (Agrega algo, no puede escribir algo del inicio)


# pprint.pprint(f.read())

# import pickle        sirve para serializar o deserializar


""" open('./nuevoArchivo.txt', "w").write("Este es el texto del archivo")
txt = open('./nuevoArchivo.txt', "r")
print(txt.read()) """




class Vehiculo:
    
    def __init__(self, color) -> None:
        self.color = color

Ferrari = Vehiculo("rojo")
pickle.dump(Ferrari, open("./ferrari.bin", "wb"))
mismoFerrari = pickle.load(open("./ferrari.bin", "rb"))

print(type(mismoFerrari))