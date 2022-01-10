# Marco de pruebas 📋
Existen numerosas alternativas para la realización de testeo de código en proyectos de Python. Algunas de ellas son:

- **Unittest** es un módulo de Python para la realización de tests. Fue diseñado para trabajar con la librería estándar de Python. Con él es posible diseñar clases para tests y definir funciones en ellas.
- **nose2** está basado en *Unittest* y es, fundamentalmente, este con plugins añadidos que hacen la tarea de testeo más sencilla. En la [documentación oficial](https://docs.nose2.io/en/latest/#nose2-vs-pytest) recomienda el uso de *pytest* en lugar de su framework si eres un usuario principiante en el testeo de código en Python.
- **Pytest** es un framework de tests de propósito general pero especializado en testeo de APIs. Utiliza una sintaxis simple que contribuye a ejecuciones de tests eficientes. Cuenta con numerosos plugins y tiene soporte para la ejecución de tests en paralelo.

En un principio, he decidido descartar **nose2** ya que en la [documentación oficial](https://docs.nose2.io/en/latest/#nose2-vs-pytest) recomienda el uso de otros test runners (**Pytest** en concreto) para usuarios que están adentrándose en el mundo del desarrollo basado en tests.

La decisión era entre **Unittest** y **Pytest**. Ambas son buenas opciones, pero he considerado que el uso de **Pytest** es relativamente más sencillo que el de **Unittest** por el hecho de de no ser necesario crear una clase para los tests ni añadir el bloque final en el que se ejecuta ```unittest.main()```. 

A ello se añaden otros motivos de haber elegido **Pytest** como:
- Sencillez en su uso, pues para ello solamente es necesario importar el módulo correspondiente e implementar los tests como funciones.
- La salida de los errores es completa y justa para identificar de manera rápida el punto en el que el código no pasa el test.
- Cuenta con sintaxis específica para usar *fixtures*.
- A todo lo anterior, añadir que tiene una documentación oficial muy bien organizada y fácil de entender y hacer uso.

# Elección de la Biblioteca de Aserciones :no_entry_sign:
Respecto a la biblioteca de aserciones, para Python existe una gran oferta de posibilidades también:

- **Aserción nativa de Python**.
- **Unittest** también puede ser utilizado como una librería de aserciones.
- **Assertpy** 
- **Grappa** es una biblioteca de aserciones para Python que intenta enfocar la tarea de testeo al lenguaje natural a través de su sintaxis.

En primera instancia, he decidido descartar la opción de **Grappa** debido a que no me acaban de convencer los estilos de aserción ```expect``` y ```should```, y la manera en que se atienden las condiciones con ellos. 

De igual manera, la biblioteca de **Unittest** me parece que cuenta con un excesivo número de funciones que importar (```assertEqual(a, b)```, ```assertTrue(x)```, ```assertIsNone(x)```, etc.) y en mi opinión ello puede complicar la tarea de testeo basada en los principios FIRST.

En este punto nos quedan dos opciones: **Aserción nativa de Python** y **Assertpy**. 

La primera opción nos puede "librar" de tener que importar una biblioteca de aserciones y hacer uso de los recursos con los que cuenta Python, algo que nos puede bastar perfectamente para lo que necesitamos. 

La segunda opción implica importar una biblioteca bastante completa, que cuenta con una [documentación](https://assertpy.github.io/docs.html) bastante detallada y cuyo uso de funciones y tratamiento de condiciones resulta ser muy intuitivo y cercano al lenguaje natural en cierta medida (lo justo y necesario, en mi opinión). Además, **Asserpy** permite la posibilidad de [añadir extensiones](https://assertpy.github.io/docs.html#assertpy.assertpy.add_extension), una opción muy interesante para personalizar el tratamiento de las condiciones en base a nuestra lógica de negocio.

Por estas razones, se ha optado por utilizar la segunda opción, **Assertpy**.
