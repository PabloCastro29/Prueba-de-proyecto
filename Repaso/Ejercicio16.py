empleados = []

cantidad = int(input("Ingrese los empleados que desea ingresar:  "))

for num in range(cantidad):
    print(f"\nEmpleado {num + 1}:")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    puesto = input("Puesto: ")
    
    empleado = {
        "nombre": nombre,
        "edad": edad,
        "puesto": puesto
    }
    
    empleados.append(empleado)


print("\nListado de empleados:")
for emp in empleados:
    print(f"Nombre: {emp['nombre']}, Edad: {emp['edad']}, Puesto: {emp['puesto']}")

empleados = 0
for emp in empleados:
    if emp ['empleados'] >30:
        empleados +=1