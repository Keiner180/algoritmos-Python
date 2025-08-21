try:
    with open("archivo_inexistente.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("❌ Error: El archivo no existe.")
