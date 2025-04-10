class Producto:
    def __init__(self, nombre, precio, stock):
       
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def verificar_disponibilidad(self, cantidad):
        if self.stock >= cantidad:
            return True
        else:
            return False

    
    def vender(self, cantidad):
        if self.verificar_disponibilidad(cantidad):
            self.stock -= cantidad
            print(f"se vendio un cantidad {cantidad} y unidades de {self.nombre}. Stock disponible: {self.stock}.")
        else:
            print(f"no disponible para vender {cantidad} unidades de {self.nombre}. Stock disponible: {self.stock}.")

 
    def reabastecer(self, cantidad):
        self.stock += cantidad
        print(f"Se han suministrado {cantidad} unidades de {self.nombre}. Stock actual: {self.stock}.")


producto = Producto("Portatil", 1200, 10)


print("Validando la  disponibilidad de 5 unidades:")
if producto.verificar_disponibilidad(5):
    print("Hay disponibilidad stock para 5 unidades.\n")
else:
    print("No hay disponibilidad de stock para 5 unidades.\n")

print("Vendiendo 3 unidades:")
producto.vender(3)

print("Verificando disponibilidad de 8 unidades:")
if producto.verificar_disponibilidad(8):
    print("Hay suficiente stock para 8 unidades.\n")
else:
    print("No hay suficiente stock para 8 unidades.\n")

print("Intentando vender 8 unidades:")
producto.vender(8)

print("Reabasteciendo con 10 unidades:")
producto.reabastecer(10)

print("Verificando disponibilidad de 8 unidades después del reabastecimiento:")
if producto.verificar_disponibilidad(8):
    print("Hay suficiente stock para 8 unidades.\n")
else:
    print("No hay suficiente stock para 8 unidades.\n")

print("Vendiendo 8 unidades:")
producto.vender(8)
