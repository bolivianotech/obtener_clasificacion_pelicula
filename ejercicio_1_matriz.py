# 1. Crear la matriz de 3x3
teclado = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 2. Imprimir la matriz completa
print("Matriz original:")
for fila in teclado:
    print(fila)

# 3. Acceder a elementos específicos
print("\nNúmero en el centro:", teclado[1][1])  # 5
print("Número en la esquina inferior derecha:", teclado[2][2])  # 9

# 4. Modificar el número en la esquina superior izquierda (1 por un 0)
teclado[0][0] = 0

# 5. Imprimir la matriz modificada
print("\nMatriz modificada:")
for fila in teclado:
    print(fila)

# Usamos el teclado modificado del ejercicio anterior
teclado = [
    [0, 8, 9],
    [4, 5, 6],
    [1, 2, 3]
]

print("Matriz como cuadrícula:")
for fila in teclado:
    for elemento in fila:
        print(elemento, end="\t")  # Imprimir sin salto de línea, separado por tabulador
    print()  # Salto de línea al terminar cada fila



# Crear matriz 5x5 con bucles anidados
matriz_ceros = []
for i in range(5):
    fila = []
    for j in range(5):
        fila.append(0)
    matriz_ceros.append(fila)

print("\nMatriz 5x5 llena de ceros (con bucles):")
for fila in matriz_ceros:
    print(fila)
print("\nJIM REQUENA - FIN DEL PROGRAMA DE EJERCICOS DE MATRICES")