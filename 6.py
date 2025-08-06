# Solicitar los costos al usuario
combustible = float(input("Digite el precio del combustible gastado: "))
peaje = float(input("Digite el precio del peaje: "))
alojamiento = float(input("Digite el precio del alojamiento: "))

costo_total = combustible + peaje + alojamiento

print(f"El costo total del viaje es: ${costo_total:.2f}")
