lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

comunes = [elemento for elemento in lista1 if elemento in lista2]

# Eliminar duplicados usando set
comunes = list(set(comunes))

print("Elementos comunes:", comunes)
