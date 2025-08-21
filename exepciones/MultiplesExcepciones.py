try:
    with open("numero.txt", "r") as f:
        valor = int(f.read())
        print("Número leído:", valor)
except (FileNotFoundError, ValueError) as e:
    print("❌ Error al procesar el archivo:", e)
