precio = int(input("Digite el precio del producto: "))
porcentaje = int(input("Digite el porcentaje a aplicar: ")) / 100

total = precio - (precio * porcentaje)

print(f"El precio con el descuento del {porcentaje * 100}% es de {total}")