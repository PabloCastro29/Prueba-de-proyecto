total_steps = 0
Actual_hour = 0

while total_steps < 10000:
    Ingresed_steps = int(input(f"Ingrese los pasos caminados {Actual_hour}:"))
    total_steps += Ingresed_steps
    Actual_hour += 1

print(f"Felicidades, haz caminado {total_steps}")