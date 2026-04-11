import sys
import os
import pytest

# Asegurar que src esté en el sys.path para importar los módulos directamente
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from validate import ValidationError, DuplicateRecordError, RecordNotFoundError
import service

@pytest.fixture(autouse=True)
def setup_teardown_layer(monkeypatch):
    """
    Mockeamos la capa de persistencia (file.save_data) para no crear archivos temporales,
    y limpiamos los diccionarios de la base de datos en memoria para que cada test 
    se corra en limpio.
    """
    monkeypatch.setattr("file.save_data", lambda x: None)
    
    # Limpiar estado
    service.registros.clear()
    service.ids_usados.clear()
    service.emails_usados.clear()
    yield

def test_new_register_success():
    """Prueba la creación exitosa de un registro."""
    record = service.new_register("USR100", "Carlos", "carlos@mail.com", 25, "activo")
    assert record["id"] == "USR100"
    assert record["nombre"] == "Carlos"
    assert len(service.registros) == 1
    assert "USR100" in service.ids_usados

def test_new_register_validation_error():
    """Prueba que falle si el email no es válido o está incompleto."""
    with pytest.raises(ValidationError) as exc_info:
        service.new_register("USR101", "Ana", "correo_invalido", 30)
    assert "formato válido" in str(exc_info.value)

def test_duplicate_record_error():
    """Prueba la protección contra identificadores duplicados."""
    service.new_register("USR102", "Luis", "luis@mail.com", 40)
    with pytest.raises(DuplicateRecordError) as exc_info:
        service.new_register("USR102", "Luis Clon", "luis2@mail.com", 40)
    assert "ya existe" in str(exc_info.value)

def test_search_and_list_record():
    """Verifica que el filtrado y ordenamiento operen correctamente."""
    service.new_register("USR103", "Zack", "zack@mail.com", 20)
    service.new_register("USR104", "Aaron", "aaron@mail.com", 22)
    
    # Búsqueda
    results = service.search_record("zack")
    assert len(results) == 1
    assert results[0]["id"] == "USR103"
    
    # Listado (ordenamiento alfabético invertido por nombre)
    ordered = service.list_records(sort_by="nombre")
    assert ordered[0]["nombre"] == "Aaron"
    assert ordered[1]["nombre"] == "Zack"

def test_delete_record():
    """Valida la eliminación segura y arroja error si el ID no existe."""
    service.new_register("USR105", "Maria", "maria@mail.com", 35)
    assert len(service.registros) == 1
    
    # Borrado exitoso
    res = service.delete_record("USR105")
    assert res is True
    assert len(service.registros) == 0
    
    # Fallo al intentar borrar inexistente
    with pytest.raises(RecordNotFoundError):
        service.delete_record("USR999")
