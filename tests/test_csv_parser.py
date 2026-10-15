import pytest
from src.csv_parser import parse_csv_line, csv_a_diccionarios, validar_csv, contar_filas, extraer_columna

def test_parse_csv_line_normal():
    # Arrange
    linea = "id,nombre,edad"
    # Act
    resultado = parse_csv_line(linea)
    # Assert
    assert resultado == ["id", "nombre", "edad"]

def test_parse_csv_line_con_comillas_internas():
    # Arrange
    linea = '1,"Perez, Juan",30'
    # Act
    resultado = parse_csv_line(linea)
    # Assert
    assert len(resultado) == 3
    assert resultado[1] == "Perez, Juan"








def test_csv_a_diccionarios_filas_incompletas():
    # Arrange
    contenido = "id,nombre,edad\n1,Juan,30\n2,Ana"
    # Act
    resultado = csv_a_diccionarios(contenido)
    # Assert
    assert "edad" in resultado[1]
    assert resultado[1]["edad"] == ""

def test_validar_csv_vacio_retorna_falso():
    # Arrange
    contenido = ""
    # Act
    resultado = validar_csv(contenido)
    # Assert
    assert resultado is False

def test_contar_filas_multiples():
    # Arrange
    contenido = "header\nfila1\nfila2"
    # Act
    resultado = contar_filas(contenido)
    # Assert
    assert resultado == 3
