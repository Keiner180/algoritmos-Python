try:
    numero = int(input("Ingrese un número entero: "))
    print("Número válido:", numero)
except ValueError:
    print("❌ Error: Debe ingresar un número entero válido.")
