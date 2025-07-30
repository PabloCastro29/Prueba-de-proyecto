def calcular_descuento(precio, porcentaje):
    if porcentaje > 100 or porcentaje < 0:
        return "Error: porcentaje inválido"

    descuento_aplicado = precio * (porcentaje / 100)
    precio_final = precio - descuento_aplicado
    return precio_final


print(calcular_descuento(100, -5)) 
print(calcular_descuento(200, 20))   
