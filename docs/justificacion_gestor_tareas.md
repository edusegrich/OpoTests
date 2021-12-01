# Elección Gestor de Tareas Invoke
Existen diversas alternativas para controlar la gestión de tareas en proyectos desarrollados en Python. Algunas de ellas, dejando aparte al cásico *Makefile*, son [*pypyr*](https://pypyr.io/), [*doit*](https://pydoit.org/) o [*invoke*](https://www.pyinvoke.org/).

- **Pypyr** funciona a través de ficheros **.yaml** utilizando sintaxis de claves-valor con etiquetas como "name" o "steps".

- **Doit** utiliza funciones de Python escritas en un fichero denominado *dodo.py* que devuelven un diccionario con campos clave-valor que contienen las acciones de las tareas y los argumentos sobre los que ejecutarlas (ficheros, directorios, etc.).

- La última opción y la que se ha optado por utilizar es **Invoke**. Es una opción muy cómoda ya que se controla todo a partir de un fichero *tasks.py* donde se definen las tareas a automatizar como funciones de Python, lanzándolas a través de la orden *run* indicando como argumento el comando exacto que ejecutarías en una terminal. Además, existe una completa y extensa [documentación](https://docs.pyinvoke.org/en/stable/).
