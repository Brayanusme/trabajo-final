import os
from colorama import init, Fore, Back, Style
import service

# Inicializar colorama para que los colores se reseteen automáticamente
init(autoreset=True)

def limpiar_pantalla():
    """Limpia la consola dependiendo del sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def leer_entero(mensaje, min_val=None, max_val=None):
    """Bucle para validar que el usuario ingrese un número entero."""
    while True:
        try:
            valor = input(mensaje)
            numero = int(valor)
            if min_val is not None and numero < min_val:
                print(Fore.RED + f"Error: El número debe ser mayor o igual a {min_val}.")
                continue
            if max_val is not None and numero > max_val:
                print(Fore.RED + f"Error: El número debe ser menor o igual a {max_val}.")
                continue
            return numero
        except ValueError:
            print(Fore.RED + "Error: Por favor, ingrese un número entero válido.")

def presionar_tecla():
    """Pausa la ejecución hasta que el usuario presione Enter."""
    input(Fore.YELLOW + "\nPresione Enter para continuar...")

def menu_crear():
    print(Fore.CYAN + "\n--- CREAR REGISTRO ---")
    id_usuario = input("Ingrese ID (ej. USR001): ").strip()
    nombre = input("Ingrese Nombre: ").strip()
    email = input("Ingrese Email: ").strip()
    edad = leer_entero("Ingrese Edad: ", min_val=0, max_val=150)
    
    estado_input = input("Ingrese Estado [activo/inactivo] (Enter para activo): ").strip().lower()
    estado = estado_input if estado_input in ['activo', 'inactivo'] else "activo"

    try:
        # Aquí se conecta con el módulo service (CRUD) para persistir
        service.new_register(id_usuario, nombre, email, edad, estado)
        print(Fore.GREEN + Style.BRIGHT + "[ÉXITO] Registro creado correctamente.")
    except Exception as e:
        print(Fore.RED + f"[ERROR] {e}")

def menu_listar():
    print(Fore.CYAN + "\n--- LISTAR REGISTROS ---")
    print("Opciones de ordenamiento:")
    print("1. Por ID")
    print("2. Por Nombre")
    print("3. Por Edad")
    
    opc = input("Seleccione ordenamiento (Enter para default por ID): ").strip()
    
    sort_dict = {"1": "id", "2": "nombre", "3": "edad"}
    sort_by = sort_dict.get(opc, "id")
    
    print(Fore.CYAN + "\n--- RESULTADOS ---")
    service.list_records(sort_by=sort_by)

def menu_buscar():
    print(Fore.CYAN + "\n--- BUSCAR REGISTRO ---")
    termino = input("Ingrese término de búsqueda (nombre, email o ID): ").strip()
    
    # Conexión con el CRUD
    resultados = service.search_record(termino)
    
    if resultados:
        print(Fore.GREEN + f"\nSe encontraron {len(resultados)} resultados:")
        for r in resultados:
            print(Fore.WHITE + f" -> ID: {r['id']:<6} | Nombre: {r['nombre']:<15} | Email: {r['email']} | Estado: {r['estado']}")
    else:
        print(Fore.YELLOW + "No se encontraron resultados para su búsqueda.")

def menu_editar():
    print(Fore.CYAN + "\n--- EDITAR REGISTRO ---")
    id_usuario = input("Ingrese el ID del registro a editar: ").strip()
    
    print(Fore.YELLOW + "Deje en blanco los campos que NO desea modificar.")
    nombre = input("Nuevo Nombre: ").strip()
    email = input("Nuevo Email: ").strip()
    edad_str = input("Nueva Edad: ").strip()
    estado = input("Nuevo Estado [activo/inactivo]: ").strip().lower()
    
    datos_nuevos = {}
    if nombre: datos_nuevos['nombre'] = nombre
    if email: datos_nuevos['email'] = email
    if edad_str:
        try:
            datos_nuevos['edad'] = int(edad_str)
        except ValueError:
            print(Fore.RED + "Error: La edad proporcionada no es válida. No se modificará la edad.")
    if estado in ['activo', 'inactivo']: 
        datos_nuevos['estado'] = estado

    if not datos_nuevos:
        print(Fore.YELLOW + "No se ingresaron datos nuevos. Operación cancelada.")
        return

    try:
        # Conexión con el CRUD
        service.update_record(id_usuario, datos_nuevos)
        print(Fore.GREEN + Style.BRIGHT + "[ÉXITO] Registro actualizado correctamente.")
    except Exception as e:
        print(Fore.RED + f"[ERROR] {e}")

def menu_eliminar():
    print(Fore.CYAN + "\n--- ELIMINAR REGISTRO ---")
    id_usuario = input("Ingrese el ID del registro a eliminar: ").strip()
    
    confirmacion = input(Fore.YELLOW + f"¿Está seguro de eliminar el registro '{id_usuario}'? (s/n): ").strip().lower()
    if confirmacion == 's':
        try:
            # Conexión con el CRUD
            exito = service.delete_record(id_usuario)
            if exito:
                print(Fore.GREEN + Style.BRIGHT + "[ÉXITO] Registro eliminado de manera exitosa.")
            else:
                print(Fore.RED + "[ERROR] No se pudo encontrar el registro para eliminar.")
        except Exception as e:
            print(Fore.RED + f"[ERROR] {e}")
    else:
        print(Fore.YELLOW + "Operación cancelada.")

def iniciar_app():
    while True:
        limpiar_pantalla()
        print(Fore.CYAN + Style.BRIGHT + "\n=== SISTEMA DE GESTIÓN DE USUARIOS ===")
        print(Fore.YELLOW + "1." + Fore.WHITE + " Crear nuevo registro")
        print(Fore.YELLOW + "2." + Fore.WHITE + " Listar todos los registros")
        print(Fore.YELLOW + "3." + Fore.WHITE + " Buscar un registro")
        print(Fore.YELLOW + "4." + Fore.WHITE + " Editar un registro")
        print(Fore.YELLOW + "5." + Fore.WHITE + " Eliminar un registro")
        print(Fore.RED + "6." + Fore.WHITE + " Salir del sistema")
        print(Fore.CYAN + "=" * 38)
        
        opcion = input(Fore.GREEN + "\nSeleccione una opción (1-6): " + Style.RESET_ALL)
        
        if opcion == '1':
            menu_crear()
        elif opcion == '2':
            menu_listar()
        elif opcion == '3':
            menu_buscar()
        elif opcion == '4':
            menu_editar()
        elif opcion == '5':
            menu_eliminar()
        elif opcion == '6':
            print(Fore.MAGENTA + "\nSaliendo del sistema. ¡Hasta pronto!")
            break
        else:
            print(Fore.RED + "\nOpción inválida. Por favor, intente de nuevo.")
        
        presionar_tecla()

if __name__ == "__main__":
    iniciar_app()
