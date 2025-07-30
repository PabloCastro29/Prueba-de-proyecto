Producto = {
    "Nombres": "Laptop lonovo",
    "Precio": 4500.00,
    "stock" : Disponible
}

print(f"Producto: {Producto['Nombres']}")
print(f"precio: Q{Producto['Precio']}")
print(f"stock disponible:{Producto{"stock"}} Unidades")

#Modificar stock
Producto["stock"] -=1 #Simula una venta

print(f"\n")