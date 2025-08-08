presupuesto = float(input("Ingrese su presupuesto mensual: "))
num_gastos = int(input("¿Cuántos gastos desea registrar?: "))

total_gastos = 0

for i in range(num_gastos):
    gasto = float(input(f"Ingrese el valor del gasto {i+1}: "))
    total_gastos += gasto

saldo = presupuesto - total_gastos

# Mostrar resultado
print(f"\nPresupuesto inicial: ${presupuesto:.2f}")
print(f"Total de gastos: ${total_gastos:.2f}")
print(f"Saldo restante: ${saldo:.2f}")
