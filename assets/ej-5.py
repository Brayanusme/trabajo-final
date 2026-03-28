has_min_length = lambda pwd: len(pwd) >= 8
has_no_spaces = lambda pwd: " " not in pwd
has_uppercase = lambda pwd: pwd != pwd.lower()
has_digits = lambda pwd: any(c.isdigit() for c in pwd)

def validate_password(password):
    """Valida contraseña. Retorna (es_válida, lista_de_errores)"""
    errors = []
    
    try:
        if not isinstance(password, str):
            raise TypeError("La contraseña debe ser texto")
        if not has_min_length(password):
            errors.append("Mínimo 8 caracteres")
        if not has_no_spaces(password):
            errors.append("No puede tener espacios")
        if not has_uppercase(password):
            errors.append("Debe tener mayúscula")
        if not has_digits(password):
            errors.append("Debe tener dígito")
        
        return (len(errors) == 0, errors)
    
    except TypeError as e:
        return (False, [str(e)])
    except Exception as e:
        return (False, [f"Error: {e}"])


# Pruebas
if __name__ == "__main__":
    try:
        password = input("Ingresa una contraseña para validar: ")
        is_valid, errors = validate_password(password)
        
        print(f"\nResultado: {'ES VÁLIDA' if is_valid else 'ES INVÁLIDA'}")
        if errors:
            print("Errores:")
            for error in errors:
                print(f"  • {error}")
        else:
            print("La contraseña es segura")
    
    except Exception as e:
        print(f"Error: {e}")
    if errors:
        print(f"Errores: {errors}")
    else:
        print("La contraseña es válida")