
""" 
#Funcion Tradicional

def saludar (nombre):
    return "Hola " + nombre

print(saludar("Guille"))
 """



"""  
# Sobreescribo el valor global de la variable

nombre = "Angel"

def saludar (nombre):
    global nombre
    nombre = "Guille"
    return "Hola " + nombre

 """
 
""" 
# Parametro por defecto u opcionales, siempre tienen que ser los ultimos ej: Esto no puedo (a="5",b,c)

def saludar (nombre="Angel"):
    return "Hola " + nombre

print(saludar())
"""

""" 
# Puedo pasar solo un parametro

def suma (a="1", b="1", c="1")
    return a + b + c
    
suma(c="7")

"""


""" 
# Argumentos, remplaza por una lista

def suma (*args)
    result = 0
    for i in args:
        result += i
    return result
    
suma(5,6,8,4)

"""

""" 
# Argumentos, remplaza por una lista

def automovil (**kwargs)
    if "auto" in kwargs and kwargs["auto"] === "rojo"
        return "El auto es rojo"
    
automovil (auto="rojo")

"""


""" 
# Return multiple

def operaciones (a, b)
    return a + b, a - b, a * b, a // c
    
suma(7,5) # retorna una tupla con los valores


# se puede hacer un destructuring

suma, resta, multi, divi = suma(7,5) # Se guardara cada uno

"""



""" 
# Operador ternario
# esto if condicion else resolucion

result = 8 + 5 if 8 + 5 > 10 else 0

"""

""" 
# Funciones anonimas

# Funciona como las flechas, es decir si solo returna pues no ponemos return
saludar = lambda nombre : "Hola, " + nombre
"""
    





def añoBisiesto (año):
    return año % 4 == 0

print(añoBisiesto(1992))
print(añoBisiesto(1990))