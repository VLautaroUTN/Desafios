"""
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
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizzBuzz():
    for numero in range(101):
        if numero%3 == 0 and numero%5 == 0:
            numero = "fizzbuzz"
        elif numero%3 == 0:
            numero = "fizz"
        elif numero%5 == 0:
            numero = "buzz"
        print(numero)

if __name__ == '__main__':
    fizzBuzz()