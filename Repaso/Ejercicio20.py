def informe_mayor(a, b):
    def mayor(x, y):
        if x > y:
            return x
        else: 
            return y
    resultado = mayor (a, b)
    return f"El mayor de {a} y {b} es {resultado}" 
print(informe_mayor(10,20))
