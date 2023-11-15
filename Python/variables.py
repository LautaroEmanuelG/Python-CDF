import random

def imprimir_tablero(tablero):
    """
    Imprime el tablero actualizado.
    """
    for fila in tablero:
        print("|".join(fila))
        print("-" * 5)

def verificar_ganador(tablero, jugador):
    """
    Verifica si el jugador actual ha ganado.
    """
    # Verificar filas y columnas
    for i in range(3):
        if all(tablero[i][j] == jugador for j in range(3)) or all(tablero[j][i] == jugador for j in range(3)):
            return True

    # Verificar diagonales
    if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2 - i] == jugador for i in range(3)):
        return True

    return False

def tablero_lleno(tablero):
    """
    Verifica si el tablero está lleno.
    """
    return all(tablero[i][j] != ' ' for i in range(3) for j in range(3))

def jugar_tateti():
    """
    Función principal para jugar al ta-te-ti.
    """
    tablero = [[' ' for _ in range(3)] for _ in range(3)]
    jugador = 'X'
    computadora = 'O'

    while True:
        imprimir_tablero(tablero)

        # Turno del jugador
        fila = int(input("Ingrese el número de fila (0, 1, 2): "))
        columna = int(input("Ingrese el número de columna (0, 1, 2): "))

        if tablero[fila][columna] == ' ':
            tablero[fila][columna] = jugador
        else:
            print("Esa posición ya está ocupada. Intente de nuevo.")
            continue

        if verificar_ganador(tablero, jugador):
            imprimir_tablero(tablero)
            print("¡Felicidades! Has ganado.")
            break

        if tablero_lleno(tablero):
            imprimir_tablero(tablero)
            print("El juego ha terminado en empate.")
            break

        # Turno de la computadora
        print("Turno de la computadora:")
        while True:
            fila_computadora = random.randint(0, 2)
            columna_computadora = random.randint(0, 2)

            if tablero[fila_computadora][columna_computadora] == ' ':
                tablero[fila_computadora][columna_computadora] = computadora
                break

        if verificar_ganador(tablero, computadora):
            imprimir_tablero(tablero)
            print("La computadora ha ganado. ¡Suerte la próxima vez!")
            break

        if tablero_lleno(tablero):
            imprimir_tablero(tablero)
            print("El juego ha terminado en empate.")
            break

if __name__ == "__main__":
    jugar_tateti()
