kg = input("Ingrese su peso en kg ")
estatura = input("Ingrese su estatura en metros ")
indice = int(float(kg) / (float(estatura) ** 2))
print("Tu índice de masa corporal es donde es " + str(indice))