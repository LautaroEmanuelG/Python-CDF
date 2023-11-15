import random

# Función para imprimir el tablero
def print_board(board):
    for row in board:
        print(" ".join(row))

# Función para colocar el barco en el tablero
def place_ship(board, ship_row, ship_col, direction):
    if direction == "horizontal":
        for i in range(3):
            board[ship_row][ship_col + i] = "S"
    elif direction == "vertical":
        for i in range(3):
            board[ship_row + i][ship_col] = "S"

# Función principal del juego
def battleship_game():
    # Crear un tablero de 5x5
    board = [["O"] * 5 for _ in range(5)]

    # Imprimir el tablero inicial
    print("Tablero de Batalla Naval:")
    print_board(board)

    # Colocar el barco de tres casillas
    ship_row = random.randint(0, 2)
    ship_col = random.randint(0, 2)
    direction = random.choice(["horizontal", "vertical"])
    place_ship(board, ship_row, ship_col, direction)

    # Juego
    for turn in range(3):
        print(f"\nTurno {turn + 1}")
        guess_row = int(input("Fila (0-4): "))
        guess_col = int(input("Columna (0-4): "))

        # Verificar si el jugador ha acertado
        if board[guess_row][guess_col] == "S":
            print("¡Felicidades! ¡Hundiste el barco!")
            break
        else:
            print("¡Agua! Inténtalo de nuevo.")

        # Imprimir el tablero actualizado
        board[guess_row][guess_col] = "X"
        print_board(board)

        if turn == 2:
            print("\nFin del juego. ¡No hundiste el barco!")

# Iniciar el juego
battleship_game()
