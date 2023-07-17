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
class PartidoDeTenis():
    def __init__(self):
        self.puntaje = [0,15, 30, 40, "deuce", "ventaja", "ganador"]
        self.jugador1 = 0
        self.jugador2 = 0

    def sumarPuntos(self, jugador):  # Se encarga de sumar los puntos
        if jugador.lower() == "p1":
            self.jugador1 += 1
        elif jugador.lower() == "p2":
            self.jugador2 += 1
        else:
            print("jugador no valido \n Debe escibirlo como p1 o p2")

    def main(self):
        while True:
            self.sumarPuntos(input("¿Quien anotó? (p1 - p2)"))
            diferencia = self.jugador1 - self.jugador2
            print(self.jugador1,"-",self.jugador2)
            print("Dif:", diferencia)
            if diferencia == 0 and self.jugador1 == 3:
                print(self.puntaje[4]) #Deuce
            elif diferencia == 1 and self.jugador1 >= 3 or self.jugador2 >= 3:
                print(self.puntaje[5]) #Ventaja
            elif diferencia == 4:
                print(self.puntaje[6], "p1")
                break

if __name__ == "__main__":
    partido = PartidoDeTenis()
    partido.main()