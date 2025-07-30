nombres = []

for contador in range(10):
    nombre_ingresado = input("Ingrese un nombre: ")
    nombres.append(nombre_ingresado)

nombres_con_vocal = []

for nombre in nombres:
    if nombre != "": 
        if nombre[0].lower() in "aeiou":
            nombres_con_vocal.append(nombre)

if nombres_con_vocal:
    print("Nombres que empiezan con vocal:")
    for nombre in nombres_con_vocal:
        print(nombre)
else:
    print("No hay ningún nombre que tenga una vocal inicial")
