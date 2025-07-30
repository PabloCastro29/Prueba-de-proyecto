limit_number = int(input("Ingrese un número límite: "))
suma_pares = 0
for valor in range(1, limit_number + 1):
    if valor % 2 == 0:
        suma_pares += valor
print("La suma de los números pares hasta", limit_number, "es:", suma_pares)