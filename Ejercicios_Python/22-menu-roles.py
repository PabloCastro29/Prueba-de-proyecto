user_role = input("Ingrese su rol (administrador/estudiante): ")

if user_role == "administrador":
    print("1. Ver usuarios\n2. Eliminar usuarios")
elif user_role == "estudiante":
    print("1. Ver notas\n2. Inscribirse en curso")
else:
    print("Rol no válido.")
