# Notas de desarrollo :notebook_with_decorative_cover:

## Desarrollo de tests en base a los principios F.I.R.S.T.

### :rocket: Fast (Rápido)
En el testeo realizado en el proyecto se lleva a cabo un alto número de comprobaciones del código desarrollado en un tiempo razonable.

Los test realizan comprobaciones  livianas pero de gran relevancia para la lógica de negocio, lo que contribuye a la rapidez de su ejecución. Además, el uso de los fixtures creados en ```conftest.py``` aporta eficiencia y reducción de tiempo de ejecución a la hora de realizar las comprobaciones ya que estos son objetos creados pre-ejecución (fase de *setup*) y compartidos por todos los tests.

En concreto, en este momento las comprobaciones se realizan ejecutando un total de **siete** tests que tardan una media de ```0.73 segundos``` en llevarse a cabo.

### :point_up: Isolated / Independent (Aislado / Independiente)
Las comprobaciones realizadas en cada test no dependen del orden en el que estas se estén realizando, por lo que se cumple el principio de independencia.

Por ejemplo, en nuestro caso, comprobar que el examen de una oposición tenga preguntas de todos los temas relativos a dicha oposición no influye en que una oposición tenga un título, por lo que ambas comprobaciones se pueden realizar sin importar el orden en el que se hagan.

### :repeat: Repeteable (Repetible)
Los tests diseñados no dependen de ningún tipo de sistema ni hardware concreto, se limitan a evaluar conceptos enfocados al código diseñado en base a la lógica de negocio.

### :white_check_mark::arrow_right_hook: Self-validating (Autoevaluable)
Gracias a la elección del [*test runner*](justificacion_eleccion_framework_test.md), los resultados de los tests se evalúan y se muestran automáticamente, sin necesidad de tener que utilizar ficheros de resultados ni visualizar comprobaciones de error tras la ejecución de estos.

### :alarm_clock: Timely (Oportuno)
El desarrollo del proyecto se sitúa en el [milestone 2.5](https://github.com/edusegrich/OpoTests/milestone/6). Los tests relativos al PMV de dicho milestone se encuentran implementados en [test](../test/). Estos tests se basan en garantizar la lógica de negocio básica del proyecto: *generar exámenes tipo tests de oposiciones* ([HU1](https://github.com/edusegrich/OpoTests/issues/3))
