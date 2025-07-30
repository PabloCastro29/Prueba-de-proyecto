
suma = 0
cantidad = 0

while True:
    numero = float(input("Ingrese un número positivo (negativo para terminar): "))
    if numero < 0:
        break
    suma += numero
    cantidad += 1

if cantidad > 0:
    promedio = suma / cantidad
    print("El promedio es:", promedio)
else:
    print("No ingresó números positivos.")
