class Cuenta:
    def __init__(self, dni=0, saldo=0.0, interes_anual=0.0):
        from random import randint
        self.__numero_cuenta = randint(10000000, 99999999)  # Se genera automáticamente
        self.dni = dni
        self.saldo = saldo
        self.interes_anual = interes_anual

    # Accedentes
    def get_numero_cuenta(self):
        return self.__numero_cuenta

    def get_dni(self):
        return self.dni

    def get_saldo(self):
        return self.saldo

    def get_interes_anual(self):
        return self.interes_anual

    # Mutadores
    def set_dni(self, dni):
        self.dni = dni

    def set_saldo(self, saldo):
        self.saldo = saldo

    def set_interes_anual(self, interes):
        self.interes_anual = interes

    # Métodos de operación
    def actualizarSaldo(self):
        interes_diario = self.interes_anual / 365 / 100
        self.saldo += self.saldo * interes_diario

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad

    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Fondos insuficientes.")

    def mostrarDatos(self):
        print(f"Cuenta: {self.__numero_cuenta}")
        print(f"DNI: {self.dni}")
        print(f"Saldo: {self.saldo:.2f}")
        print(f"Interés anual: {self.interes_anual}%")

cuenta1 = Cuenta(12345678, 1000, 10)  # DNI, saldo inicial, interés anual
cuenta1.mostrarDatos()

