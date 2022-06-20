#! / Usr / bin / env python
# - * - Codificación: utf-8 - *

def c_mayusculas (cadena):
    cont = 0
    for i in cadena:
        if i != i.lower(): #Recordar que lower() convierte una cadena en minúsculas
            cont += 1
    print ("La_cadena_tiene"), cont, "mayuscula/s"