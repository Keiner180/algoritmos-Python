lista = []

print("Los puestos disponibles son los #: ")


for i in range(5):
    fila = []
    for j in range(5):
        fila.append("#")
    lista.append(fila)

for fila in lista:
    print(" ".join(fila))  

    


while True:
    
    print("Si desea salir ponga el numero 6 en fila o columa")
    puestoReservarFila = int(input("Ingrese la fila que desea el puesto: ")) - 1
    puestoReservarColumna = int(input("Ingrese la columa que desea el puesto: ")) -1
    
    if(puestoReservarColumna == 0 or puestoReservarFila == 0):
        break

    if(lista[puestoReservarFila][puestoReservarColumna] == "#"):
        print("Puesto reservado con éxito")
        lista[puestoReservarFila][puestoReservarColumna] = "R"
    else:
        print("Puesto ha sido reservado por otra persona")
        
    for fila in lista:
        print(" ".join(fila))  
        
    

