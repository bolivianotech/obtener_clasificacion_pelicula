# Ejercicio: Verificador de Edad para Películas usando Funciones
# Versión completa con documentación detallada y pruebas con asserts

def obtener_clasificacion_pelicula(edad_persona):
    """
    Determina qué tipo de películas puede ver una persona según su edad.

    Esta función evalúa la edad de una persona y devuelve un mensaje
    indicando qué clasificaciones de películas puede ver según las
    normas estándar de la industria cinematográfica.

    Args:
        edad_persona (int): La edad de la persona en años. 
                           Debe ser un número entero positivo.

    Returns:
        str: Un mensaje que indica la clasificación de películas
             que la persona puede ver según su edad:
             - Para menores de 13: películas G o PG
             - Para 13-17 años: películas PG-13
             - Para 18 años o más: películas R
             - Para edades inválidas: mensaje de error

    Examples:
        >>> obtener_clasificacion_pelicula(10)
        'Te recomendamos películas clasificadas G o PG.'

        >>> obtener_clasificacion_pelicula(15)
        'Puedes ver películas clasificadas PG-13.'

        >>> obtener_clasificacion_pelicula(20)
        '¡Puedes ver películas clasificadas R!'

    Note:
        Esta función NO utiliza input() ni print() para ser reutilizable.
        Solo procesa datos y retorna resultados.
    """

    # Validación: Verificar que la edad esté en un rango válido
    if edad_persona < 0 or edad_persona > 120:
        return "Edad no válida."

    # Clasificación para niños (menores de 13 años)
    if edad_persona < 13:
        return "Te recomendamos películas clasificadas G o PG."

    # Clasificación para adolescentes (13 a 17 años)
    elif edad_persona < 18:
        return "Puedes ver películas clasificadas PG-13."

    # Clasificación para adultos (18 años o más)
    else:  # edad_persona >= 18
        return "¡Puedes ver películas clasificadas R!"


# =============================================================================
# SECCIÓN DE PRUEBAS CON ASSERTS
# =============================================================================
# ¡IMPORTANTE! Las pruebas van DESPUÉS de definir la función
# pero ANTES del programa principal que interactúa con el usuario

def ejecutar_pruebas():
    """
    Ejecuta todas las pruebas unitarias para verificar que la función
    obtener_clasificacion_pelicula() funciona correctamente.

    Utiliza asserts para validar diferentes casos de prueba:
    - Casos límite (edades en los bordes de cada clasificación)
    - Casos normales (edades típicas en cada rango)
    - Casos de error (edades inválidas)

    Raises:
        AssertionError: Si alguna prueba falla, se detiene la ejecución
                       y muestra qué prueba específica falló.
    """

    print("🧪 Ejecutando pruebas de la función obtener_clasificacion_pelicula()...")
    print("=" * 60)

    # PRUEBAS PARA ADULTOS (18 años o más)
    # Caso normal: adulto joven
    assert obtener_clasificacion_pelicula(20) == "¡Puedes ver películas clasificadas R!", \
        "Prueba fallida: Adulto de 20 años"
    print("✅ Prueba 1 PASADA: Adulto de 20 años")

    # Caso límite: exactamente 18 años (límite inferior de adultos)
    assert obtener_clasificacion_pelicula(18) == "¡Puedes ver películas clasificadas R!", \
        "Prueba fallida: Límite Adulto (18 años)"
    print("✅ Prueba 2 PASADA: Límite adulto (18 años)")

    # Caso normal: adulto mayor
    assert obtener_clasificacion_pelicula(65) == "¡Puedes ver películas clasificadas R!", \
        "Prueba fallida: Adulto mayor"
    print("✅ Prueba 3 PASADA: Adulto mayor de 65 años")

    # PRUEBAS PARA ADOLESCENTES (13-17 años)
    # Caso normal: adolescente típico
    assert obtener_clasificacion_pelicula(15) == "Puedes ver películas clasificadas PG-13.", \
        "Prueba fallida: Adolescente de 15 años"
    print("✅ Prueba 4 PASADA: Adolescente de 15 años")

    # Caso límite: exactamente 13 años (límite inferior de adolescentes)
    assert obtener_clasificacion_pelicula(13) == "Puedes ver películas clasificadas PG-13.", \
        "Prueba fallida: Límite Adolescente (13 años)"
    print("✅ Prueba 5 PASADA: Límite adolescente (13 años)")

    # Caso límite: 17 años (límite superior de adolescentes)
    assert obtener_clasificacion_pelicula(17) == "Puedes ver películas clasificadas PG-13.", \
        "Prueba fallida: Adolescente de 17 años"
    print("✅ Prueba 6 PASADA: Adolescente de 17 años")

    # PRUEBAS PARA NIÑOS (menores de 13 años)
    # Caso normal: niño típico
    assert obtener_clasificacion_pelicula(10) == "Te recomendamos películas clasificadas G o PG.", \
        "Prueba fallida: Niño de 10 años"
    print("✅ Prueba 7 PASADA: Niño de 10 años")

    # Caso límite: niño muy pequeño
    assert obtener_clasificacion_pelicula(5) == "Te recomendamos películas clasificadas G o PG.", \
        "Prueba fallida: Niño de 5 años"
    print("✅ Prueba 8 PASADA: Niño de 5 años")

    # Caso límite: 12 años (límite superior de niños)
    assert obtener_clasificacion_pelicula(12) == "Te recomendamos películas clasificadas G o PG.", \
        "Prueba fallida: Niño de 12 años"
    print("✅ Prueba 9 PASADA: Niño de 12 años")

    # PRUEBAS PARA CASOS DE ERROR (edades inválidas)
    # Edad negativa
    assert obtener_clasificacion_pelicula(-5) == "Edad no válida.", \
        "Prueba fallida: Edad negativa"
    print("✅ Prueba 10 PASADA: Edad negativa (-5)")

    # Edad excesivamente alta
    assert obtener_clasificacion_pelicula(150) == "Edad no válida.", \
        "Prueba fallida: Edad excesivamente alta"
    print("✅ Prueba 11 PASADA: Edad excesivamente alta (150)")

    # Caso límite: edad 0
    assert obtener_clasificacion_pelicula(0) == "Te recomendamos películas clasificadas G o PG.", \
        "Prueba fallida: Edad 0 años"
    print("✅ Prueba 12 PASADA: Bebé de 0 años")

    print("=" * 60)
    print("🎉 ¡TODAS LAS PRUEBAS PASARON EXITOSAMENTE!")
    print("🛡️  Nuestra función es robusta y maneja todos los casos correctamente.")
    print()


