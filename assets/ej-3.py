while True:
    print("\n===== MENÚ =====")
    print("1. Dividir números")
    print("2. Abrir archivo")
    print("3. Salir")

    opcion = input("Elige una opción: ")

# 1
    if opcion == "1":
        try:
            a = float(input("Numerador: "))
            b = float(input("Denominador: "))
            resultado = a / b
            print(f"Resultado: {resultado}")

        except ValueError:
            print("No quiere: debes ingresar números válidos.")

        except ZeroDivisionError:
            print("No quiere: no se puede dividir entre cero.")

        except Exception as e:
            print(f"Error no previsto: {e}")

# 2
    elif opcion == "2":
        try:
            nombre = input("Nombre del archivo: ")
            f = open(nombre, "r")
            primera_linea = f.readline()
            f.close()
            print(f"Primera línea: {primera_linea}")

        except FileNotFoundError:
            print("No quiere: el archivo no existe.")

        except Exception as e:
            print(f"Error no previsto: {e}")

# 3
    elif opcion == "3":
        print("Y volo")
        break

    else:
        print("Opción inválida. Elige 1, 2 o 3.")