try:
    a = int(input("Ingrese un número: "))
    b = int(input("Ingrese otro número: "))
    print("Resultado:", a / b)
except ZeroDivisionError:
    print("❌ Error: No se puede dividir entre cero.")
