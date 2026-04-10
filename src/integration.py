"""
Módulo de integración con librerías externas (Pandas).
Se emplea para un manejo avanzado de datos, generación de reportes y exportación.
"""
import pandas as pd
import service
import file
import os

def generar_reporte(*args, **kwargs):
    """
    Función genérica utilizando parámetros dinámicos (*args y **kwargs)
    para analizar, filtrar y exportar los registros a un formato CSV.
    
    :param args: Parámetros posicionales opcionales; se utilizan para las
                 columnas sobre las cuales aplicar un ordenamiento (ej. 'edad', 'nombre').
    :param kwargs: Filtros en formato clave-valor (ej. estado='activo', id='USR001').
    """
    registros = service.registros
    
    if not registros:
        print("No hay registros almacenados para procesar.")
        return False
        
    # Integración con Pandas (librería externa) para crear el DataFrame
    df = pd.DataFrame(registros)
    
    # 1. Aplicación dinámica de filtros usando **kwargs
    for key, value in kwargs.items():
        if key in df.columns:
            if isinstance(value, str):
                # Filtrado insensible a mayúsculas/minúsculas
                df = df[df[key].str.lower() == value.lower()]
            else:
                # Filtrado exacto
                df = df[df[key] == value]

    # 2. Aplicación dinámica de ordenamiento usando *args
    columnas_orden = [col for col in args if col in df.columns]
    if columnas_orden:
        df = df.sort_values(by=columnas_orden)
        
    if df.empty:
        print("Atención: No hay registros que coincidan con los filtros aplicados.")
        return False
        
    # Mostrar resultados en la consola utilizando utilidades de Pandas (Generar un "Reporte")
    print("\n" + "="*20 + " REPORTE GENERADO CON PANDAS " + "="*20)
    print(df.to_string(index=False))
    print("="*69)
    
    # Calcular y mostrar algunas estadísticas si existe la columna de edad
    if 'edad' in df.columns and pd.api.types.is_numeric_dtype(df['edad']):
        print("\n--- ESTADÍSTICAS BÁSICAS DE EDAD ---")
        print(df['edad'].describe().round(2).to_string())
        
    # 3. Exportar resultados a un archivo CSV
    output_path = os.path.join(file.BASE_DIR, "data", "reporte_usuarios.csv")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False, encoding='utf-8')
    print(f"\n[ÉXITO] Los registros se han exportado exitosamente a CSV en:\n{output_path}")
    
    return True
