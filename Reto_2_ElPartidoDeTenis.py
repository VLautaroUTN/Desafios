"""
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
"""
puntajes = [0,15, 30, 40, "deuce", "ventaja", "ganador"]
jugador1 = 0
jugador2 = 0

def sumarPuntos(jugador):
    if jugador.lower() == "p1":
        jugador1 += 1
    elif jugador.lower() == "p2":
        jugador2 += 1
    else:
        print("jugador no valido")

def partidoDeTenis():
    while True:
        diferencia = jugador1 - jugador2
        if diferencia == 0 and jugador1 == 3:
            print(puntajes[4])
        elif diferencia == 1 and jugador1 >= 3 or jugador2 >= 3:
            print(puntajes[5])
    

if __name__ == "__main__":
    partidoDeTEnis()