Nombres = []
for i in range(4):
    nombre = input(f"Ingrese el nombre {i+1}: ")
    Nombres.append(nombre)
print("Saludos a:")
for personas in Nombres:
    print(f"Hola, {personas}!") 