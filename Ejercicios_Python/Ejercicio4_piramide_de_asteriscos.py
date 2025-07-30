leves = int(input("Ingrese el numero de niveles de la piramide:"))

for level in range( 1, leves +1):
    spaces = " " * (leves - level)
    asterisks = "*" * (2 * level - 1)
    print(spaces + asterisks + spaces)