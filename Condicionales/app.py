""" If """

# En python es distinto el tabulador del espacio, si comienzo a usar uno, debo seguir con el mismo
# Si no, dara un error de compilacion
""" 
edad = 18

if edad > 18 and edad < 45:
    print("Puede pasar")
elif edad <= 0:
    print("No podria ser un humano")
else:
    print("Lo siento no puede pasar") """
    
""" While """


contador = 100
while contador >= 1:
    print(contador)
    #Puedo usar break tambien
    # Tambien la palabra continue que vuelva a entrar en while y no lea lo que sigue
    contador -= 1
    
    
    
    
    
    

""" For 
(En un for puedo poner un else, que se ejecutara si no encuentra ningun break en el for)
"""

""" lista = [1, 2, 3, 4]

for num in lista:
    print(num)
# En el for tambien se puede usar break
    
largoLista = len(lista) # Es como lista.length
 """








""" Encontrar un valor tambien se puede hacer asi """
""" 
if 2 in lista:
    print("Existe el numero 2 en la lista")
    
     """
    
    
    
    
    
    
""" Metodos de lista (Array) """
""" 
sorted(lista)
sorted(lista, reverse=True)


# Match (Switch) Solo de python mayor a 3.10
b = 2

match b:
    case 1:
        print("es uno")
    case 2:
        print("es dos") """