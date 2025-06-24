producto = {'codigo': 'P001', 'nombre': 'Café', 'precio': 38.0, 'stock': 100}
print("\n--- Claves del producto ---")
for clave in producto: # Por defecto, itera sobre las CLAVES
    print(clave)
print("\n--- Clave y Valor ---")
for clave in producto:
    valor = producto[clave]
    print(f"{clave.capitalize()}: {valor}")
