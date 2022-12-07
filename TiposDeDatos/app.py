""" Lista 
    Puedo poner cualquier tipo... los booleanos son con mayuscula al inicio
"""

list = ["a", 5, True, 5.5]
print(list)
list.append("Hola")
list.remove("Hola")
print(list)

""" Diccionario  (Es como un objeto) """

a = {
    "nombre": "Angel",
    "apellido": "Montania"
}

print(a["nombre"])

a.pop("nombre")  
# Pop devuelve el valor eliminado


""" Conjunto, No puede repetir valores """

conjunto = { 1, 2, 3, 1, 2, 3 }
print(conjunto)

conjunto2 = {4, 5, 6}

conjunto | conjunto2
# Union, Une los dos conjuntos quitando obviamente los repetidos

conjunto & conjunto2
# Interseccion. Busca los valores que coincidan entre los conjuntos

conjunto - conjunto2
# Diferencia, entre conjunto y conjunto2. Mostrara los distintos que tiene conjunto

conjunto ^ conjunto2
# Diferencia simetrica, entre conjunto y conjunto2. Mostrara los distintos que tiene conjunto




""" Metodos de string """

texto = "Hola"

texto.capitalize()
texto.title()
texto.upper()
texto.lower()
texto.replace("h", "a")
texto.find("la")
texto.split()
"".join(list)





""" Operadores aritmeticos """

21 // 5 # Division Flotante
21 / 5 # Division entero 

20 ** 2 # Potencia

a = 5

a *= 5
a /= 5
a **= 5

""" Operadores Logicos """

True and True
True or False
not True

""" Funcion Type """
type(True)




""" Casos locos """

3 * "Python" #  "PythonPythonPython"
