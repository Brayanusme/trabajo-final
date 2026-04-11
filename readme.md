# 📂 Gestión de Usuarios - Proyecto Final Python

Un sistema interactivo por consola (CLI) desarrollado en Python para la administración temporal y persistente de usuarios mediante operaciones CRUD (Crear, Leer, Actualizar, Eliminar). Integra un robusto manejo de excepciones, reportes dinámicos con `pandas` y persistencia automática en formato JSON.

---

## 🚀 Características Principales

- **Gestión Completa (CRUD)**: Creación, filtrado, lectura, actualización y eliminación de registros de usuarios.
- **Reportes con Pandas**: Exporta datos analíticos y estadísticos a formato `.csv`.
- **Arquitectura Limpia**: Separación funcional entre vista (`menu.py`), lógica de negocio (`service.py`), almacenamiento (`file.py`) e integración externa (`integration.py`).
- **Validaciones Seguras**: Excepciones personalizadas para evitar IDs duplicados, correos inválidos o errores de rango.
- **Pruebas Unitarias Automáticas**: Suite de testing incorporada elaborada con `pytest`.

---

## 🛠️ Instalación y Configuración

Asegúrate de contar con Python 3.8 o superior instalado en tu sistema.

1. **Situarse en la raíz del proyecto**.
2. **Instalar las dependencias necesarias** ejecutando:
   ```bash
   pip install -r requirements.txt
   ```
   *(Dependencias principales: colorama, pandas, pytest)*

---

## 💻 Uso de la Aplicación

Para desplegar la interfaz de línea de comandos e interactuar con la base de datos principal, ejecuta:

```bash
python src/main.py
```

### Ejercicios Adicionales (Directorio Assets)
Se incluye un submenú independiente para acceder a los ejercicios aislados solicitados por la clase. Para revisarlos:
```bash
python assets/menu.py
```

---

## 🧪 Ejecución de Pruebas

El sistema cuenta con una batería de tests unitarios diseñados para respaldar la confiabilidad del servicio central sin alterar tus datos productivos reales. 

Para disparar las pruebas automáticas, corre:
```bash
pytest tests/
```

---

## 🧑‍💻 Autores
Proyecto desarrollado y mantenido por Brayan usme 