Estudiantes = []

Cantidad = int(input("Ingrese el numero de los estudiantes que registrara: "))
for num in range(Cantidad):
    print(f"\nEstudiante {num + 1}:")
    nombre = input("Ingrese el nombre del estudiante: ")
    nota1 = float(input("Ingrese la nota 1 : "))
    nota2 = float(input("Ingrese la segunda nota: "))

    promedio = (nota1 + nota2) /2
    
    Estudiante = {
        "nombre" : nombre,
        "nota1" : nota1,
        "nota2" : nota2,
        "promedio": promedio
    }

    Estudiantes.append(Estudiante)

print("\nListado de estudiantes:")
for est in Estudiantes:
    print(f"Nombre: {est['nombre']}, promedio: {est['promedio']}")

aprobados = 0 
for est in Estudiantes:
    if est['promedio'] >=60:
        aprobados +=1
