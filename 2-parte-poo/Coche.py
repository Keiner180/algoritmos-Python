class Motor:
    def arrancar(self):
        print("Motor encendido.")

    def apagar(self):
        print("Motor apagado.")


class Rueda:
    def inflar(self):
        print("Rueda inflada.")

    def desinflar(self):
        print("Rueda desinflada.")


class Ventana:
    def abrir(self):
        print("Ventana abierta.")

    def cerrar(self):
        print("Ventana cerrada.")


class Puerta:
    def __init__(self):
        self.ventana = Ventana()

    def abrir(self):
        print("Puerta abierta.")

    def cerrar(self):
        print("Puerta cerrada.")


class Coche:
    def __init__(self):
        self.motor = Motor()
        self.ruedas = [Rueda() for _ in range(4)]
        self.puertas = [Puerta() for _ in range(2)]

    def encender(self):
        self.motor.arrancar()

    def apagar(self):
        self.motor.apagar()

    def inflar_ruedas(self):
        for i, rueda in enumerate(self.ruedas, 1):
            print(f"Rueda {i}: ", end="")
            rueda.inflar()

    def abrir_puertas(self):
        for i, puerta in enumerate(self.puertas, 1):
            print(f"Puerta {i}: ", end="")
            puerta.abrir()

mi_coche = Coche()

mi_coche.encender()

mi_coche.inflar_ruedas()

mi_coche.abrir_puertas()

mi_coche.apagar()
