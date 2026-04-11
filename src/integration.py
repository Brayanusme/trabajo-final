"""
Módulo de integración con librerías externas (Pandas).
Se emplea para un manejo avanzado de datos, generación de reportes y exportación.
"""
from typing import Any, Tuple, Optional
import pandas as pd
import service
import file
import os

def generar_reporte(*args: Any, **kwargs: Any) -> Tuple[bool, Optional[str], Optional[str], Optional[str]]:
    """
    Función genérica utilizando parámetros dinámicos (*args y **kwargs)
    para analizar, filtrar y exportar los registros a un formato CSV.
    
    :param args: Parámetros posicionales opcionales; se utilizan para las
                 columnas sobre las cuales aplicar un ordenamiento (ej. 'edad', 'nombre').
    :param kwargs: Filtros en formato clave-valor (ej. estado='activo', id='USR001').
    :return: (exito, reporte_str, estadisticas_str, output_path)
    """
    registros = service.registros
    
    if not registros:
        return False, "No hay registros almacenados para procesar.", None, None
        
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
        return False, "Atención: No hay registros que coincidan con los filtros aplicados.", None, None
        
    # Mostrar resultados en la consola utilizando utilidades de Pandas (Generar un "Reporte")
    reporte_str = "\n" + "="*20 + " REPORTE GENERADO CON PANDAS " + "="*20 + "\n"
    reporte_str += df.to_string(index=False) + "\n"
    reporte_str += "="*69
    
    # Calcular y mostrar algunas estadísticas si existe la columna de edad
    estadisticas_str = None
    if 'edad' in df.columns and pd.api.types.is_numeric_dtype(df['edad']):
        estadisticas_str = "\n--- ESTADÍSTICAS BÁSICAS DE EDAD ---\n"
        estadisticas_str += df['edad'].describe().round(2).to_string()
        
    # 3. Exportar resultados a un archivo CSV
    output_path = os.path.join(file.BASE_DIR, "data", "reporte_usuarios.csv")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False, encoding='utf-8')
    
    return True, reporte_str, estadisticas_str, output_path
