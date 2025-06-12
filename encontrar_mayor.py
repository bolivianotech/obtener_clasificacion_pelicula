def encontrar_mayor(lista_numeros):
  # Caso especial: lista vacía
  if not lista_numeros:
      return None

  # Inicializamos el mayor temporal con el primer elemento
  mayor_temporal = lista_numeros[0]

  # Recorremos el resto de la lista
  for elemento_actual in lista_numeros[1:]:
      if elemento_actual > mayor_temporal:
          mayor_temporal = elemento_actual

  return mayor_temporal

# Pruebas
print("\nProbando encontrar_mayor...")
assert encontrar_mayor([1, 9, 2, 8, 3, 7]) == 9
assert encontrar_mayor([-1, -9, -2, -8]) == -1
assert encontrar_mayor([42, 42, 42]) == 42
assert encontrar_mayor([]) == None  # Prueba del caso especial
assert encontrar_mayor([5]) == 5
print("¡Pruebas para encontrar_mayor pasaron! ✅")
