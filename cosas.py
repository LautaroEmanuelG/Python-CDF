casilla = input("¿En que casilla quieres colocarlo?\n(Ej:2-2 o 1 1)\n----->")
fila = int(casilla[0])
casilla_str = list(casilla)
casilla_str.append("-")
print(casilla_str)
for num in "123456789":
    if casilla_str[2] == num:
        col = int(casilla_str[2])
    elif casilla_str[1] == num:
        col = int(casilla_str[1])
        
print(col)