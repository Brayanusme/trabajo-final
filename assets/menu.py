import os
import sys
import subprocess

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError:
    # Fallback genérico si colorama no está en el entorno local de los assets
    class MockColor:
        def __getattr__(self, name): return ""
    Fore = Style = MockColor()

def limpiar_pantalla():
    """Limpia la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def obtener_ejercicios(directorio):
    """Obtiene y ordena la lista de scripts python omitiendo este menú."""
    archivos = [f for f in os.listdir(directorio) if f.endswith('.py') and f != os.path.basename(__file__)]
    archivos.sort()
    return archivos

def ejecutar_ejercicio(ruta_ejercicio):
    """Ejecuta el script de manera aislada utilizando un subproceso con el mismo intérprete."""
    limpiar_pantalla()
    print(Fore.CYAN + Style.BRIGHT + f"\n--- Ejecutando: {os.path.basename(ruta_ejercicio)} ---\n")
    try:
        # Llamar al script y esperar a que termine
        subprocess.run([sys.executable, ruta_ejercicio])
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\nEjecución cancelada por el usuario.")
    except Exception as e:
        print(Fore.RED + f"\nExcepción inesperada al ejecutar: {e}")
        
    print(Fore.CYAN + Style.BRIGHT + "\n" + "-"*50)
    input(Fore.YELLOW + "Presione Enter para volver al menú de ejercicios...")

def main():
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    
    while True:
        ejercicios = obtener_ejercicios(directorio_actual)
        
        limpiar_pantalla()
        print(Fore.GREEN + Style.BRIGHT + "\n=== MENÚ DE EJERCICIOS (ASSETS) ===")
        
        if not ejercicios:
            print(Fore.RED + "No se encontraron ejercicios (.py) en la carpeta.")
            input("Presione Enter para salir...")
            break

        for i, ej in enumerate(ejercicios, 1):
            print(Fore.YELLOW + f"{i}. " + Fore.WHITE + ej)
            
        print(Fore.RED + "0. " + Fore.WHITE + "Salir")
        print(Fore.GREEN + "=" * 35)
        
        opcion = input(Fore.CYAN + "\nSeleccione el número del ejercicio:  " + Style.RESET_ALL).strip()
        
        if opcion == '0':
            print(Fore.MAGENTA + "\nSaliendo del menú de ejercicios. ¡Adiós!")
            break
            
        if opcion.isdigit():
            idx = int(opcion) - 1
            if 0 <= idx < len(ejercicios):
                ruta_completa = os.path.join(directorio_actual, ejercicios[idx])
                ejecutar_ejercicio(ruta_completa)
            else:
                input(Fore.RED + "\nError: Opción fuera de rango. Presione Enter para reintentar...")
        else:
            input(Fore.RED + "\nError: Entrada inválida. Debe ingresar el número. Presione Enter para continuar...")

if __name__ == "__main__":
    main()
