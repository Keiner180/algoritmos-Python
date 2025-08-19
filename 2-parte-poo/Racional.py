from math import gcd

class Racional:
    def __init__(self, numerador=0, denominador=1):
        if denominador == 0:
            raise ValueError("El denominador no puede ser cero.")
        self.numerador = numerador
        self.denominador = denominador
        self.simplificar()

    # Métodos accedentes
    def get_numerador(self):
        return self.numerador

    def get_denominador(self):
        return self.denominador

    # Método para leer valores
    def leer(self):
        self.numerador = int(input("Ingrese numerador: "))
        self.denominador = int(input("Ingrese denominador: "))
        if self.denominador == 0:
            raise ValueError("El denominador no puede ser cero.")
        self.simplificar()

    # Operaciones
    def suma(self, otro):
        num = self.numerador * otro.denominador + otro.numerador * self.denominador
        den = self.denominador * otro.denominador
        return Racional(num, den)

    def resta(self, otro):
        num = self.numerador * otro.denominador - otro.numerador * self.denominador
        den = self.denominador * otro.denominador
        return Racional(num, den)

    def multiplicacion(self, otro):
        num = self.numerador * otro.numerador
        den = self.denominador * otro.denominador
        return Racional(num, den)

    def division(self, otro):
        if otro.numerador == 0:
            raise ValueError("No se puede dividir entre cero.")
        num = self.numerador * otro.denominador
        den = self.denominador * otro.numerador
        return Racional(num, den)

    def simplificar(self):
        divisor = gcd(self.numerador, self.denominador)
        self.numerador //= divisor
        self.denominador //= divisor

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

r1 = Racional(2, 3)
r2 = Racional(4, 5)
print("Multiplicación:", r1.multiplicacion(r2))
