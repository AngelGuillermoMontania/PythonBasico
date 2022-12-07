""" Herencia """
""" class Objeto:
    _encendido: False
    
    def encenderApagar (self): #el parametro es para poder usar las variables de la clase
        self._encendido = not self._encendido
        
    def isEncendido (self):
        return self._encendido
    
        
        

class Lampara(Objeto):
    _funciona: True
        
    def isFunciona (self):
        return self._color
        
lamp1 = Lampara()
lamp1.encenderApagar()
print(dir(lamp1)) # Me permite ver todo el contenido de la clase
 """
# No existe private, public y demas... Son solo public
# con _ podemos indicar los que no deberian tocarse




""" Clase estatica, es decir que no tiene instancias """
""" 
class Estatica:
    count = 0
    
    def sumar():
        Estatica.count += 1
        
        
      """   
        
        
        
        
        
""" Constructor """
""" 
class Animal:
    
    def __init__(self, vive):
        self.vive = vive

class Perro(Animal):
    
    def __init__(self, vive, nombre): #Constructor con __init__
        super().__init__(vive)   # Super... para el constructor del padre
        self.nombre = nombre
    
    def __str__(self): # Es como la funcion toString de Java, mostrara lo que diga aca al hacer print
        return "El nombre del perro es " + self.nombre
    
sanson = Perro(True, "Sanson")
print(sanson) """
# La declaracion pass, es como un return. Simplemente no hace nada








""" 
class Vehiculo:
    
    def __init__(self, Color, Ruedas, Puertas):
        self.Color = Color
        self.Ruedas = Ruedas
        self.Puertas = Puertas

class Coche(Vehiculo):
    
    def __init__(self, Color, Ruedas, Puertas, Velocidad, Cilindrada):
        super().__init__(Color, Ruedas, Puertas)
        self.Velocidad = Velocidad
        self.Cilindrada = Cilindrada
        
    def __str__(self):
        return self.Color + " " + str(self.Ruedas) + " " + str(self.Puertas) + " " + str(self.Velocidad) + " " + str(self.Cilindrada) + " " + str(self.__class__)
        
FordEscort = Coche("Rojo", 4, 5, 160, 1500)

print(FordEscort)

 """
 
 
 
 
 
 
 
 
class Alumno:
    
    def __init__(self, nombre, nota):
        self._nombre = nombre
        self._nota = nota
    
    def verNombre(self):
        return self._nombre
    
    def verNota(self):
        return self._nota
    
    def isAprueba(self):
        return self._nota > 6
    

Angel = Alumno("Angel", 7)
print(Angel.verNota())
print(Angel.isAprueba())