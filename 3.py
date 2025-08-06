edad = int(input("Ingrese la edad de la persona: "))

if edad <= 13:
    print("Clasificación: Niño")
elif edad <= 18:
    print("Clasificación: Adolescente")
else:
    print("Clasificación: Adulto")
