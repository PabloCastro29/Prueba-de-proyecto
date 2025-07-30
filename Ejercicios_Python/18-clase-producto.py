class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def aplicar_descuento(self, porcentaje):
        descuento = self.precio * (porcentaje / 100)
        self.precio -= descuento

producto1 = Producto("Camisa", 100, 20)
producto1.aplicar_descuento(10)
print("Precio con descuento:", producto1.precio)
