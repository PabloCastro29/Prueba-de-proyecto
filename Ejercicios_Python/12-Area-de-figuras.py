import math

def area_circulo(radio):
    return math.pi * radio ** 2

def area_cuadrado(lado):
    return lado ** 2

def area_triangulo(base, altura):
    return (base * altura) / 2

figura = input("Elija figura (circulo, cuadrado, triangulo): ")

if figura == "circulo":
    radio = float(input("Ingrese el radio: "))
    print("Área del círculo:", area_circulo(radio))
elif figura == "cuadrado":
    lado = float(input("Ingrese el lado: "))
    print("Área del cuadrado:", area_cuadrado(lado))
elif figura == "triangulo":
    base = float(input("Ingrese la base: "))
    altura = float(input("Ingrese la altura: "))
    print("Área del triángulo:", area_triangulo(base, altura))
else:
    print("Opción no válida.")