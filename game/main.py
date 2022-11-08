import random
#Definimos las variables globaales
options = ["Piedra", "Papel", "Tijera"]


#Metodo de comprobacion de ganador
def game(player, computer):
    if player == "Piedra" and computer == "Tijera":
        return "player", "El ganador es el jugador de la Ronda"
    elif player == "Papel" and computer == "Piedra":
        return "player", "El ganador es el jugador de la Ronda"
    elif player == "Tijera" and computer == "Papel":
        return "player", "El ganador es el jugador de la Ronda"
    elif player == computer:
        return None, "Ha ocurrido un empate en la Ronda"
    else:
        return "computer", "El ganador es la computadora de la Ronda"

#Funcion de eleccion
def rps(choice):
    for i in options:
        if i == choice:
            return(True, i)
    print("Has introducido una opcion incorrecta")
    return(False, None)

#Logica del juego
def main():

    print("El juego esta por comenzar")
    player_points = 0
    computer_points = 0
    round = 0
    while player_points != 2 and computer_points != 2:
        round += 1
        print("Comienza la ** RONDA", round, "**")
        print("El jugador tiene:", player_points)
        print("La computadora tiene:", computer_points,"\n")
        aux = False
        while aux == False:
            aux, player = rps(input("Elige Piedra Papel o Tijera ").casefold().capitalize())

        print("El jugador a elegido", player)

        computer = rps(random.choice(options))[1]
        print("La computadora a elegido", computer)

        win, msj = game(player, computer)
        if win == "player":
            player_points += 1
        elif win == "computer":
            computer_points += 1

        print(msj + "\n")
    if player_points > computer_points:
        winner = "Jugador"
    else:
        winner = "Computadora"
    print("El ganador de la partida ha sido", winner)

if __name__ == "__main__":
    main()