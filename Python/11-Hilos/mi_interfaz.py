import PySimpleGUI as pg

pg.theme("Topanga")

layout = [
    [pg.Text('MI INTERFAZ',
             key='-TEXT-', font=('Arial Bold', 20),
             expand_x=True, justification='center')],
    [pg.InputText(key="num1"), pg.InputText(key="num2")],
    [pg.Button("+", size=(20, 2)), pg.Button("-", size=(20, 2)),
     pg.Button("*", size=(20, 2)), pg.Button("/", size=(20, 2))],
    [pg.Slider((0, 10), orientation="h")],
    [pg.Button("Pegar")],
    [pg.Output(size=(80, 10))]
]

ventana = pg.Window("Mi aplicacion", layout)


def sumar(*args):
    return sum(args)


def restar(*args):
    return args[0] - args[1]


def multiplicar(*args):
    return args[0] * args[1]


def dividir(*args):
    return args[0] / args[1]


while True:
    evento, valor = ventana.read()
    if evento == pg.WIN_CLOSED:
        ventana.close()
        break
    if evento == "+":
        print(sumar(int(valor["num1"]), int(valor["num2"])))
    if evento == "-":
        print(restar(int(valor["num1"]), int(valor["num2"])))
    if evento == "*":
        print(multiplicar(int(valor["num1"]), int(valor["num2"])))
    if evento == "/":
        print(dividir(int(valor["num1"]), int(valor["num2"])))
