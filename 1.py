cuenta = float(input("Ingrese el monto de la cuenta: "))
porcentaje_propina = float(input("Ingrese el porcentaje de propina: "))

propina = cuenta * (porcentaje_propina / 100)
total = cuenta + propina

print(f"La propina es: ${propina:.2f}")
print(f"El total a pagar es: ${total:.2f}")
