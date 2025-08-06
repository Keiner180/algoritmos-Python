monto = float(input("Ingrese el monto del préstamo: "))
tasa_anual = float(input("Ingrese la tasa de interés anual (en %): "))
meses = int(input("Ingrese el número de meses: "))

tasa_mensual = tasa_anual / 12 / 100

if tasa_mensual == 0:
    cuota = monto / meses  # Sin interés
else:
    cuota = monto * (tasa_mensual * (1 + tasa_mensual)**meses) / ((1 + tasa_mensual)**meses - 1)

# Mostrar el resultado
print(f"El pago mensual es: ${cuota:.2f}")
