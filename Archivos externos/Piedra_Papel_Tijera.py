import random

jugador_gana = 0
computadora_gana = 0

print("Juguemos a piedra, papel o tijera")

# Mientras ninguno haya ganado 2 veces
while jugador_gana < 2 and computadora_gana < 2:
    eleccion_jugador = input("\nElige piedra, papel o tijera: ").lower()
    opciones = ["piedra", "papel", "tijera"]
    eleccion_computadora = random.choice(opciones)
    print(f"La computadora eligió: {eleccion_computadora}")

    # Determinar el ganador de la ronda
    if (eleccion_jugador == "piedra" and eleccion_computadora == "tijera") or \
       (eleccion_jugador == "tijera" and eleccion_computadora == "papel") or \
       (eleccion_jugador == "papel" and eleccion_computadora == "piedra"):
        ganador = "Jugador"
    elif eleccion_jugador == eleccion_computadora:
        ganador = "Empate"
    else:
        ganador = "Computadora"

    # Actualizar el puntaje
    if ganador == "Jugador":
        jugador_gana += 1
        print("Ganaste esta ronda")
    elif ganador == "Computadora":
        computadora_gana += 1
        print("La computadora ganó esta ronda")
    else:
        print("Es un empate")

    print(f"Puntaje actual - Jugador: {jugador_gana}, Computadora: {computadora_gana}")

# Determinar el ganador final
if jugador_gana > computadora_gana:
    print("¡Felicidades! Ganaste el mejor de tres.")
else:
    print("La computadora ganó el mejor de tres. ¡Suerte para la próxima!")
  