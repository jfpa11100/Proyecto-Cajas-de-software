class Jugador:
    def __init__(self, nombre, numero) -> None:
        self.Nombre = nombre
        self.Numero = numero
        self.Puntuacion = None

    def Registrar(self, Juego):
        Juego.Guardar_Jugador(self)

    def Adivinar(self, intento, Juego):
        Juego.Verificar_intento(intento)

    def __repr__(self) -> str:
        return repr(f"Jugador {self.Nombre}, num: {self.Numero}")