"""
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
"""

import string
import random

def generadorContrasenas(longitud = 8, mayusculas = True,
    numeros = True, simbolos = True):
    conjuntoTotal = list(string.ascii_lowercase)

    if mayusculas:
        conjuntoTotal += list(string.ascii_uppercase)
    if numeros:
        conjuntoTotal += list(string.digits)
    if simbolos:
        conjuntoTotal += list(string.punctuation)
    
    contrasena = "".join(random.choices(conjuntoTotal, k = longitud))
    return contrasena

def validarLongitud():
    while True:
        longitud = input("Longitud de contraseña: \n-> ")
        try:
            longitud = int(longitud)
        except:
            print("La longitud debe ser un numero")
        if longitud >= 8 and longitud <= 16:
            print("ok")
            return longitud
        else:
            print("Longitud invalida")

def menuSIoNO(textoDeseado):
    while True:
        print("¿Desea incluir " + textoDeseado + " ?")
        eleccion = input("Y / N  \n-> ").lower()
        if eleccion == "y":
            return True
        elif eleccion == "n":
            return False
        else:
            print("Opcion invalida\n \n")

def menuGenContr():
    longi = validarLongitud()
    mayus = menuSIoNO("mayusculas")
    num = menuSIoNO("números")
    simbol = menuSIoNO("simbolos")
    contrasena = generadorContrasenas(longi, mayus, num, simbol)
    print("Su contraseña es: \n" + contrasena)


if __name__ == "__main__":
    menuGenContr()