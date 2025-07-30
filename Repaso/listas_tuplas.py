edades = [20,15,15,130]
print(edades.count(15))
print(edades.index(130))

#Imprimir elementos de una lista
frutas = ["manzana", "pera", "uva"] 
for fruta in frutas:
    print(fruta)    

#Imprimir con mensaje
nombres = ["Juan", "Ana", "Pedro"]
for nombre in nombres:
    print(f"Hola, {nombre}!")

#suma de los valores de una lista
numeros = [1, 2, 3, 4, 5]
suma = 0
for numero in numeros:
    suma += numero
print(f"La suma de los números es: {suma}")

#Recorrer con el rango (en la lista, acceso por indice, se quiere saber la posición, del indice)
Colores = ["rojo", "verde", "azul"]
for i in range(len(Colores)):
    print(f"Color en la posición {i}: {Colores[i]}")