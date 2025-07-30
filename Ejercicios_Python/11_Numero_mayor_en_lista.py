def mayor(Numbers_list):
    maximo = Numbers_list[0]
    for numero in Numbers_list:
        if numero > maximo:
            maximo = numero
    return maximo

numeros = [3, 8, 2, 45, 22]
print("El número mayor es:", mayor(numeros))
