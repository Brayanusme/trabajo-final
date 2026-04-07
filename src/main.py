import service

def demo():
    print("=== DEMOSTRACIÓN DE CRUD COMPLETO ===")
    
    # Listar antes que todo
    service.list_records()
    
    print("\n[1] TEST: C - Crear y Validar los Datos iniciales ")
    try:
        service.new_register("USR001", "Ana Gómez", "ana@mail.com", 29, "activo")
    except Exception as e:
        print(f"(Aviso) {e}")

    try:
        service.new_register("USR002", "Carlos Rincón", "carlos@hotmail.com", 34, "activo")
    except Exception as e:
        print(f"(Aviso) {e}")

    try:
        service.new_register("USR003", "Laura Martínez", "laura@gmail.com", 22, "inactivo")
    except Exception as e:
        print(f"(Aviso) {e}")

    print("\n--- CASOS DE ERROR ---")
    try:
        service.new_register("USR001", "Impostor", "falso@mail.com", 30)
    except Exception as e:
        print(f"Error esperado atrapado: {e}")

    try:
        service.new_register("USR004", "El Fallido", "sin-arroba.com", 30)
    except Exception as e:
        print(f"Error esperado atrapado: {e}")

    
    print("\n[2] TEST: R - Leer usando Lambda en sort ")
    service.list_records(sort_by="edad")

    
    print("\n[3] TEST: Búsqueda usando List Comprehension ")
    busqueda = service.search_record("laura")
    print("Resultados de buscar 'laura':")
    for b in busqueda:
        print(f"  > ID: {b['id']} | Email: {b['email']}")
        

    print("\n[4] TEST: U - Actualizar y Manejar Errores de Actualización ")
    try:
        # Pensemos que Laura cumplió años y la pusimos activa
        service.update_record("USR003", {"edad": 23, "estado": "activo"})
    except Exception as e:
        print(e)
        
    print("\n--- Intentando modificar ID Inexistente ---")
    try:
        service.update_record("USR999", {"edad": 50})
    except Exception as e:
        print(f"Error esperado atrapado: {e}")

        
    print("\n[5] TEST: D - Eliminar ")
    try: # Borramos a la persona 1
        service.delete_record("USR001")
    except Exception as e:
        print(e)

    print("\n--- Intentando Borrar ID Inexistente ---")
    try:
        service.delete_record("USR999")
    except Exception as e:
        print(f"Error esperado atrapado: {e}")

        
    print("\n[Opcional] TEST FINAL: Persistencia Completa mostrada")
    # Este array debió quedarse sin USR001, con USR003 activo, organizado aquí alfabéticamente
    service.list_records(sort_by="nombre")

if __name__ == "__main__":
    # Limpiamos el archivo o no, de todas formas el try-except protegerá 
    # de intentar crear id duplicados si los datos sobrevivieron ejecuciones previas.
    demo()