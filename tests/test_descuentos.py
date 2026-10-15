import pytest
from src.descuentos import aplicar_descuento, calcular_descuento, calcular_precio_final, descuento_apilado, descuento_por_volumen, descuento_cumulativo

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


def test_aplicar_descuento_precio_negativo_lanza_error():
    # Arrange
    precio, porcentaje = -50, 10
    # Act & Assert
    with pytest.raises(ValueError):
        aplicar_descuento(precio, porcentaje)

def test_calcular_descuento_normal():
    # Arrange
    precio, porcentaje = 200, 15
    # Act
    resultado = calcular_descuento(precio, porcentaje)
    # Assert
    assert resultado == 30

def test_descuento_cumulativo_normal():
    # Arrange
    precio = 100
    descuentos = [10, 10] # 100 -> 90 -> 81
    # Act
    resultado = descuento_cumulativo(precio, descuentos)
    # Assert
    assert resultado == 81

def test_descuento_por_volumen_cantidades_menores():
    # Arrange
    precio_unitario = 10
    # Act
    res_15 = descuento_por_volumen(15, precio_unitario) # 5% desc
    res_5 = descuento_por_volumen(5, precio_unitario)   # 0% desc
    # Assert
    assert res_15 == 142.5
    assert res_5 == 50

def test_calcular_precio_final_valores_invalidos():
    # Arrange, Act & Assert: Cubrir los raise ValueError
    with pytest.raises(ValueError):
        calcular_precio_final(-100, 19, 10)  # precio negativo
    with pytest.raises(ValueError):
        calcular_precio_final(100, -19, 10)  # impuesto negativo
    with pytest.raises(ValueError):
        calcular_precio_final(100, 19, 150)  # descuento > 100

def test_descuento_por_volumen_rangos_medios():
    # Arrange & Act: Cubrir las ramas de 50 y 20 unidades
    res_50 = descuento_por_volumen(50, 10) # 15% desc
    res_20 = descuento_por_volumen(20, 10) # 10% desc
    # Assert
    assert res_50 == 425
    assert res_20 == 180

def test_descuento_cumulativo_valores_invalidos():
    with pytest.raises(ValueError):
        descuento_cumulativo(-100, [10])
    with pytest.raises(ValueError):
        descuento_cumulativo(100, [150])
