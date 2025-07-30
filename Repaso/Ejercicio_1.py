Name = input ("Ingrese su nombre: ")
Age = int(input("Ingrese su edad: "))
height = float(input("Ingrese su altura en metros:"))
weigth = float(input("Ingrese su peso en kg: "))
#meses vividos
meses_vividos = Age * 12
print(f"{Name}, has vivido {meses_vividos} meses")
height = height * 100  
imc = weigth / (height ** 2)
print(f"Hola tienes {Age}, has vivido aproximadamente {meses_vividos} meses y mides {height} cm ")
print(f"Hola{Name}, tienes {Age}")
print(f"pesas {weigth} kg y mides {height} cm")
print(f"Tu indice de mas corporal es {imc}")