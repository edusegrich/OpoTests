# Repositorio de la asignatura Infraestructura Virtual ☁️ 📱
📝 Infraestructura Virtual  
🎓 Grado en Ingeniería Informática  
🏫 Universidad de Granada  
✒️ Eduardo Segura Richart  

# *OpoTests* 👨‍🎓 📑
### Problema 😟
Debido a la situación actual, hay una gran cantidad de estudiantes que se decantan por estudiar una oposición para labrarse un futuro. Muchas de las oposiciones que se convocan en España evalúan a los candidatos con exámenes de tipo test.

### Idea Principal 💡
La idea de este proyecto es hacer una aplicación que genere exámenes tipo test para las distintas oposiciones de manera que los opositores tengan una herramienta que les ayude a practicar y prepararse.  


## Instalación 🛠️ 💿 🖥️
A continuación se detallan los pasos a seguir para la instalación del proyecto.  

Lo primero que debes hacer es clonar el repositorio del proyecto. Para ello, abre una terminal y ejecuta el siguiente comando:  
```
git clone git@github.com:edusegrich/OpoTests
```

Una vez clonado el repositorio, debes instalar el **gestor de tareas** del proyecto: **Invoke**. Para ello, ejecuta la siguiente orden:  
```
pip install invoke
```  

El siguiente paso es  [instalar Poetry](https://python-poetry.org/docs/#installation), el **gestor de dependencias** del proyecto. Para instalarlo, sitúate en el directorio raíz del proyecto y ejecuta la orden para su instalación:
```
cd OpoTests
```
```
invoke installpoetry
```
  
Una vez instalado Poetry, lo último que tenemos que hacer es instalar las dependencias del proyecto ejecutando:  
```
invoke installdeps
```

En este punto el proyecto ya está listo para su uso.

## Guía de uso
Si quieres comprobar la sintaxis de los ficheros fuente, ejecuta el siguiente comando:
```
invoke check
```
  
Si quieres lanzar los tests, ejecuta el siguiente comando:
```
invoke test
```
Si quieres lanzar los tests dentro del contenedor de pruebas de `Docker` diseñado, tienes dos comandos:
1. Construcción del contenedor:
  ```
  invoke docker-build
  ```
2. Ejecución del contenedor:
  ```
  invoke docker-run
  ```

## Documentación 📋 📂
En el subdirectorio *docs* se puede consultar la [documentación](/docs) acerca del proyecto.

### Usuarios 🧑‍🤝‍🧑
Información acerca de los [usuarios](docs/tipos_de_usuario.md) y la función de cada uno de ellos en la aplicación.

### Hitos o Milestones 🚩
Se pueden consultar los [milestones](docs/milestones.md) del proyecto, así como el estado en el que se encuentra cada uno.

### Lenguaje del proyecto
Se puede consultar la [justificación](docs/justificacion_eleccion_lenguaje.md) de la elección del lenguaje del proyecto.

### Gestor de dependencias
Se puede consultar la justificación de la elección del [gestor de dependencias](docs/justificacion_gestor_dependencias.md) del proyecto.

### Gestor de tareas
Se puede consultar la justificación de la elección del [gestor de tareas](docs/justificacion_gestor_tareas.md) del proyecto.

### Imagen base de Docker :dvd:
Se puede consultar la justificación de la elección de la [image base de Docker](docs/justificacion_imagen_docker.md).

### Sistemas de Integración Continua
El análisis de sistemas de integración continua y la elección para el proyecto se puede consultar en las [notas de CI](/docs/notas_CI.md).
