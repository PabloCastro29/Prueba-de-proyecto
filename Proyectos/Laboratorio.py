#Declare los nombres con una lista
Lista = ["Ana", "Pedro", "Juan"]

#Como se elimina un elemento de la lista
Lista = ["Ana", "Pedro", "Juan"]
list.remove("Pedro")
print(Lista)

#Que hace el siguiente codigo
while True:
 print("Hola")
 break

#Declarar un diccionario con nombre edad y carrera
diccionario = {
    "nombre": "Ana",
    "edad": 25,
    "carrera": "Ingeniería"
}


#Diferencia entre lista y tupla
#Una lista es mutable y una tupla es inmutable. "

#Practica 2
#Escribir un ciclo while que pida números hasta que el usuario ingrese 0. Muestra la suma total.
suma_total = 0
while True: 
    numero = int(input("Ingrese un número (0 para salir): "))
    if numero == 0:
        break
    suma_total += numero

#Dada la lista numeros = [10, 20, 30, 40], recórrela con un for y muestrar cada número multiplicado por 2
numeros = [10, 20, 30, 40]
for numero in numeros:      
    print(numero * 2)

#Crea un diccionario llamado producto con las claves: nombre, precio, stock.
#Ingresar tres productos e imprimirlos con este formato
#El producto [nombre] cuesta Q[precio] y hay [stock] unidades disponibles
producto = {}
for i in range(3):
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese el stock del producto: "))
    
    producto[nombre] = {
        "precio": precio,
        "stock": stock
    }
for nombre, detalles in producto.items():
    print(f"El producto {nombre} cuesta Q{detalles['precio']} y hay {detalles['stock']} unidades disponibles")