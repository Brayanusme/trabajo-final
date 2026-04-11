from typing import List, Dict, Any, Optional
from validate import validar_registro, ValidationError, RecordNotFoundError, DuplicateRecordError
import file

# Cargar registros iniciales y configurar nuestros sets para control rápido de duplicados
registros: List[Dict[str, Any]] = []
ids_usados: set = set()
emails_usados: set = set()

def load_initial_data() -> None:
    """Carga los datos iniciales. Útil para tests."""
    global registros, ids_usados, emails_usados
    registros = file.load_data()
    ids_usados = {r['id'] for r in registros}
    emails_usados = {r['email'] for r in registros}

# Llamamos a la carga inicial normal
load_initial_data()

def new_register(id: str, nombre: str, email: str, edad: int, estado: str = "activo") -> Dict[str, Any]:
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
    validar_registro(registro) # lanza ValidationError si falla

    # Revisar colisiones
    if id in ids_usados:
        raise DuplicateRecordError(f"Error: el ID '{id}' ya existe.")

    if email in emails_usados:
        raise DuplicateRecordError(f"Error: el email '{email}' ya está registrado.")

    registros.append(registro)
    ids_usados.add(id)
    emails_usados.add(email)
    
    file.save_data(registros)
    return registro

def list_records(sort_by: str = "id") -> List[Dict[str, Any]]:
    """
    Lista los registros ordenados mediante el poder de lambda functions.
    """
    if len(registros) == 0:
        return []

    # USO DE LAMBDA REAL: Ordenar un diccionario utilizando lambda
    # Basado en la clave dictada por el parámetro sort_by
    lista_ordenada = sorted(registros, key=lambda x: x.get(sort_by, x['id']))
    return lista_ordenada

def search_record(termino: str) -> List[Dict[str, Any]]:
    """
    Busca registros por coincidencia parcial usando List Comprehension.
    """
    termino = termino.lower()
    
    # USO DE LIST COMPREHENSION ACÁ: Filtrar registros en una sola línea elegante iterando todos los elementos
    resultados = [
        r for r in registros 
        if termino in str(r['nombre']).lower() or termino in str(r['email']).lower() or termino in str(r['id']).lower()
    ]
    
    return resultados

def update_record(id: str, datos_nuevos: Dict[str, Any]) -> Dict[str, Any]:
    """
    Actualiza datos y maneja el error de modificación o ID inválido.
    """
    if id not in ids_usados:
        raise RecordNotFoundError(f"Operación cancelada: El ID buscado '{id}' no existe.")

    # Ubicamos cuál es el registro original
    idx = next((i for i, r in enumerate(registros) if r['id'] == id), None)
    if idx is None:
        raise RecordNotFoundError("Error crítico en la base de datos de memoria.")
    
    registro_actual = registros[idx]
    
    # Clonamos y combinamos para poder validarlo todo primero antes de guardarlo en la estructura principal
    registro_actualizado = registro_actual.copy()
    registro_actualizado.update(datos_nuevos)
    registro_actualizado['id'] = id # Proteger el ID original evitando sobre-escritura 
    
    # Volvemos a apoyarnos en el validador
    validar_registro(registro_actualizado)

    # Proteger el set de emails también si es que se ha modificado el correo
    nuevo_email = registro_actualizado['email']
    correo_previo = registro_actual['email']
    if nuevo_email != correo_previo and nuevo_email in emails_usados:
        raise DuplicateRecordError(f"Error de actualización: el email '{nuevo_email}' ya lo emplea otro usuario.")

    if nuevo_email != correo_previo:
        emails_usados.remove(correo_previo)
        emails_usados.add(nuevo_email)
        
    registros[idx] = registro_actualizado
    file.save_data(registros)
    return registro_actualizado

def delete_record(id: str) -> bool:
    """
    Elimina registro, control de errores verificando existencia.
    """
    if id not in ids_usados:
        raise RecordNotFoundError(f"Operación cancelada para borrar: El ID '{id}' no existe y no puede ser removido.")

    # Conseguir el objetivo y borrar su huella en todas las listas/sets
    meta = next((r for r in registros if r['id'] == id), None)
    
    if meta:
        registros.remove(meta)
        ids_usados.remove(id)
        emails_usados.remove(meta['email'])
        file.save_data(registros)
        return True
    return False