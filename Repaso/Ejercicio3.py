Name = input("Ingresa tu nombre: ")
Age  = int(input("Ingresa tu edad: "))
Weight = input("Ingresa tu peso en kilogramos: ")
Height = input("Ingresa tu altura en metros: ")
IMC = float(Weight) / (float(Height) ** 2)

if IMC >= 18.5:
    print(f"{Name}, estas por debajo de tu peso ideal")
elif 18.5 <= IMC <24.9:
    print(f"{Name}, Tienes un peso noraml")
elif 25 <= IMC <29.9:
    print(f"{Name}, Tienes sobrepeso")
else:
    print((f" hola pablo {Name}, tienes {Age} años y mides {Height}, pesas {Weight}, tu IMC es {IMC} y  tienes obesidad "))
