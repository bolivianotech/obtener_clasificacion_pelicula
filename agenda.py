# Diccionario principal donde las claves son nombres y los valores son diccionarios con info del contacto
agenda = {}

def agregar_contacto(nombre, telefonos, email):
    """
    Agrega un nuevo contacto a la agenda.
    telefonos: lista de números (puede tener uno o más).
    """
    if nombre in agenda:
        print(f"El contacto '{nombre}' ya existe.")
        return
    agenda[nombre] = {
        'telefonos': telefonos,
        'email': email
    }
    print(f"Contacto '{nombre}' agregado.")

def buscar_por_nombre(nombre):
    """
    Busca y devuelve la información del contacto por nombre.
    """
    return agenda.get(nombre, None)

def editar_contacto(nombre, telefonos=None, email=None):
    """
    Edita los datos de un contacto existente.
    Solo actualiza los campos que se pasen.
    """
    if nombre not in agenda:
        print(f"El contacto '{nombre}' no existe.")
        return
    if telefonos is not None:
        agenda[nombre]['telefonos'] = telefonos
    if email is not None:
        agenda[nombre]['email'] = email
    print(f"Contacto '{nombre}' actualizado.")

def mostrar_contacto(nombre):
    contacto = buscar_por_nombre(nombre)
    if contacto:
        print(f"Nombre: {nombre}")
        print(f"Teléfonos: {', '.join(contacto['telefonos'])}")
        print(f"Email: {contacto['email']}")
    else:
        print(f"No se encontró el contacto '{nombre}'.")

# Ejemplo de uso:
agregar_contacto('Juan Pérez', ['555-1234', '555-5678'], 'juan@example.com')
mostrar_contacto('Juan Pérez')

editar_contacto('Juan Pérez', email='juanperez@nuevoemail.com')
mostrar_contacto('Juan Pérez')
