import pytest
from src.calculadora import sumar, dividir, raiz_cuadrada, minimo, calcular_perimetro_rectangulo

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
