
lista = ["manzana", "pera", "uva", "mango"]

# Elemento a buscar
elemento = input("Ingresa el elemento que quieres buscar: ")

# Verificar si está en la lista
if elemento in lista:
    print(f"El elemento '{elemento}' SÍ está en la lista.")
else:
    print(f"El elemento '{elemento}' NO está en la lista.")
