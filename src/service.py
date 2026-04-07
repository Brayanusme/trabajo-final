from validate import validar_registro
import file

# Estructuras de datos en memoria (se cargan inicializando con el archivo)
registros = file.load_data()
ids_usados = {r['id'] for r in registros}
emails_usados = {r['email'] for r in registros}

def crear_registro(id, nombre, email, edad):
    registro = {
        "id": id,
        "nombre": nombre,
        "email": email,
        "edad": edad
    }

    # Validar campos
    errores = validar_registro(registro)
    if errores:
        print("No se pudo crear el registro:")
        for error in errores:
            print(" -", error)
        return

    # Verificar ID único con el set
    if id in ids_usados:
        print(f"Error: el ID '{id}' ya existe")
        return

    # Verificar email único con el set
    if email in emails_usados:
        print(f"Error: el email '{email}' ya está registrado")
        return

    # Guardar en memoria
    registros.append(registro)
    ids_usados.add(id)
    emails_usados.add(email)
    
    # Persistir realmente los datos guardándolos en nuestro JSON
    file.save_data(registros)
    print(f"✔ Creado y guardado en archivo: {nombre}")

def listar_registros():
    if len(registros) == 0:
        print("No hay registros almacenados.")
        return
    print(f"\nTotal de registros: {len(registros)}")
    print("-" * 40)
    for r in registros:
        print(f"ID: {r['id']} | Nombre: {r['nombre']} | Email: {r['email']} | Edad: {r['edad']}")
    print("-" * 40)