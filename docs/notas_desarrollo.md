# Notas de desarrollo :notebook_with_decorative_cover:

## Desarrollo de tests en base a los principios F.I.R.S.T.

### :rocket: Fast (Rápido)
En el testeo realizado en el proyecto se lleva a cabo un alto número de comprobaciones del código desarrollado en un tiempo razonable. En concreto, en este momento las comprobaciones se realizan ejecutando un total de **ocho** tests que tardan una media de ```0.708 segundos``` en llevarse a cabo.

### :point_up: Independent (Independiente)
Las comprobaciones realizadas en cada test no dependen del orden en el que estas se estén realizando, por lo que se cumple el principio de independencia.

### :repeat: Repeteable (Repetible)
Los tests diseñados no dependen de ningún tipo de sistema ni hardware concreto, se limitan a evaluar conceptos enfocados al código diseñado en base a la lógica de negocio.

### :white_check_mark::arrow_right_hook: Self-validating (Autoevaluable)
Gracias a la elección del [*test runner*](justificacion_eleccion_framework_test.md), los resultados de los tests se evalúan y se muestran automáticamente, sin necesidad de tener que utilizar ficheros de resultados ni visualizar comprobaciones de error tras la ejecución de estos.

### :alarm_clock: Timely (Oportuno)
El desarrollo del proyecto se sitúa en el [milestone 1](https://github.com/edusegrich/OpoTests/milestone/2). Los tests relativos al PMV de dicho milestone se encuentran implementados en [test](../test/).
