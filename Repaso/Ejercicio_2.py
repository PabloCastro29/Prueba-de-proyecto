Name = input("Ingrese su nombre :")
Kilometros = float(input("Ingrese la cantidad de kilometros que va a correrr: "))
price = float(input("iNGRESE LA CANTIDAD DE DINERO QUE TIENE: "))
Total_Cost = Kilometros * price
Money = float(input("Ingrese la cantidad de dinero que tiene disponible en dolares:  "))
dinero_sobrante = Money - Total_Cost
print(f"{Name}, el costo total de los kilometros recorridos es {Total_Cost} y te sobrara {dinero_sobrante} despues de pagar")