#🧩 Ejercicio 6: Refactorizar procesamiento de ventas

def calculate_sale_total(venta: dict) -> float:
    """Calcula total de una venta con descuentos aplicados."""
    if venta.get("status") != "ok":
        raise ValueError(f"Venta inválida: {venta}")
    
    precio, cantidad = venta["price"], venta["quantity"]
    cliente = venta.get("customer", "regular")
    
    # Descuento: 10% si cantidad >= 10, +5% extra si es VIP
    descuento = (0.1 if cantidad >= 10 else 0.0) + (0.05 if cliente == "vip" else 0.0)
    
    return precio * cantidad * (1 - descuento)


def calculate_total(ventas: list) -> float:
    """Suma totales de ventas válidas (ignora inválidas)."""
    total = 0
    for venta in ventas:
        try:
            total += calculate_sale_total(venta)
        except ValueError:
            continue
    return total


def report_invalid_sales(ventas: list) -> None:
    """Reporta ventas inválidas."""
    invalidas = [v for v in ventas if v.get("status") != "ok"]
    if invalidas:
        print("VENTAS INVÁLIDAS:")
        for venta in invalidas:
            print(f"  - {venta}")
    else:
        print("No hay ventas inválidas.")


# =============================================================================
# PRUEBAS
# =============================================================================

if __name__ == "__main__":
    # Test 1: Suma correcta
    ventas = [
        {"status": "ok", "price": 100, "quantity": 1, "customer": "regular"},
        {"status": "ok", "price": 50, "quantity": 1, "customer": "regular"}
    ]
    assert calculate_total(ventas) == 150.0
    print("✓ Test 1: Suma correcta")
    
    # Test 2: Descuento por cantidad
    ventas = [{"status": "ok", "price": 100, "quantity": 10, "customer": "regular"}]
    assert calculate_total(ventas) == 900.0
    print("✓ Test 2: Descuento cantidad (10%)")
    
    # Test 3: Descuento VIP
    ventas = [{"status": "ok", "price": 100, "quantity": 10, "customer": "vip"}]
    assert calculate_total(ventas) == 850.0
    print("✓ Test 3: Descuento VIP (15% total)")
    
    # Test 4: Ignora inválidas
    ventas = [
        {"status": "ok", "price": 100, "quantity": 1, "customer": "regular"},
        {"status": "cancelled", "price": 50, "quantity": 1, "customer": "regular"},
        {"status": "ok", "price": 25, "quantity": 1, "customer": "regular"}
    ]
    assert calculate_total(ventas) == 125.0
    print("✓ Test 4: Ignora ventas inválidas")
    
    # Test 5: Reporte
    report_invalid_sales(ventas)
    
    print("\nTODOS LOS TESTS PASARON ✓")