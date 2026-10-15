import pytest
from src.calculadora import sumar, dividir, raiz_cuadrada, minimo, calcular_perimetro_rectangulo, restar, multiplicar, potencia, promedio, maximo, calcular_area_rectangulo

def test_sumar_positivos():
    # Arrange
    a, b = 7, 5
    # Act
    resultado = sumar(a, b)
    # Assert
    assert resultado == 12

def test_dividir_por_cero_lanza_error():
    # Arrange & Act & Assert
    with pytest.raises(ValueError):
        dividir(10, 0)

def test_raiz_cuadrada_numero_negativo():
    # Arrange
    numero = -9
    # Act & Assert
    with pytest.raises(ValueError):
        raiz_cuadrada(numero)

def test_minimo_lista_desordenada():
    # Arrange
    lista = [5, 8, 3, 10]
    # Act
    resultado = minimo(lista)
    # Assert
    assert resultado == 3

def test_calcular_perimetro_rectangulo_valores_negativos():
    # Arrange
    base, altura = -4, 5
    # Act & Assert
    with pytest.raises(ValueError):
        calcular_perimetro_rectangulo(base, altura)

def test_restar_y_multiplicar():
    # Arrange
    a, b = 10, 5
    # Act
    res_resta = restar(a, b)
    res_mult = multiplicar(a, b)
    # Assert
    assert res_resta == 5
    assert res_mult == 50

def test_potencia_y_area():
    # Arrange
    base, exp = 2, 3
    # Act
    res_pot = potencia(base, exp)
    res_area = calcular_area_rectangulo(base, exp)
    # Assert
    assert res_pot == 8
    assert res_area == 6

def test_promedio_y_maximo_lista():
    # Arrange
    lista = [2, 4, 6]
    # Act
    res_prom = promedio(lista)
    res_max = maximo(lista)
    # Assert
    assert res_prom == 4
    assert res_max == 6

def test_promedio_lista_vacia_lanza_error():
    # Arrange & Act & Assert
    with pytest.raises(ValueError):
        promedio([])
