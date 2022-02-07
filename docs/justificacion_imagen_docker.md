# Imagen base de Docker :dvd:
## Requisitos de la imagen
A la hora de buscar una imagen de docker como base para la construcción de nuestro contenedor de pruebas, hay una serie de requisitos que debe cumplir y que nos ayudarán a descartar unas opciones y decantarnos por otras.

La imagen debe cumplir los siguientes requisitos:

- **Imagen pequeña**, lo que nos facilitará la tarea de construcción y despliegue.
- La imagen debe ser **estable**, es decir, contar con el menor número de dependencias necesarias posible.
- **Extensible**, es decir, capaz de instalar dependencias que necesitemos para nuestro proyecto.
- **Compatible** con la versión de Python que necesitamos.

Con estas características debemos encontrar una imagen que nos permita construir y desplegar un contenedor para la realización de los tests *ligero* y con un *óptimo tiempo de ejecución*.

## Criterios de búsqueda
Para la búsqueda de opciones de imágenes base se han tenido en cuenta los siguientes criterios:
- Versiones de imágenes estables y actualizadas (etiqueta *latest*).
- Versión de Python 3.8 (como mínimo) ya que es la versión mínima con la que se trabaja en el proyecto.
- Distribuciones conocidas (Ubuntu 20.04, Ubuntu 18.04, CentOS...).

## Opciones de imágenes base
Una vez establecidos los requisitos que han de cumplirse y teniendo en cuenta los criterios de búsqueda nos encontramos con múltiples opciones. Podemos elegir entre dos opciones generales:

1. Imagen base de un SO al que le podemos instalar la versión de Python que queramos.
2. Imagen base oficial de Python para Docker.

Para la primera opción tenemos:

