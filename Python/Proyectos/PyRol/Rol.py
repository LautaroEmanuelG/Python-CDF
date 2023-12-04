import random

class Personaje:
    def __init__(self, nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.inteligencia = inteligencia
        self.agilidad = agilidad
        self.fuerza = fuerza

    def atacar(self, enemigo):
        raise NotImplementedError("Método atacar no implementado en la clase base")

class Guerrero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida=100, ataque=10, defensa=8, inteligencia=5, agilidad=5, fuerza=10)

    def atacar(self, enemigo):
        # Implementa la lógica de ataque para el Guerrero
        pass

class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida=80, ataque=12, defensa=5, inteligencia=12, agilidad=6, fuerza=5)

    def atacar(self, enemigo):
        # Implementa la lógica de ataque para el Mago
        pass

class Arquero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida=90, ataque=8, defensa=6, inteligencia=6, agilidad=12, fuerza=7)

    def atacar(self, enemigo):
        # Implementa la lógica de ataque para el Arquero
        pass

class Asesino(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida=85, ataque=10, defensa=7, inteligencia=10, agilidad=10, fuerza=8)

    def atacar(self, enemigo):
        # Implementa la lógica de ataque para el Asesino
        pass

# class EnemigoVolador:
#     def __init__(self, nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza):
#         super().__init__(nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza)
#         self.vuela = True

class Juego:
    def __init__(self):
        self.jugador = None
        self.enemigos = [
            Guerrero("Enemigo Guerrero"),
            Mago("Enemigo Mago"),
            Arquero("Enemigo Arquero"),
            # EnemigoVolador("Enemigo Volador", vida=100, ataque=10, defensa=8, inteligencia=5, agilidad=15, fuerza=10)
        ]

    def seleccionar_clase(self):
        print("Selecciona tu clase:")
        print("1. Guerrero")
        print("2. Mago")
        print("3. Arquero")
        print("4. Asesino")

        opcion = int(input())
        if opcion == 1:
            self.jugador = Guerrero("Jugador Guerrero")
        elif opcion == 2:
            self.jugador = Mago("Jugador Mago")
        elif opcion == 3:
            self.jugador = Arquero("Jugador Arquero")
        elif opcion == 4:
            self.jugador = Asesino("Jugador Asesino")
        else:
            print("Opción no válida. Seleccionando Guerrero por defecto.")
            self.jugador = Guerrero("Jugador Guerrero")

    def combatir(self, enemigo):
        # Implementa la lógica de combate
        pass

    def jugar(self):
        self.seleccionar_clase()

        for encuentro in range(1, 5):
            print(f"\nEncuentro {encuentro}: {self.enemigos[encuentro - 1].nombre}")
            self.combatir(self.enemigos[encuentro - 1])

        print("\n¡Has completado el juego!")

if __name__ == "__main__":
    juego = Juego()
    juego.jugar()