def obtener_edad_usuario():
    """
    Solicita la edad al usuario y valida que sea un número entero válido.

    Maneja errores de entrada del usuario (como letras en lugar de números)
    y sigue pidiendo la edad hasta que se ingrese un valor válido.

    Returns:
        int: La edad ingresada por el usuario (número entero válido)

    Note:
        Esta función utiliza un bucle while para seguir pidiendo
        la edad hasta que el usuario ingrese un número válido.
    """

    while True:  # Bucle infinito hasta obtener entrada válida
        try:
            # Intentar convertir la entrada del usuario a entero
            edad = int(input("Por favor, ingresa tu edad: "))
            return edad  # Si la conversión es exitosa, retornar la edad

        except ValueError:
            # Si el usuario ingresó algo que no es un número
            print("❌ Error: Debes ingresar un número entero válido.")
            print("   Ejemplos válidos: 15, 25, 30")
            print("   Ejemplos inválidos: 'quince', '25.5', 'abc'")
            print()


def mostrar_resultado(edad, mensaje):
    """
    Muestra el resultado de la clasificación de película de manera formateada.

    Args:
        edad (int): La edad de la persona
        mensaje (str): El mensaje de clasificación devuelto por la función

    Note:
        Esta función se encarga únicamente de la presentación visual
        del resultado, separando la lógica de negocio de la presentación.
    """

    print("\n" + "=" * 50)
    print("🎬 RESULTADO DE CLASIFICACIÓN DE PELÍCULAS")
    print("=" * 50)
    print(f"👤 Edad ingresada: {edad} años")
    print(f"🎭 Clasificación: {mensaje}")
    print("=" * 50)


def main():
    """
    Función principal del programa que coordina toda la ejecución.

    Esta función:
    1. Muestra el título del programa
    2. Ejecuta las pruebas para verificar que todo funciona
    3. Solicita la edad al usuario
    4. Llama a la función de clasificación
    5. Muestra el resultado

    Note:
        Separa claramente las responsabilidades: pruebas, entrada de datos,
        procesamiento y salida de datos.
    """

    # Mostrar título del programa
    print("🎬" * 20)
    print("    VERIFICADOR DE EDAD PARA PELÍCULAS")
    print("🎬" * 20)
    print()

    # Ejecutar pruebas primero para asegurar que todo funciona
    ejecutar_pruebas()

    # Programa principal de interacción con el usuario
    print("📝 Ahora vamos a verificar TU edad para películas...")
    print()

    # Obtener edad del usuario con validación
    edad_ingresada = obtener_edad_usuario()

    # Llamar a nuestra función principal para obtener la clasificación
    mensaje_cine = obtener_clasificacion_pelicula(edad_ingresada)

    # Mostrar el resultado de manera formateada
    mostrar_resultado(edad_ingresada, mensaje_cine)

    # Mensaje de despedida
    print("\n🎭 ¡Gracias por usar nuestro verificador de edad!")
    print("   ¡Disfruta de tus películas! 🍿")


# =============================================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# =============================================================================
# Esta sección se ejecuta solo cuando el archivo se ejecuta directamente
# (no cuando se importa como módulo en otro archivo)

if __name__ == "__main__":
    """
    Punto de entrada principal del programa.

    El uso de 'if __name__ == "__main__":' es una buena práctica que
    permite que este código se ejecute solo cuando el archivo se ejecuta
    directamente, pero no cuando se importa desde otro archivo.
    """

    # Ejecutar el programa principal
    main()