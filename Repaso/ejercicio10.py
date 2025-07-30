Lista = []
suma_total = 0
for i in range (5):
    number = float(input(f"Ingrese el número {i+1}: "))
    Lista.append(number)
    suma_total += number
print(f"La lista de números es: {Lista}")
print(f"La suma total es: {suma_total}")