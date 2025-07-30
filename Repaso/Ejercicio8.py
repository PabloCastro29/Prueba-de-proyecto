import random

numero_secreto = random.randint(1, 10)

while True:
    intento = input("Adivina el número (entre 1 y 10): ")
    try:
        intento = int(intento)
        if intento < 1 or intento > 10:
            print("Por favor, ingresa un número entre 1 y 10.")
            continue
        if intento == numero_secreto:
            print("¡Correcto!")
            break
        else:
            print("Incorrecto, intenta otra vez.")
    except ValueError:
        print("Por favor, ingresa un número válido.")