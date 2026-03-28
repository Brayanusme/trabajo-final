op = input("Igrese operacion (suma, resta, multi, divi): ")
a = int(input("ingrese el primer numero: "))
b = int(input("ingrese el segundo numero: "))

def calc(a, b, op):
    ops = {
        "suma": lambda x, y: x + y,
        "resta": lambda x, y: x - y,
        "multi": lambda x, y: x * y,
        "divi": lambda x, y: "error" if y == 0 else x / y
    }
    func = ops.get(op)
    return func(a, b) if func else None
result = calc(a, b, op)
print("el resultado de la", op, "es", result)