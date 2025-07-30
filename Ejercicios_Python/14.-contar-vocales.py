def vocales (texto):
    cantidad_De_vocales = 0
    for caracter in texto.lower():
        if caracter in "aeiou":
            cantidad_De_vocales += 1
    return cantidad_De_vocales
cadena = input("Ingrese el texto:")
print("La cantidad de vocales es:", vocales(cadena))