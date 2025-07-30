for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    if num < 0:
        print("Número negativo ingresado. Se detiene el programa.")
        break 