| Distribución          | Tamaño virtual  |
|-----------------------|----------|
|[alpine:3.15.0](https://github.com/docker-library/repo-info/blob/master/repos/alpine/local/latest.md)          | 5.6 MB   |
|[debian:bullseye (latest)](https://github.com/docker-library/repo-info/blob/master/repos/debian/local/latest.md)   | 124 MB   |
|[ubuntu:20.04](https://github.com/docker-library/repo-info/blob/master/repos/ubuntu/local/20.04.md)          | 73 MB    |
|[RHEL 8 (latest)](https://github.com/docker-library/repo-info/blob/master/repos/centos/local/latest.md)                 | 231.2 MB |

En cambio, también disponemos de imágenes de Docker oficiales de Python. Estas imágenes están construidas sobre un SO y tienen preinstaladas múltiples versiones de Python. Las alternativas son:

| Distribución               | Tamaño Virtual  |
|----------------------------|----------|
|[python:3.8.12-alpine3.15](https://github.com/docker-library/repo-info/blob/master/repos/python/local/3.8-alpine.md)    | 48 MB  |
|[python:3.8.12-bullseye](https://github.com/docker-library/repo-info/blob/master/repos/python/local/3.8.12-bullseye.md)      | 885 MB |
|[python:3.8.12-slim-bullseye](https://github.com/docker-library/repo-info/blob/master/repos/python/local/3.8.12-slim.md) | 121.6 MB |

La primera de ellas lleva una versión de **Alpine**, la segunda y la tercera cuentan con las versiones de **Debian** *bullseye* y *slim*, respectivamente.

## Elección imagen base de Docker
Tras haber realizado una búsqueda de las distintas posibilidades que ofrece Docker, se ha realizado una medición de los tiempos de construcción y ejecución de los tests del proyecto, así como el tamaño de las imágenes con cada opción tras instalar las dependencias necesarias. De esta manera y siguiendo los requisitos preestablecidos, se han descartado algunas imágenes candidatas antes de realizar con ellas la medición de los tiempos y tamaño experimentalmente.

Imágenes base como `RHEL 8 (latest)` o `python:3.8.12-bullseye` no cumplen con el primero de los requisitos (**Imagen pequeña**), por lo que han sido descartadas de antemano.

En todos los contenedores se ha instalado:
- **curl**: para la descarga de [*Poetry*](https://python-poetry.org/docs/#installation) por medio del método recomendado. Es posible también instalarlo con *pip* pero el proceso implica la instalación de otras dependencias que realmente no necesitamos y ello supondría una contradicción con respecto a los requisitos establecidos.
- **invoke**: para la gestión de tareas.
- **poetry**: para la gestión de dependencias.

En los contenedores no oficiales de python (primera opción) se ha instalado (además de lo anterior):
- **python3**: lenguaje del proyecto.
- **pip**: gestor de paquetes de python.

Teniendo en cuenta ello, los resultados se muestran en la siguiente tabla:

| Distribución                    | Tamaño      | Tiempo de construcción                              | Tiempo de ejecución |
|---------------------------------|-------------|-----------------------------------------------------|------------------|
|`python:3.8.12-alpine3.15`       | 255 MB      | *real* 1m53,873s *user* 0m0,053s *sys* 0m0,029s     | 0.314s
|`python:3.8.12-slim`             | 347 MB      | *real* 2m0,232s *user* 0m0,133s *sys* 0m0,087s      | 0.323s
|`ubuntu:20.04`                   | 621 MB      | *real* 3m44,788s *user* 0m0,175s *sys* 0m0,207s     | 0.490s
|`alpine:3.15.0`                  | No medido   | No medido                                           | No medido
|~~`python:3.8.12-bullseye`~~     | ~~1.09 GB~~ | ~~No medido~~                                       | ~~0.305s~~

Como podemos observar, la imagen `python:3.8.12-alpine3.15` es la opción que mejores resultados ha ofrecido, tanto en tamaño de la imagen creada como en los tiempos de construcción y de ejecución de los tests, superando ligeramente a la opción de `python:3.8.12-slim` en estos parámetros.

Las opciones con imágenes de SO generales probadas son `ubuntu:20.04` y `alpine:3.15.0`. La primera aumenta el tamaño de las versiones oficiales de Python casi el doble y no mejora el tiempo de construcción a pesar de que no registra un mal tiempo de ejecución de tests. No es una mala opción pero le penaliza, al tratarse de una distribución de propósito general, el hecho de contener dependencias que no nos son de utilidad para nuestro objetivo. Por tanto, los requisitos primero (**imagen pequeña**) y segundo (**minimización del número de dependencias**) se ven mermados. En cuanto a la segunda, se han tenido algunos problemas para desarrollar de manera cómoda sus pruebas. Es difícil instalar en Alpine una versión concreta de Python y no se ha conseguido llegar a añadirle la versión 3.8 (base sobre la que se ha desarrollado el proyecto). Además, la instalación de las dependencias de *Poetry* ha presentado problemas. La experiencia con esta opción ha resultado ser un tanto frustrante.

Por último y aunque no se ha considerado una alternativa real debido a su tamaño, se ha probado la imagen `python:3.8.12-bullseye`. El tiempo obtenido en la ejecución de tests ha sido el mejor de los obtenidos pero el tamaño de la imagen creada es exagerado (1.09 GB) y la idea es escoger una opción que muestre un equilibrio de todas las características que se esperan.

Una vez analizadas las alternativas, los resultados con cada una de ellas han sacado las siguientes conclusiones con respecto a los requisitos esperados:

| Distribución                           | Imagen pequeña | Mínimas dependencias | Extensible | Compatible |
|----------------------------------------|----------------|----------------------|------------|------------|
|`python:3.8.12-alpine3.15` :trophy:     |       ✔️        |           ✔️          |      ✔️     |     ✔️      |
|`python:3.8.12-slim`                    |       ✔️        |           ✔️          |      ✔️     |     ✔️      |
|`ubuntu:20.04`                          |      :x:       |          :x:         |      ✔️     |     ✔️      |
|`alpine:3.15.0`                         |       -        |           ✔️          |     :x:    |    :x:     |


Por tanto, la opción escogida es `python:3.8.12-alpine3.15`.