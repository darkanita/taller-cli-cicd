import pytest
from app import saludar
 
def test_saludar():
    assert "Hola Ana" in saludar("Ana")
 
def test_nombre_vacio():
    with pytest.raises(ValueError):
        saludar("")
