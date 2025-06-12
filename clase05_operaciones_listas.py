# clase05_operaciones_listas.py
# Ejercicio 1: Función p
def sumar_elementos(lista_numeros):
    """
    Función que recibe una lista de números y retorna la suma total de los elementos.
    Parámetro:
        lista_numeros: Lista de números a sumar
    Retorna:
        La suma total de todos los elementos de la lista (puede ser un número negativo)     """
    # Implementa el algoritmo que diseñamos:
    # Crea una variable acumulador_suma inicializada en 0
    acumulador_suma = 0
    # Usa un bucle for para recorrer lista_numeros
    for elemento_actual in lista_numeros:
        # En cada iteración, acumulador_suma += elemento_actual
        acumulador_suma += elemento_actual
    # Al final, return acumulador_suma
    return acumulador_suma
# Casos de Prueba con assert
print("Probando sumar_elementos...")
assert sumar_elementos([1, 2, 3, 4, 5]) == 15
assert sumar_elementos([10, -2, 5]) == 13
assert sumar_elementos([]) == 0  # ¡Importante probar con una lista vacía!
assert sumar_elementos([100]) == 100
print("¡Pruebas para sumar_elementos pasaron! ✅")
# Pruebas adicionales para verificar que funciona correctamente
print("\n--- Pruebas adicionales ---")
print(f"Suma de [1, 2, 3, 4, 5]: {sumar_elementos([1, 2, 3, 4, 5])}")
print(f"Suma de [10, -2, 5]: {sumar_elementos([10, -2, 5])}")
print(f"Suma de lista vacía []: {sumar_elementos([])}")
print(f"Suma de [100]: {sumar_elementos([100])}")
print(f"Suma de [-1, -2, -3]: {sumar_elementos([-1, -2, -3])}")
print(f"Suma de [0, 0, 0, 0]: {sumar_elementos([0, 0, 0, 0])}")
print("JIMMY REQUENA - FIN DEL PROGRAMA")