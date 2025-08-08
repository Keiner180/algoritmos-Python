import random  # Importamos para poder mezclar aleatoriamente
# Lista de canciones
canciones = [
    "Shape of You - Ed Sheeran",
    "Blinding Lights - The Weeknd",
    "Bohemian Rhapsody - Queen",
    "Bad Guy - Billie Eilish",
    "Despacito - Luis Fonsi",
    "Rolling in the Deep - Adele"
]

print("Lista original de canciones:")
for cancion in canciones:
    print("-", cancion)


random.shuffle(canciones)

# Mostramos la lista aleatoria
print("Lista de reproducción en orden aleatorio:")
for cancion in canciones:
    print("-", cancion)
