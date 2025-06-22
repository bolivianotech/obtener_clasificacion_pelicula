# Función 1: Crear la sala llena de 'L' (libres)
def crear_sala(filas, columnas):
    return [['L' for _ in range(columnas)] for _ in range(filas)]

# Función 2: Mostrar visualmente la sala
def mostrar_sala(sala):
    print("   " + " ".join(f"{i}" for i in range(len(sala[0]))))  # Números de columna
    for i, fila in enumerate(sala):
        print(f"{i:2} " + " ".join(fila))

# Función 3: Ocupar un asiento
def ocupar_asiento(sala, fila, columna):
    filas = len(sala)
    columnas = len(sala[0])

    # Verifica si coordenadas son válidas
    if 0 <= fila < filas and 0 <= columna < columnas:
        if sala[fila][columna] == 'L':
            sala[fila][columna] = 'O'
            print(f"Asiento ({fila}, {columna}) ocupado exitosamente.")
            return True
        else:
            print("Ese asiento ya está ocupado.")
            return False
    else:
        print("Coordenadas fuera de rango.")
        return False

# Función 4 (Opcional): Contar asientos libres
def contar_asientos_libres(sala):
    return sum(fila.count('L') for fila in sala)

# Programa Principal
def main():
    filas, columnas = 5, 8  # Tamaño predeterminado
    sala = crear_sala(filas, columnas)

    while True:
        print("\n📽️  Estado actual de la sala de cine:")
        mostrar_sala(sala)
        print(f"Asientos libres: {contar_asientos_libres(sala)}")
        print("\nMenú:")
        print("1. Ocupar asiento")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            try:
                fila = int(input("Ingresa el número de fila: "))
                columna = int(input("Ingresa el número de columna: "))
                ocupar_asiento(sala, fila, columna)
            except ValueError:
                print("❌ Entrada inválida. Por favor ingresa números.")
        elif opcion == '0':
            print("🎬 Gracias por usar el sistema de reserva. ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida. Intenta nuevamente.")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
