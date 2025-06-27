# Tu programa debió ser algo similar por favor ejecuta este código y 
# compara la salida y sube ambas verciones a tu repositorio como 
# evidencia de tu respuesta.
class CarritoDeCompras:
    """
    Representa un carrito de compras que puede contener productos y calcular el total.
    """
    def __init__(self):
        """
        Inicializa un nuevo carrito de compras vacío. [cite: 912]
        """
        self.productos = []

    def agregar_producto(self, producto):
        """
        Añade un producto (un diccionario) al carrito. [cite: 912]
        """
        self.productos.append(producto)
        print(f"Producto '{producto['nombre']}' agregado al carrito.")

    def calcular_total(self):
        """
        Calcula la suma de los precios de todos los productos en el carrito. [cite: 912]
        """
        total = 0
        for producto in self.productos:
            total += producto['precio']
        return total

    def mostrar_carrito(self):
        """
        Muestra el contenido del carrito y el precio total. [cite: 912]
        """
        print("\n--- Carrito de Compras ---")
        if not self.productos:
            print("El carrito está vacío.")
        else:
            for producto in self.productos:
                print(f"- {producto['nombre']}: ${producto['precio']:.2f}")

        total_a_pagar = self.calcular_total()
        print(f"--------------------------")
        print(f"Total a pagar: ${total_a_pagar:.2f}")

# Ejemplo de uso:
mi_carrito = CarritoDeCompras()
mi_carrito.mostrar_carrito() # Muestra carrito vacío

# Creamos y agregamos productos
producto1 = {"nombre": "Café Orgánico", "precio": 35.50}
producto2 = {"nombre": "Tableta de Chocolate", "precio": 12.75}
mi_carrito.agregar_producto(producto1)
mi_carrito.agregar_producto(producto2)

# Mostramos el carrito final
mi_carrito.mostrar_carrito()


#RESPUESTA ESPERADO EN CONSOLA:
#--- Carrito de Compras ---
#El carrito está vacío.
#--------------------------
#Total a pagar: $0.00
#Producto 'Café Orgánico' agregado al carrito.
#Producto 'Tableta de Chocolate' agregado al carrito.
#
#--- Carrito de Compras ---
#- Café Orgánico: $35.50
#- Tableta de Chocolate: $12.75
#--------------------------
#Total a pagar: $48.25