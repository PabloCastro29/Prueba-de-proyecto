def numero_primo(number):
    if number < 2: 
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
        return True
valor = int(input("INGRESE EL NUMERO:"))
if numero_primo(valor):
    print(valor, "Es primo")
else: 
    print(valor, "No es")


    #While cuando se manejan menus y un for cuando se manejan iteraciones
    