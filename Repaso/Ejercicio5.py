Años_de_Experiencia = int(input("Ingrese sus años de experiencia: "))
sueldo_base = float(input("Ingrese su sueldo base: "))
if Años_de_Experiencia >=10: 
    bono = sueldo_base * 0.20
elif 5 <= Años_de_Experiencia < 10:
    bono = sueldo_base * 0.10
else: 
    bono = 0
sueldo_total = sueldo_base + bono
print(f" Bono asignado: Q", bono)
print(f"Sueldo total : Q", sueldo_total)