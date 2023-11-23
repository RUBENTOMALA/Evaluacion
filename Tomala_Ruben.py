import random

def dado():
    return random.randint(1, 6)

def mover_token(current_position, steps):
    current_position += steps

    # Verificamos si la nueva posición está en una serpiente o escalera
    snakes_and_ladders = {99: 80 , 95:75 , 92: 88, 89: 68, 74:53, 62:19, 64:60 , 46:25, 49:11, 16:6, 2:38, 7:14, 8:31, 15:26, 21:42, 28:84, 36:44, 51:67, 78:98, 71:91, 87:94}
    if current_position in snakes_and_ladders:
        if current_position < snakes_and_ladders[current_position]:
            print("Has caido en una escalera!")
            current_position = snakes_and_ladders[current_position]
        else:
            print("Has caido en una serpiente!")
            current_position = snakes_and_ladders[current_position]
    return current_position

def play_game():
    print("¡Bienvenido a Snakes and Ladders!")
    current_position = 1

    while True:
        input("Presiona Enter para lanzar el dado...")
        pasos = dado()
        print(f"Has lanzado un {pasos}.")
        current_position_aux=current_position
        current_position = mover_token(current_position, pasos)

        print(f"Ahora estás en la casilla {current_position}.")

        if current_position == 100:
            print("¡Felicidades! ¡Has ganado!")
            break
        if current_position>=100:
            current_position=current_position_aux
            print("Te has excedido!")
            
play_game()
