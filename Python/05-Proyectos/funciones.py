# Presentacion de Batalla Naval
# Jugadores: Jugador 1 vs Jugador 2
# o jugador 1 vs CPU
# Si es jugador1 vs jugador 2 un barco de 3 casillas
# jugador 1 5 barcos de una casilla y cpu barco de 3 casillas random
# Los barcos de 3 casillas horizontal o vertical
# El mapa es de 6x6 una matriz
# Casilla Vacia " ",casilla disparada "X", casilla con barco "B"

def crearTablero(jugador):
    tablero = []
    for i in range(6):
        fila = []
        for j in range(6):
            if j == 0:
                fila.append(f"{i+1}|")
            fila.append("|_|")
        tablero.append(fila)
    ultFila = []
    for l in range(7):
        if l == 0:
            ultFila.append(f"{jugador}")
        else:
            ultFila.append(f"|{l}|")
    tablero.append(ultFila)
    return tablero


def imprimirTablero(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            print(tablero[i][j], end=" ")
        print()


def colocarBarcoCasilla(tablero, barco):
    fila = 0
    col = 0
    print("Coloca tu Barco")
    while True:
        casilla = input("¿En que casilla quieres colocarlo?\n(Ej:2-2 o 1 1)\n----->")
        fila = int(casilla[0])
        col = int(casilla[2])
        print("fila: ",fila,"columna: ",col)
        if 0 <= fila <= 5 and 1 <= col <= 6:
            tablero[fila][col] = "|B|"
            colocarBarcoDireccion(tablero,fila,col)
            break
        else:
            print("!!! ---- No es una casilla valida ---- !!!")
    #Chequear que barco es
    
def colocarBarcoDireccion(tablero,fila, col):
    dir = 5
    while dir != 0:
        dir=int(input("""
¿En que direccion lo colocamos?
    1.Horizontal (Hacia la derecha)
    2.Vertical (Hacia abajo)
    0.Para cambiar casilla\n
----->"""))
        if dir == 1:
            if tablero[fila][col+2] == "|_|":
                tablero[fila][col+1] = "|B|"
                tablero[fila][col+2] = "|B|"
                return True
            else:
                "No es posible colocarlo en esa direccion"
                dir=5
        elif dir == 2:
            if tablero[fila+2][col] == "|_|": 
                tablero[fila+1][col] = "|B|"
                tablero[fila+2][col] = "|B|"
                return True
            else:
                "No es posible colocarlo en esa direccion"
                dir=5
        elif dir == 0:
            colocarBarcoCasilla(tablero,0)
        else: print("No es una opcion valida")
