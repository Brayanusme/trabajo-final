def validar_id(id):
    if id == "" or id == None:
        return "El ID no puede estar vacío"
    if len(id) < 3:
        return "El ID debe tener mínimo 3 caracteres"
    return None
 
def validar_nombre(nombre):
    if nombre == "" or nombre == None:
        return "El nombre no puede estar vacío"
    if len(nombre) < 2:
        return "El nombre debe tener mínimo 2 caracteres"
    return None
 
def validar_email(email):
    if email == "" or email == None:
        return "El email no puede estar vacío"
    if "@" not in email or "." not in email:
        return "El email no tiene un formato válido"
    return None

def validar_edad(edad):
    if type(edad) != int:
        return "La edad debe ser un número entero"
    if edad < 0 or edad > 100:
        return "La edad debe estar entre 0 y 100"
    return None
def validar_estado(estado):
    if estado == "" or estado is None:
        return "El campo activo no puede estar vacío"
    if estado not in ["activo", "inactivo"]:
        return "El campo activo debe ser 'activo' o 'inactivo'"
    return None
 
def validar_registro(registro):
    errores = []
 
    error = validar_id(registro.get("id"))
    if error:
        errores.append(error)
 
    error = validar_nombre(registro.get("nombre"))
    if error:
        errores.append(error)
 
    error = validar_email(registro.get("email"))
    if error:
        errores.append(error)
 
    error = validar_edad(registro.get("edad"))
    if error:
        errores.append(error)
    error = validar_estado(registro.get("estado"))
    if error:
        errores.append(error)
 
    return errores