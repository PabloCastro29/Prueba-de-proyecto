cantidad = int(input("Cuantas personas quiere ingresar: "))
Ages = []
for number in range (cantidad):
    age = int(input(f"escriba la edad de la personas: "))
    Ages.append(age)
print("Las edades ingresadas son:")
print(Ages)
Mayores = 0
for age in Ages:
    if age >=18:
        Mayores +=1
print(f"La cantidad de personas mayores de edad es: {Mayores}")

suma = sum(Ages)
promedio = suma / cantidad
print(f"La suma de las edades es: {suma}")