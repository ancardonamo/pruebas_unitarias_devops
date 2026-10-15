import pytest
from src.descuentos import aplicar_descuento, calcular_descuento, calcular_precio_final, descuento_apilado, descuento_por_volumen

def test_aplicar_descuento_normal():
    # Arrange
    precio, porcentaje = 100, 20
    # Act
    resultado = aplicar_descuento(precio, porcentaje)
    # Assert
    assert resultado == 80

def test_calcular_descuento_porcentaje_invalido():
    # Arrange & Act & Assert
    with pytest.raises(ValueError):
        calcular_descuento(100, 150)

def test_calcular_precio_final_con_impuesto_y_descuento():
    # Arrange
    precio, impuesto, descuento = 100, 19, 10
    # Act
    resultado = calcular_precio_final(precio, impuesto, descuento)
    # Assert
    assert resultado == 107.1

def test_descuento_apilado_exceso_porcentaje():
    # Arrange
    precio = 100
    descuentos = [60, 50]
    # Act & Assert
    with pytest.raises(ValueError):
        descuento_apilado(precio, descuentos)

def test_descuento_por_volumen_limite_superior():
    # Arrange
    cantidad, precio_unitario = 100, 10
    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    # Assert
    assert resultado == 800
