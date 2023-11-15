import funciones as fn
opcion = 1;
#Menu
print("""
    ----------------------------
    Bienvenido a BATALLA NAVAL
    ----------------------------
    Que modo de juego desea jugar?
    1. Jugador 1 vs Jugador 2
    2. Jugador 1 vs CPU
    3. Salir
    """)
if opcion == 1:
    print("Seleccionó. Jugador 1 vs Jugador 2 \n-----------------------------")
    tablero1 = fn.crearTablero(" J1");
    fn.imprimirTablero(tablero1);
    fn.colocarBarcoCasilla(tablero1,3)
    fn.imprimirTablero(tablero1);
    
    tablero2 = fn.crearTablero("J2");
    fn.imprimirTablero(tablero2);
    fn.colocarBarcoCasilla(tablero2,3)
    fn.imprimirTablero(tablero2);