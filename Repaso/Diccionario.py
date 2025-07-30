persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
print("Edad", persona["edad"])
print(persona["nombre"])
#Agregar nuevo par
persona["Profesion"] = "Ingeniero"
#Modificar valor
persona["edad"] = 3
#Eliminar clave
del persona["ciudad"]
#Mostra claves

print("\nClaves:")

for clave in persona.keys():
    print(clave)

for valor in persona.values():
        print(valor)
#Mostrar todos los pares clave-valor
print("\nDatos de la persona:")

for clave, valor in persona.items():
    print(f"{clave}: {valor}")

