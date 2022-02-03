# Marco de pruebas 📋

## Requisitos
Los requisitos que se esperan del marco de pruebas con el que realizar la tarea de testeo son:
1. Documentación actualizada y soporte activo.
2. Sencillez de uso.
3. Salida de resultados clara y descriptiva.
4. Uso de *fixtures*.
5. Uso de bibliotecas de aserciones externas.

## Opciones

Existen numerosas alternativas para la realización de testeo de código en proyectos de Python. Algunas de ellas son:

### **Unittest**
1. Cuenta con una [documentación oficial](https://docs.python.org/3.10/library/unittest.html) actualizada con cada versión y, actualmente, tiene en desarrollo la versión 3.11, en cuyo [repositorio de GitHub](https://github.com/python/cpython/tree/main/Lib/unittest) hay commits registrados recientemente. ✔️
2. Su uso es sencillo: los tests se definen en funciones que se agrupan en clases. ✔️
3. La información de salida no aporta mucho más que "número de tests pasados" y cuando hay errores, la información se muestra bastante abultada y poco organizada. :x:
4. Permite el uso de *fixtures*. ✔️
5. Permite el uso de bibliotecas de aserciones externas. ✔️

### **nose2**
1. Tiene [documentación oficial](https://docs.nose2.io/en/latest/) disponible con la última versión y también tiene un [repositorio de GitHub](https://github.com/nose-devs/nose2) en activo. ✔️
2. Su uso es como el de Unittest. ✔️
3. La salida es similar a la de Unittest. :x:
4. Permite el uso de *fixtures*. ✔️
5. Permite el uso de bibliotecas de aserciones externas. ✔️

### **Pytest**
1. Cuenta con una buena [documentación oficial](https://docs.pytest.org/en/6.2.x/) y [repo de GitHub](https://github.com/pytest-dev/pytest) activo. ✔️
2. Su uso es bastante sencillo: los test se definen en funciones dentro de ficheros cuyo nombre empiece por 'test'. Es bastante intuitivo y fácil de aprender y familiarizarse con su funcionamiento. ✔️
3. La salida es muy descriptiva: se aporta información sobre el porcentaje de tests que se han pasado y cuando hay errores se marcan de color rojo en la terminal, indicando claramente en qué partes del código el test no ha pasado, ayudando así a identificar rápidamente los errores. ✔️
4. Permite el uso de *fixtures*. ✔️
5. Permite el uso de bibliotecas de aserciones externas. ✔️

## Elección
Observando los criterios en base a cada una de las opciones, el ganador es **Pytest**.

En un principio, he decidido descartar **nose2** ya que en la [documentación oficial](https://docs.nose2.io/en/latest/#nose2-vs-pytest) recomienda el uso de otras alternativas (**Pytest** en concreto) para usuarios que están adentrándose en el mundo del desarrollo basado en tests.

La decisión era entre **Unittest** y **Pytest**. Ambas son buenas opciones, pero he considerado que el uso de **Pytest** es relativamente más sencillo que el de **Unittest** por el hecho de de no ser necesario crear una clase para los tests ni añadir el bloque final en el que se ejecuta ```unittest.main()```.

Además, la salida de los resultados (tanto de éxito como de errores) es bastante más clara y organizada en **Pytest**. 

El uso de *fixtures* también considero que es más sencillo en **Pytest**, pues para este basta con usar un decorador dedicado (```@pytest.fixture```). En cambio, en **Unittest** es necesario definir una función de ```SetUp``` para su construcción y una de ```TearDown``` para su destrucción.


# Biblioteca de Aserciones :no_entry_sign:
## Opciones
Respecto a la biblioteca de aserciones, para Python existe una gran oferta de posibilidades también:

- **Aserción nativa de Python**.
- **Unittest** dispone de funciones de aserción en la clase *TestCase* que provee, de modo que ello también puede ser utilizado como una librería de aserciones.
- **Assertpy**.
- **Grappa** es una biblioteca de aserciones para Python que intenta enfocar la tarea de testeo al lenguaje natural a través de su sintaxis.

## Elección
En primera instancia, he decidido descartar la opción de **Grappa** debido a que no me acaban de convencer los estilos de aserción ```expect``` y ```should```, y la manera en que se atienden las condiciones con ellos. 

En este punto nos quedan tres opciones: **funciones de Unittest**, **Aserción nativa de Python** y **Assertpy**.

La primera opción, [funciones de Unittest](https://docs.python.org/es/3.9/library/unittest.html#classes-and-functions), me parece que cuenta con pocas funciones para la aserción. Es cierto que tiene funciones como ```assertEqual(a, b)```, ```assertTrue(x)``` o ```assertIsNone(x)``` que pueden ser útiles pero no tiene una función, por ejemplo, para comprobar si un diccionario tiene cierta clave, cosa que nos podría hacer falta para comprobar si una pregunta tiene una respuesta correcta de entre las respuestas posibles y que sí tiene **Assertpy**. Es por ello que quizá esta opción se puede quedar corta y complicarnos la tarea de testeo.

La segunda opción nos puede "librar" de tener que importar una biblioteca de aserciones y hacer uso de los recursos con los que cuenta Python, algo que nos puede bastar perfectamente para lo que necesitamos. 

La tercera opción implica importar una biblioteca bastante completa, que cuenta con una [documentación](https://assertpy.github.io/docs.html) bastante detallada y cuyo uso de funciones y tratamiento de condiciones resulta ser muy intuitivo y cercano al lenguaje natural en cierta medida (lo justo y necesario, en mi opinión). Además, **Assertpy** permite la posibilidad de [añadir extensiones](https://assertpy.github.io/docs.html#assertpy.assertpy.add_extension), una opción muy interesante para personalizar el tratamiento de las condiciones en base a nuestra lógica de negocio.

Por estas razones, se ha optado por utilizar la tercera opción, **Assertpy**.
