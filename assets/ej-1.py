def calcular_promedio(entrada: str) -> float:
    numeros = []

    for parte in entrada.split(","):
        parte = parte.strip() 
        try:
            numero = int(parte)
            numeros.append(numero)
        except ValueError:
            print(f"  No quiero  '{parte}' no es un entero válido, se ignora.")

    if not numeros:
        raise ValueError("No hay números válidos para calcular el promedio.")

    promedio = sum(numeros) / len(numeros)
    return promedio

entrada = input("Ingresa enteros separados por comas: ")

try:
    resultado = calcular_promedio(entrada)
    print(f"\nPromedio: {resultado:.2f}")
except ValueError as e:
    print(f"\nNo quiero: {e}")