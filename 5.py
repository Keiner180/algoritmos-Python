# Lista vacía para almacenar los productos
lista_compras = []

while True:
    print("\n===== MENÚ =====")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Mostrar lista de compras")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        producto = input("Ingrese el nombre del producto a agregar: ")
        lista_compras.append(producto)
        print(f"'{producto}' agregado a la lista.")

    elif opcion == "2":
        producto = input("Ingrese el nombre del producto a eliminar: ")
        if producto in lista_compras:
            lista_compras.remove(producto)
            print(f"'{producto}' eliminado de la lista.")
        else:
            print(f"El producto '{producto}' no está en la lista.")

    elif opcion == "3":
        if lista_compras:
            print("Lista de compras:")
            for i, item in enumerate(lista_compras, 1):
                print(f"{i}. {item}")
        else:
            print("La lista está vacía.")

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intente de nuevo.")
