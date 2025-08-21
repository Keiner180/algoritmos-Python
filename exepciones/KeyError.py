try:
    dic = {"nombre": "Keiner"}
    print(dic["edad"])
except KeyError:
    print("❌ Error: La clave no existe en el diccionario.")
