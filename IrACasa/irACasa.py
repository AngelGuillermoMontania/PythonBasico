import time

def irACasa ():
    if(time.localtime().tm_hour >= 19 & time.localtime().tm_hour <= 11):
        return "No es horario de trabajo"
    else:
        return "Faltan " + str(19 - time.localtime().tm_hour) +  " horas con " + str(time.localtime().tm_min) + " minutos para salir del trabajo"