# 1. Crear la matriz de 3x3 llamada "teclado"
teclado = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 2. Imprimir la matriz completa para verificarla
print("Matriz original:")
for fila in teclado:
    print(fila)

# 3. Mostrar números específicos usando índices
print("\nNúmero en el centro:", teclado[1][1])             # Fila 1, Columna 1 → 5
print("Número en la esquina inferior derecha:", teclado[2][2])  # Fila 2, Columna 2 → 9

# 4. Modificar el número en la esquina superior izquierda (1 → 0)
teclado[0][0] = 0  # Fila 0, Columna 0

# 5. Imprimir la matriz nuevamente para ver el cambio
print("\nMatriz después de modificar la esquina superior izquierda:")
for fila in teclado:
    print(fila)
