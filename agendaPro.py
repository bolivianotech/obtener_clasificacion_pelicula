import json
import os

"""
Programa Agenda de Contactos en Python con persistencia
-------------------------------------------------------
Se guarda la agenda en un archivo JSON para mantener los contactos
entre ejecuciones.
"""

agenda = {}

ARCHIVO = "agenda.json"

def cargar_agenda():
    """Carga la agenda desde un archivo JSON si existe."""
    global agenda
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, 'r', encoding='utf-8') as f:
            agenda = json.load(f)
        print(f"✅ Agenda cargada desde '{ARCHIVO}'.\n")
    else:
        agenda = {}
        print("⚠️ No se encontró archivo de agenda, comenzando vacía.\n")

def guardar_agenda():
    """Guarda la agenda en un archivo JSON."""
    with open(ARCHIVO, 'w', encoding='utf-8') as f:
        json.dump(agenda, f, indent=4, ensure_ascii=False)
    print(f"✅ Agenda guardada en '{ARCHIVO}'.")

def agregar_contacto():
    nombre = input("Ingrese nombre completo: ").strip()
    if nombre in agenda:
        print(f"⚠️ El contacto '{nombre}' ya existe.")
        return

    telefonos = []
    print("Ingrese números de teléfono (deje vacío para terminar):")
    while True:
        telefono = input("Número: ").strip()
        if telefono == '':
            break
        telefonos.append(telefono)

    email = input("Ingrese email: ").strip()

    agenda[nombre] = {
        'telefonos': telefonos,
        'email': email
    }
    print(f"✅ Contacto '{nombre}' agregado correctamente.\n")

def buscar_por_nombre():
    nombre = input("Ingrese nombre a buscar: ").strip()
    contacto = agenda.get(nombre)
    if contacto:
        print_contacto(nombre, contacto)
    else:
        print(f"❌ No se encontró el contacto '{nombre}'.\n")

def editar_contacto():
    nombre = input("Ingrese nombre del contacto a editar: ").strip()
    if nombre not in agenda:
        print(f"❌ El contacto '{nombre}' no existe.\n")
        return

    contacto = agenda[nombre]
    print("Datos actuales:")
    print_contacto(nombre, contacto)

    print("\nEditar teléfonos:")
    print("Teléfonos actuales:")
    for i, t in enumerate(contacto['telefonos'], start=1):
        print(f"{i}. {t}")
    print("Ingrese nuevos números (deje vacío para no cambiar):")
    nuevos_telefonos = []
    while True:
        t = input("Número: ").strip()
        if t == '':
            break
        nuevos_telefonos.append(t)
    if nuevos_telefonos:
        contacto['telefonos'] = nuevos_telefonos

    nuevo_email = input(f"Email actual: {contacto['email']} | Nuevo email (enter para no cambiar): ").strip()
    if nuevo_email:
        contacto['email'] = nuevo_email

    print(f"\n✅ Contacto '{nombre}' actualizado.\n")

def eliminar_contacto():
    nombre = input("Ingrese nombre del contacto a eliminar: ").strip()
    if nombre in agenda:
        del agenda[nombre]
        print(f"✅ Contacto '{nombre}' eliminado.\n")
    else:
        print(f"❌ El contacto '{nombre}' no existe.\n")

def mostrar_todos():
    if not agenda:
        print("📭 La agenda está vacía.\n")
        return

    print("📋 Lista de contactos:")
    for nombre, contacto in agenda.items():
        print_contacto(nombre, contacto)
        print("-" * 30)
    print()

def print_contacto(nombre, contacto):
    print(f"Nombre: {nombre}")
    print(f"Teléfonos: {', '.join(contacto['telefonos']) if contacto['telefonos'] else 'No tiene'}")
    print(f"Email: {contacto['email']}")

def menu():
    cargar_agenda()
    while True:
        print("=== Agenda de Contactos ===")
        print("1. Agregar contacto")
        print("2. Buscar contacto por nombre")
        print("3. Editar contacto")
        print("4. Eliminar contacto")
        print("5. Mostrar todos los contactos")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ").strip()

        if opcion == '1':
            agregar_contacto()
        elif opcion == '2':
            buscar_por_nombre()
        elif opcion == '3':
            editar_contacto()
        elif opcion == '4':
            eliminar_contacto()
        elif opcion == '5':
            mostrar_todos()
        elif opcion == '6':
            guardar_agenda()
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida. Intente de nuevo.\n")

if __name__ == "__main__":
    menu()
