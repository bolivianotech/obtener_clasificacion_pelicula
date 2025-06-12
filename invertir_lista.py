def invertir_lista(lista_original):
  # Crear una nueva lista vacía
  lista_invertida = []

  # Recorrer la lista original de atrás hacia adelante
  for i in range(len(lista_original) - 1, -1, -1):
      lista_invertida.append(lista_original[i])

  # Retornar la nueva lista invertida
  return lista_invertida


# Pruebas
print("\nProbando invertir_lista...")

lista_prueba = [1, 2, 3, 4, 5]
lista_resultante = invertir_lista(lista_prueba)

assert lista_resultante == [5, 4, 3, 2, 1]
assert lista_prueba == [1, 2, 3, 4, 5]  # ¡Verifica que la original no cambió!
assert invertir_lista(["a", "b", "c"]) == ["c", "b", "a"]
assert invertir_lista([]) == []

print("¡Pruebas para invertir_lista pasaron! ✅")
