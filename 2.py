print("Conversor de Moneda")
print("1. Dólares a Euros")
print("2. Euros a Dólares")

opcion = input("Seleccione una opción (1 o 2): ")

if opcion == "1":
    dolares = float(input("Ingrese la cantidad en dólares: "))
    tasa_euro = float(input("Ingrese la tasa de conversión de dólar a euro: "))
    euros = dolares * tasa_euro
    print(f"La cantidad equivalente en euros es: €{euros:.2f}")

elif opcion == "2":
    euros = float(input("Ingrese la cantidad en euros: "))
    tasa_dolar = float(input("Ingrese la tasa de conversión de euro a dólar: "))
    dolares = euros * tasa_dolar
    print(f"La cantidad equivalente en dólares es: ${dolares:.2f}")

else:
    print("Opción inválida. Por favor elija 1 o 2.")
