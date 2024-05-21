'''Piedra, papel y tijera. En cada ronda del juego del cachipún, los dos competidores
deben elegir entre jugar tijera, papel o piedra.
Las reglas para decidir quién gana la ronda son: tijera le gana a papel, papel le gana a
piedra, piedra le gana a tijera, y todas las demás combinaciones son empates.
El ganador del juego es el primero que gane tres rondas.
Escriba un programa que pregunte a cada jugador cuál es su jugada, muestre cuál es el
marcador después de cada ronda, y termine cuando uno de ellos haya ganado tres
rondas. Los jugadores deben indicar su jugada escribiendo tijera, papel o piedra.'''

Piedra = 1
Papel = 2
Tijera = 3
resultado_jugador1 = 0
resultado_jugador2 = 0
while resultado_jugador1 < 3 and resultado_jugador2 < 3:
    Jugador1 = int(input("Jugador numero 1.Ingresa un movimiento (1 = Piedra, 2 = Papel o 3 = Tijera): "))
    Jugador2 = int(input("Jugador numero 2.Ingresa un movimiento (1 = Piedra, 2 = Papel o 3 = Tijera): "))
    if Jugador1 == Piedra and Jugador2 == Papel or Jugador1 == Papel and Jugador2 == Tijera or Jugador1 == Tijera and Jugador2 == Piedra:
        print ("Punto para el jugador 2.")
        resultado_jugador2 += 1
    elif Jugador2 == Piedra and Jugador1 == Papel or Jugador2 == Papel and Jugador1 == Tijera or Jugador2 == Tijera and Jugador1 == Piedra:
        print ("Punto para el jugador 1.")
        resultado_jugador1 += 1
    elif Jugador1 == Piedra and Jugador2 == Piedra or Jugador1 == Papel and Jugador2 == Papel or Jugador1 == Tijera and Jugador2 == Tijera:
        print("Usaron el mismo movimiento , intenten de vuelta.")
    elif Jugador1 and Jugador2 != Piedra and Papel and Tijera:
        print("El movimiento no es correcto vuelve a intentarlo.")
if resultado_jugador1 ==3:
    print("El jugador numero 1 gana ¡Felicitaciones!.")
if resultado_jugador2 ==3:
    print("El jugador numero 2 gana ¡Felicitaciones!.")
