# Lista de cumpleaños (nombre, fecha en formato DD/MM/AAAA)
cumpleaños = [
    ("Ana", "14/03/2000"),
    ("Pedro", "25/07/1998"),
    ("Laura", "05/03/2001"),
    ("Carlos", "19/12/1999"),
    ("Marta", "02/07/2002"),
    ("Luis", "28/12/1995")
]

por_mes = {
    "Enero": [],
    "Febrero": [],
    "Marzo": [],
    "Abril": [],
    "Mayo": [],
    "Junio": [],
    "Julio": [],
    "Agosto": [],
    "Septiembre": [],
    "Octubre": [],
    "Noviembre": [],
    "Diciembre": []
}

for nombre, fecha in cumpleaños:
    dia, mes, año = fecha.split("/")
    mes = int(mes)
    lista_meses = list(por_mes.keys())
    mes_nombre = lista_meses[mes - 1]
    por_mes[mes_nombre].append((nombre, fecha))

# Mostrar resultados
for mes, lista in por_mes.items():
    print(f"{mes}:")
    for nombre, fecha in lista:
        print(f"  - {nombre} ({fecha})")
