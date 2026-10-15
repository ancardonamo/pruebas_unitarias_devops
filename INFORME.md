# Informe: Taller — Análisis y Mejora de Pruebas Unitaria

* **Nombre:** Andrés Felipe Cardona Molina
* **Grupo:** 1
* **Fecha:** 15 de octubre de 2026

---

## Análisis por módulo

1. `calculadora.py` Este módulo provee operaciones matemáticas fundamentales y algunas utilidades para listas. Decidí enfocar las pruebas en valores límite y datos anómalos (ej. intentar sacar raíces de números negativos, listas desordenadas o con un solo elemento positivo) porque las funciones matemáticas suelen fallar en los bordes algebraicos o al no inicializar correctamente las variables acumuladoras.
2. `descuentos.py` Se encarga de aplicar reducciones porcentuales y cálculos de precios finales. Las pruebas se enfocaron en los límites de los porcentajes (menores a 0 o mayores a 100) y en la interacción entre diferentes reducciones. El objetivo era verificar que las operaciones matemáticas siguieran el orden correcto (descuentos antes de impuestos) y que la lógica del negocio no permitiera regalar dinero o generar saldos negativos al apilar promociones.
3. `csv_parser.py` Administra el procesamiento de texto en formato separado por comas. Las pruebas se enfocaron en la resiliencia del parser ante formatos irregulares muy comunes en archivos reales, como la asimetría en el número de columnas o la presencia de comillas dobles (",") para agrupar texto que incluye comas internas. 

---

## Tabla de bugs encontrados y corregidos

|    Módulo    |         Función         |        Entrada que lo revela            |                Resultado erróneo                     |         Resultado esperado                 |                             Corrección aplicada                                   |
| :----------- | :---------------------- | :-------------------------------------- | :--------------------------------------------------- | :----------------------------------------- | :-------------------------------------------------------------------------------- |
| `calculadora`| `raiz_cuadrada`         | `-9`                                    | Retornaba un número complejo.                        | Lanzar `ValueError`.                       | Se agregó: `if numero < 0: raise ValueError(...)` antes del cálculo.              |
| `calculadora`| `minimo`                | `[5, 8, 3, 10]`                         | Retornaba `0`.                                       | Retornar `3`.                              | Se cambió `min_val = 0` por `min_val = lista[0]`.                                 |
| `descuentos` | `calcular_precio_final` | `precio=100, impuesto=19, descuento=10` | Retornaba `109.0`. Calculaba el impuesto sobre $100. | Retornar `107.1`. Impuesto sobre $90.      | Se corrigió: `impuesto_monto = precio_con_descuento * (impuesto / 100)`.          |
| `descuentos` | `descuento_apilado`     | `precio=100, descuentos=[60, 50]`       | Permitía un descuento del 110%, retornando `-10.0`.  | Lanzar `ValueError`.                       | Se agregó validación: `if total_descuento > 100: raise ValueError(...)`.          |
| `csv_parser` | `parse_csv_line`        | `'1,"Perez, Juan",30'`                  | Dividía el texto en 4 partes (rompía el nombre).     | Dividir en 3 partes conservando el nombre. | Se reemplazó el uso de `.split(',')` por la librería estándar `csv` y `StringIO`. |
| `csv_parser` | `csv_a_diccionarios`    | `id,nombre,edad\n1,Juan,30\n2,Ana`      | Omitía la llave "edad" en el segundo diccionario.    | Crear llave "edad" con valor vacío `""`.   | Se iteró explícitamente sobre las cabeceras en lugar de iterar solo sobre los valores de la fila. |

---

## Cobertura

La cobertura superó exitosamente el 85% en los tres módulos trabajados tras agregar pruebas para cubrir caminos alternativos (condicionales `if/else`) y manejo de excepciones (`raise ValueError`).
El apartado de calculadora tiene 86%, el de csv_parser tiene 91% y el de descuentos tiene 87%. Esto quiere decir que esta fue la parte de código que se recorrió. No quiere decir que esta sea funcional y libre de bugs y que la que falta no lo sea, 
simplemente quiere decir que hay pruebas para ello que recorrieron ese porcentaje de codigo. Y dado que tenemos pruebas para estos casos y al haber hecho los pytests correspondientes, todos pasaron exitosamente,
podríamos asumir que está funcionando correctamente las pruebas hechas y que tenemos una cobertura de esos módulos en esos porcentajes dados. 

```text
---------- coverage: platform linux, python 3.13.5-final-0 -----------
Name                       Stmts   Miss  Cover   Missing
--------------------------------------------------------
src/__init__.py                0      0   100%
src/autenticacion.py          42     42     0%   6-77
src/calculadora.py            44      6    86%   22, 32, 43, 53, 63, 70
src/conversor.py              56     56     0%   6-94
src/csv_parser.py             77      7    91%   12, 35, 63, 72, 95, 108, 121
src/descuentos.py             60      8    87%   12, 20, 50, 53, 77, 91, 94, 102
src/fibonacci.py              42     42     0%   6-73
src/manipulador_texto.py      93     93     0%   6-156
src/procesador_texto.py       49     49     0%   6-84
src/utils.py                  53     53     0%   6-92
src/validador.py              64     64     0%   6-117
--------------------------------------------------------
TOTAL                        580    420    28%
```


## Reflexíon

En primer lugar, hablemos de la cobertura. De la cobertura podrían decirse distintas cosas. Entre estas, que el hecho de que la cobertura esté al 100% no garantiza que esta esté correctamente estructurada.
Con esto me refiero a que puedes obtener un porcentaje perfecto de cobertura sin que tengas uno de los siguientes valores: uno, que el resultado final tenga sentido y dos, que la fórmula matemática o la lógica que se implementó sea realmente la que pidió el cliente. 
Tal vez sí funciona, sí saca los datos que debería sacar, pero no era lo que me estaban pidiendo. Tampoco me avisa si tengo alguna funcionalidad que no se implementó, ya que no tiene la capacidad de ver la lógica del negocio.

De este taller pude deducir bastantes cosas. Lo primero es no conformarme con que el código funcione bien cuando los datos son ideales, sino forzar casos límites. 
Quizás a veces en un campo en el que debe ser solo un nombre, probar qué pasa si pongo caracteres inválidos, qué pasa si en valores que deben ser positivos meto valores negativos, meto decimales para valores que deben ser enteros y este tipo de cosas para cada función. 
Me parece bastante interesante el hecho de que cada función debe tener su propio análisis para saber que no se pueda romper de ninguna manera que no esté esperada. También comprendí que no necesariamente cuando una prueba sale en rojo quiere decir que algo esté mal, 
sino que es un hallazgo bastante interesante y que me permite a mí hallar una manera de solucionarlo cuando tal vez intentando forzar los casos límites, no lo hallé. Y también claro cuál es la importancia del DevOps en este aspecto, 
ya que interactúan simultáneamente el desarrollo del código, la automatización de las pruebas y la documentación, ya que lo tenemos en el mismo repositorio versionado y se pueden automatizar estas pruebas para que funcionen correctamente cada que se hace un desarrollo, 
lo cual me parece muy positivo y si se tuvieran todas las pruebas de todos los modelos, me permitiría a mí, como lo hemos trabajado en muchas clases, subir cambios teniendo la certeza de que todo va a funcionar bien.
