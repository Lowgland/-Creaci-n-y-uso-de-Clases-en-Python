class InventarioTienda:
    def __init__(self, nombre_Tienda):
        self.nombre_Tienda=nombre_Tienda
        self.productos=[] #Esto hace que la lista empiece vacia

    def agregar_Producto(self, nombre, precio, cantidad):
        if cantidad <= 0:
            print("La cantidad tiene que ser positiva")
            return
        if precio <= 0:
            print("El precio tiene que ser mayor a cero")
            return
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad,
        }
        self.productos.append(producto)
        print(f"Producto: {nombre} fue agregado")

    def vender_Producto(self, nombre, cantidad):
        if cantidad <= 0:
            print("La cantidad que se va a vender tiene que ser positiva")
            return
        for c in self.productos:
            if c["nombre"].lower() == nombre.lower():
                if c["cantidad"] >= cantidad:
                    c["cantidad"] -= cantidad
                    print(f"El producto: {nombre} fue vendido por {cantidad}")
                else:
                    print("No hay stock suficiente")
                return
        print("El producto no existe")

    def mostrar_Inventario(self):
        if not self.productos:
            print("No hay productos en el inventario")
        else:
            print("\n Inventario de productos")
            for c in self.productos:
                print(f"{c['nombre']} // Precio: {c['precio']} // Cantidad: {c['cantidad']}")

    def producto_Mas_Caro(self):
        if not self.productos:
            print("No hay productos en el inventario")
            return
        producto_caro = None
        precio_max = -1
        for c in self.productos:
            if c["precio"] > precio_max:
                precio_max = c["precio"]
                producto_caro = c["nombre"]
        print(f"El producto más caro es '{producto_caro}' con precio de {precio_max} pesos")

def main():
    inventario=InventarioTienda("Mi tienda")
    while True:
        print("\n Menú")
        print("1.- Agregar producto")
        print("2.- Vender producto")
        print("3.- Mostrar inventario")
        print("4.- Consultar producto más caro")
        print("5.- Salir")
        opcion = input("Selecciona una opción: (Solo el número) ")
        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad del producto: "))
            inventario.agregar_Producto(nombre, precio, cantidad)
        elif opcion == "2":
            nombre = input("Nombre del producto que se va a vender: ")
            cantidad = int(input("Cantidad del producto que se va a vender: "))
            inventario.vender_Producto(nombre, cantidad)
        elif opcion == "3":
            inventario.mostrar_Inventario()
        elif opcion == "4":
            inventario.producto_Mas_Caro()
        elif opcion == "5":
            print("Saliendo del programa")
            break
        else:
            print("Opción no válida, intenta otra vez")
if __name__ == "__main__": #Esto hace que si corra el programa, a veces cuando no estaba no lo podia correr
    main()