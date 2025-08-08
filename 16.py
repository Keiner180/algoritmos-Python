distancia = float(input("Ingrese la distancia a recorrer (en km): "))
velocidad = float(input("Ingrese la velocidad promedio (en km/h): "))

if velocidad > 0:
    tiempo = distancia / velocidad
    print(f"El tiempo de viaje es: {tiempo:.2f} horas")
else:
    print("La velocidad debe ser mayor que 0")
