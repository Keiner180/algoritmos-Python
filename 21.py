
numero = int(input("Ingresa un número: "))

es_primo = True  #

if numero <= 1:
    es_primo = False
else:
    for i in range(2, int(numero // 2) + 1):  
        if numero % i == 0:
            es_primo = False
            break

# Salida
if es_primo:
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} NO es un número primo.")
