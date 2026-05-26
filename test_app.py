import pytest
from app import saludar
from app import calcular_promedio
 
def test_saludar():
    assert "Hola Ana" in saludar("Ana")
 
def test_nombre_vacio():
    with pytest.raises(ValueError):
        saludar("")

def test_promedio():
    assert calcular_promedio([4.0, 5.0]) == 4.5
 
def test_promedio_vacio():
    with pytest.raises(ValueError):
        calcular_promedio([])
