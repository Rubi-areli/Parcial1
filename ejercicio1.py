#Una tienda local vende diversos productos, cada vez que un cliente
#hace una compra niña mary se encarga de anotarlo en una libreta. A su
#vez, con una calculadora le da el total a cada cliente y les da su
#respectivo vuelto en caso de necesitarlo.
#Niña mary también se encarga de atender a los proveedores que
#le dan cierta cantidad de producto y un precio sugerido de venta,
#propón una solución dentro de tu programa para ayudarle



class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Venta:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto, cantidad):
        self.productos.append((producto, cantidad))

    def calcular_total(self):
        total = sum(producto.precio * cantidad for producto, cantidad in self.productos)
        return total

class Proveedor:
    def __init__(self, nombre, producto, precio_sugerido):
        self.nombre = nombre
        self.producto = producto
        self.precio_sugerido = precio_sugerido

def mostrar_productos_disponibles(productos):
    print("Productos disponibles:")
    for idx, producto in enumerate(productos, 1):
        print(f"{idx}. {producto.nombre} - ${producto.precio:.2f}")

# Lista de productos disponibles
productos_disponibles = [
    Producto("Arroz", 1.5),
    Producto("Frijol", 2.0),
    Producto("Azúcar", 1.8),
    Producto("Aceite", 3.5),
    Producto("leche",3.0)
]

# Crear una nueva venta
venta = Venta()

# Mostrar productos disponibles
mostrar_productos_disponibles(productos_disponibles)

# Ingresar productos a la venta
while True:
    seleccion = input("Seleccione el número del producto que desea comprar (o 'q' para terminar): ")
    if seleccion.lower() == 'q':
        break

    try:
        seleccion = int(seleccion)
        if 1 <= seleccion <= len(productos_disponibles):
            producto_seleccionado = productos_disponibles[seleccion - 1]
            cantidad = int(input(f"Ingrese la cantidad de {producto_seleccionado.nombre} que desea: "))
            venta.agregar_producto(producto_seleccionado, cantidad)
        else:
            print("Selección no válida. Por favor, seleccione un número válido de la lista.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")

# Calcular y mostrar el total
total = venta.calcular_total()
print(f"Total a pagar: ${total:.2f}")

# Ingresar el monto pagado por el cliente
monto_pagado = float(input("Ingrese el monto con el que paga el cliente: "))

# Calcular vuelto o verificar si es insuficiente
if monto_pagado >= total:
    vuelto = monto_pagado - total
    print(f"El cliente ha pagado ${monto_pagado:.2f}. Vuelto: ${vuelto:.2f}")
else:
    print(f"El monto pagado es insuficiente. Faltan ${total - monto_pagado:.2f} para completar la compra.")
