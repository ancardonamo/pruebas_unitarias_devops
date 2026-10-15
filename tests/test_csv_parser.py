import pytest
from src.csv_parser import parse_csv_line, csv_a_diccionarios, validar_csv, contar_filas, extraer_columna, filtrar_por_columna, contar_columnas

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

def test_extraer_columna_existente():
    # Arrange
    contenido = "id,nombre\n1,Ana\n2,Juan"
    # Act
    resultado = extraer_columna(contenido, 1)
    # Assert
    assert resultado == ["nombre", "Ana", "Juan"]

def test_filtrar_por_columna_coincidencia():
    # Arrange
    contenido = "id,rol\n1,admin\n2,user\n3,admin"
    # Act
    resultado = filtrar_por_columna(contenido, 1, "admin")
    # Assert
    assert len(resultado) == 2
    assert resultado[0] == ["1", "admin"]

def test_contar_columnas_normal():
    # Arrange
    contenido = "col1,col2,col3\ndato1,dato2,dato3"
    # Act
    resultado = contar_columnas(contenido)
    # Assert
    assert resultado == 3

def test_leer_funciones_con_csv_vacio():
    # Arrange
    contenido = ""
    # Act
    res_contar = contar_columnas(contenido)
    res_extraer = extraer_columna(contenido, 0)
    # Assert
    assert res_contar == 0
    assert res_extraer == []

def test_csv_a_diccionarios_sin_cabecera():
    # Arrange
    contenido = "1,Ana\n2,Juan"
    # Act
    resultado = csv_a_diccionarios(contenido, tiene_cabecera=False)
    # Assert: El código actual retorna [] si tiene_cabecera es False
    assert len(resultado) == 0

def test_validar_csv_filas_distinto_tamano():
    # Arrange
    contenido = "id,nombre\n1,Ana\n2" # La segunda fila tiene menos columnas
    # Act
    resultado = validar_csv(contenido)
    # Assert
    assert resultado is False

def test_extraer_columna_indice_fuera_de_rango():
    # Arrange
    contenido = "id,nombre\n1,Ana"
    # Act: Pedir una columna que no existe
    resultado = extraer_columna(contenido, 5)
    # Assert: Debe rellenar con strings vacíos
    assert resultado == ["", ""]
