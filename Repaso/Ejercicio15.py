Agenda = {}
for i in range(3):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    telefono = input(f"Ingrese el telefono de {nombre}: ")
    Agenda[nombre] = telefono
consulta = input("Ingrese el nombre del contacto a consultar: ")
if consulta in Agenda:
    print(f"Telefono de {consulta}: {Agenda[consulta]}")
else:
    print(f"No se encontro el contacto {consulta} en la agenda.")