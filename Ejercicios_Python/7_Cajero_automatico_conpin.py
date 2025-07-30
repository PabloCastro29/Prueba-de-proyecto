pin = 13243
Attempts_made = 0

while Attempts_made < 3:
    ingresed_pin = int(input("Ingrese el pin:"))
    if ingresed_pin == pin:
        print("pin correcto")
        break
    else:
        print("Pin Incorrecto")
        Attempts_made +=1
if Attempts_made == 3: 
    print("Cuenta bloqueada")

    