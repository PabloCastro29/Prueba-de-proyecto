Alumno = {}
Alumno["Name"] = input("Ingrese el nombre del alumno: ")
Alumno["Edad"] = int(input("Ingrese la edad del alumno: "))
Alumno["Carrera"] = input("Ingrese la carrera del alumno: ")
print("Esta es la informacion del alumno:  ")
for valor, clave in Alumno.items():
    print(f"{valor}: {clave}")
