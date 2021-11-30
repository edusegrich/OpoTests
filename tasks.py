from invoke import task, run

@task
def check_syntax(c):
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
