from typing import Optional, Dict, Any, List

class ValidationError(Exception):
    """Excepción lanzada cuando los datos proporcionados no cumplen las reglas de negocio."""
    pass

class RecordNotFoundError(Exception):
    """Excepción lanzada cuando un registro buscado, a actualizar o eliminar no existe."""
    pass

class DuplicateRecordError(Exception):
    """Excepción lanzada cuando se intenta usar un ID o Email que ya están registrados."""
    pass

def validar_id(id_val: Optional[str]) -> Optional[str]:
    if not id_val:
        return "El ID no puede estar vacío"
    if len(str(id_val)) < 3:
        return "El ID debe tener mínimo 3 caracteres"
    return None

def validar_nombre(nombre: Optional[str]) -> Optional[str]:
    if not nombre:
        return "El nombre no puede estar vacío"
    if len(str(nombre)) < 2:
        return "El nombre debe tener mínimo 2 caracteres"
    return None

def validar_email(email: Optional[str]) -> Optional[str]:
    if not email:
        return "El email no puede estar vacío"
    if "@" not in str(email) or "." not in str(email):
        return "El email no tiene un formato válido"
    return None

def validar_edad(edad: Any) -> Optional[str]:
    if not isinstance(edad, int):
        return "La edad debe ser un número entero"
    if edad < 0 or edad > 100:
        return "La edad debe estar entre 0 y 100"
    return None

def validar_estado(estado: Optional[str]) -> Optional[str]:
    if not estado:
        return "El campo activo no puede estar vacío"
    if estado not in ["activo", "inactivo"]:
        return "El campo activo debe ser 'activo' o 'inactivo'"
    return None

def validar_registro(registro: Dict[str, Any]) -> None:
    """Valida un diccionario de registro. Lanza ValidationError si falla algo."""
    errores: List[str] = []

    error = validar_id(registro.get("id"))
    if error: errores.append(error)

    error = validar_nombre(registro.get("nombre"))
    if error: errores.append(error)

    error = validar_email(registro.get("email"))
    if error: errores.append(error)

    error = validar_edad(registro.get("edad"))
    if error: errores.append(error)

    error = validar_estado(registro.get("estado"))
    if error: errores.append(error)

    if errores:
        raise ValidationError(", ".join(errores))