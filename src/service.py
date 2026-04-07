from validate import validar_registro
import file

# Cargar registros iniciales y configurar nuestros sets para control rápido de duplicados
registros = file.load_data()
ids_usados = {r['id'] for r in registros}
emails_usados = {r['email'] for r in registros}

def new_register(id, nombre, email, edad, estado="activo"):
    """
    Crea un nuevo registro y lo persiste en el archivo JSON.
    Incluye manejo de excepciones mediante validaciones previas.
    """
    registro = {
        "id": id,
        "nombre": nombre,
        "email": email,
        "edad": edad,
        "estado": estado
    }

    # Validación de datos (ej: el email no contiene @)
    errores = validar_registro(registro)
    if errores:
        raise ValueError(f"Error de validación al crear: {', '.join(errores)}")

    # Revisar colisiones
    if id in ids_usados:
        raise ValueError(f"Error: el ID '{id}' ya existe.")

    if email in emails_usados:
        raise ValueError(f"Error: el email '{email}' ya está registrado.")

    registros.append(registro)
    ids_usados.add(id)
    emails_usados.add(email)
    
    file.save_data(registros)
    print(f"[OK] Creado y guardado con éxito: {nombre}")
    return registro

def list_records(sort_by="id"):
    """
    Lista los registros ordenados mediante el poder de lambda functions.
    """
    if len(registros) == 0:
        print("No hay registros almacenados.")
        return []

    # USO DE LAMBDA REAL: Ordenar un diccionario utilizando lambda
    # Basado en la clave dictada por el parámetro sort_by
    lista_ordenada = sorted(registros, key=lambda x: x.get(sort_by, x['id']))
    
    print(f"\nTotal de registros ({len(registros)}) - [Ordenamiento por: {sort_by}]:")
    print("-" * 65)
    for r in lista_ordenada:
        print(f"[{r['estado'].upper():^8}] | ID: {r['id']:<6} | Nombre: {r['nombre']:<15} | Edad: {r['edad']:>2} | Email: {r['email']}")
    print("-" * 65)
    return lista_ordenada

def search_record(termino):
    """
    Busca registros por coincidencia parcial usando List Comprehension.
    """
    termino = termino.lower()
    
    # USO DE LIST COMPREHENSION ACÁ: Filtrar registros en una sola línea elegante iterando todos los elementos
    resultados = [
        r for r in registros 
        if termino in r['nombre'].lower() or termino in r['email'].lower() or termino in r['id'].lower()
    ]
    
    return resultados

def update_record(id, datos_nuevos):
    """
    Actualiza datos y maneja el error de modificación o ID inválido.
    """
    if id not in ids_usados:
        raise KeyError(f"Operación cancelada: El ID buscado '{id}' no existe.")

    # Ubicamos cuál es el registro original
    idx = next((i for i, r in enumerate(registros) if r['id'] == id), None)
    if idx is None:
        raise ValueError("Error crítico en la base de datos de memoria.")
    
    registro_actual = registros[idx]
    
    # Clonamos y combinamos para poder validarlo todo primero antes de guardarlo en la estructura principal
    registro_actualizado = registro_actual.copy()
    registro_actualizado.update(datos_nuevos)
    registro_actualizado['id'] = id # Proteger el ID original evitando sobre-escritura 
    
    # Volvemos a apoyarnos en el validador
    errores = validar_registro(registro_actualizado)
    if errores:
        raise ValueError(f"Error de validación al momento de actualizar: {', '.join(errores)}")

    # Proteger el set de emails también si es que se ha modificado el correo
    nuevo_email = registro_actualizado['email']
    correo_previo = registro_actual['email']
    if nuevo_email != correo_previo and nuevo_email in emails_usados:
        raise ValueError(f"Error de actualización: el email '{nuevo_email}' ya lo emplea otro usuario.")

    if nuevo_email != correo_previo:
        emails_usados.remove(correo_previo)
        emails_usados.add(nuevo_email)
        
    registros[idx] = registro_actualizado
    file.save_data(registros)
    print(f"[OK] ID {id} se actualizó permanentemente.")
    return registro_actualizado

def delete_record(id):
    """
    Elimina registro, control de errores verificando existencia.
    """
    if id not in ids_usados:
        raise KeyError(f"Operación cancelada para borrar: El ID '{id}' no existe y no puede ser removido.")

    # Conseguir el objetivo y borrar su huella en todas las listas/sets
    meta = next((r for r in registros if r['id'] == id), None)
    
    if meta:
        registros.remove(meta)
        ids_usados.remove(id)
        emails_usados.remove(meta['email'])
        file.save_data(registros)
        print(f"[OK] Registro [{id}] eliminado de manera exitosa de los datos.")
        return True
    return False