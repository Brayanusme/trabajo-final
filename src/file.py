import json
import os
from typing import List, Dict, Any

# Obtener la ruta absoluta de la carpeta del proyecto (padre de src/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
DATA_PATH = os.path.join(DATA_DIR, "registros.json")

def load_data() -> List[Dict[str, Any]]:
    """Carga los registros desde el archivo JSON si existe. Maneja asegurando su existencia."""
    try:
        if not os.path.exists(DATA_PATH):
            return []
            
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
            
    except json.JSONDecodeError:
        print("Error: El archivo JSON de registros está corrupto o vacío. Se iniciará una lista nueva.")
        return []
    except Exception as e:
        print(f"Error al leer el archivo de registros: {e}")
        return []

def save_data(data: List[Dict[str, Any]]) -> None:
    """Guarda la lista de registros en el archivo JSON con manejo de errores."""
    try:
        # Asegurarse de que la carpeta data exista
        os.makedirs(DATA_DIR, exist_ok=True)
        
        with open(DATA_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
            
    except Exception as e:
        print(f"Error al escribir y guardar en el archivo: {e}")
