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

def validarLongitud(longitud):
    

if __name__ == "__main__":
    
    generadorContrasenas()