try:
    f = open("archivo.txt", "r")

except FileNotFoundError:
    print("Error: el archivo no existe.")

except PermissionError:
    print("Error: no tienes permiso para abrir el archivo.")

else:
    lineas = 0
    for linea in f:
        lineas += 1
    print(f"El archivo tiene {lineas} líneas.")

finally:
    print("Proceso terminado.")