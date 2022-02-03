from invoke import task, run

@task
def installpoetry(c):
    """
    Tarea para instalar el gestor de dependencias Poetry
    """
    print("Instalando el gestor de dependencias...")
    run("curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -")

@task
def installdeps(c):
    """
    Tarea para instalar las dependencias del proyecto
    """
    run("poetry install")

@task
def check(c):
    """
    Tarea para comprobar la sintaxis de los ficheros fuente.
    """
    print("Comprobando sintaxis de los ficheros...")
    run("pylint -E opotests")

@task
def test(c):
    """
    Tarea para comprobar el funcionamiento.
    """
    print("Ejecutando test a los ficheros fuente...")
