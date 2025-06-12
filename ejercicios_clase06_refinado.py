# clase06_busquedas.py

# ------------------------------
# Ejercicio 1: Búsqueda Lineal
# ------------------------------
def busqueda_lineal(lista, clave):
    for i in range(len(lista)):
        if lista[i] == clave:
            return i
    return -1

# Pruebas de búsqueda lineal
mi_lista_desordenada = [10, 5, 42, 8, 17, 30, 25]
print("Probando busqueda_lineal...")

assert busqueda_lineal(mi_lista_desordenada, 42) == 2
assert busqueda_lineal(mi_lista_desordenada, 10) == 0  # Al inicio
assert busqueda_lineal(mi_lista_desordenada, 25) == 6  # Al final
assert busqueda_lineal(mi_lista_desordenada, 99) == -1  # No existe
assert busqueda_lineal([], 5) == -1  # Lista vacía

print("¡Pruebas para busqueda_lineal pasaron! ✅")

# ------------------------------
# Ejercicio 2: Búsqueda Binaria
# ------------------------------
def busqueda_binaria(lista_ordenada, clave):
    izquierda = 0
    derecha = len(lista_ordenada) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista_ordenada[medio] == clave:
            return medio
        elif clave > lista_ordenada[medio]:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1

# Pruebas de búsqueda binaria
lista_ordenada = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print("\nProbando busqueda_binaria...")

assert busqueda_binaria(lista_ordenada, 23) == 5
assert busqueda_binaria(lista_ordenada, 91) == 9  # Último
assert busqueda_binaria(lista_ordenada, 2) == 0   # Primero
assert busqueda_binaria(lista_ordenada, 3) == -1  # No existe
assert busqueda_binaria(lista_ordenada, 100) == -1  # Fuera de rango

print("¡Pruebas para busqueda_binaria pasaron! ✅")

# ---------------------------------------------
# Experimento del Caos: Búsqueda binaria mal usada
# ---------------------------------------------
print("\nRealizando el experimento del caos...")

# Volvemos a usar la lista desordenada
mi_lista_desordenada = [10, 5, 42, 8, 17, 30, 25]

# Intentamos usar búsqueda binaria en una lista desordenada
resultado_caos = busqueda_binaria(mi_lista_desordenada, 5)

print(f"Búsqueda binaria de '5' en lista desordenada devolvió: {resultado_caos}")
print("JIMMY REQUENA - FIN DEL PROGRAMA")
# Probablemente devuelva -1 (fallo), o un índice incorrecto

# Conclusión:
# La búsqueda binaria necesita que la lista esté ordenada.
# Si se aplica mal, puede dar resultados incorrectos o engañosos.
