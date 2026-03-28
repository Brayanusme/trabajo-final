import service
 
# --- Crear registros válidos ---
print("=== Creando registros ===")
service.crear_registro("USR001", "Ana Gómez", "ana@mail.com", 29)
service.crear_registro("USR002", "Carlos Rincón", "carlos@mail.com", 34)
service.crear_registro("USR003", "Laura Martínez", "laura@mail.com", 22)
 
# --- Listar todos ---
print("\n=== Lista de registros ===")
service.listar_registros()
 
# --- Intentar ID duplicado ---
print("\n=== Intentando ID duplicado ===")
service.crear_registro("USR001", "Otro Usuario", "otro@mail.com", 25)
 
# --- Intentar email duplicado ---
print("\n=== Intentando email duplicado ===")
service.crear_registro("USR999", "Copia Ana", "ana@mail.com", 30)
 
# --- Intentar datos inválidos ---
print("\n=== Intentando datos inválidos ===")
service.crear_registro("", "Sin ID", "sinid@mail.com", 20)
service.crear_registro("USR004", "", "sinnombre@mail.com", 20)
service.crear_registro("USR004", "Sin Email", "no-es-email", 20)
service.crear_registro("USR004", "Edad Mala", "edad@mail.com", -5)
 
# --- Lista final (solo los 3 válidos) ---
print("\n=== Lista final ===")
service.listar_registros()
 
# --- Ver sets en uso ---
print("\nIDs en uso:", service.ids_usados)
print("Emails en uso:", service.emails_usados)