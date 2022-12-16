""" import _thread
import time

def horaActual(nombreHilo, tiempo):
    count = 0
    
    while count < 5:
        time.sleep(tiempo)
        count += 1
        print(f"hilo: {nombreHilo}, - {time.ctime(time.time())}")
        

_thread.start_new_thread(horaActual, ("hilo Uno", 1))        
_thread.start_new_thread(horaActual, ("hilo Dos", 2))

while True:
    pass
 """
 
 
 
 
 
 
 
 
 
"""  
from functools import reduce
 
newList = filter(lambda x: x > 5, [2,7,6,3,-5])
print(list(newList))

listMap = map(lambda x: x * 2, [2,7,6,3,-5])
print(list(listMap))

numReduce = reduce(lambda a,b: a + b, [2,7,6,3,-5])
print(numReduce)
 """
 
 
 
 
 
"""  
nombres = ["Angel", "Caro"]
edad = [30,19]
personas = zip(nombres, edad)
print(list(personas))
 """
 



from functools import reduce

listFilter = filter(lambda x: x % 2 != 0, [57,88,21,33,22,94,9,2,36,77])
sumList = reduce(lambda a,b: a + b, listFilter)
print(sumList)