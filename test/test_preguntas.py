import pytest
from assertpy import assert_that, add_extension

from importar import *
from opotests.pregunta import Pregunta
from opotests.dificultad import Dificultad

@pytest.fixture
def datos_pregunta():
    datos = importar_pregunta('test/preguntas.txt')
    return datos

@pytest.fixture
def pregunta():
    datos_pregunta = importar_pregunta('test/preguntas.txt')
    return Pregunta(datos_pregunta[0], datos_pregunta[1], datos_pregunta[2], datos_pregunta[3], datos_pregunta[4], datos_pregunta[5])

def test_estado_pregunta():
    """
    Test para comprobar que la pregunta tiene los atributos correctos
    """
    # Comprobamos que la pregunta no esta vacia
    # assert_that(pregunta).is_not_empty()
    datos = importar_pregunta('test/preguntas.txt')
    pregunta = Pregunta(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5])

    # Comprobamos que la pregunta tiene un id
    assert_that(pregunta.id).is_instance_of(int)
    assert_that(pregunta.id).is_not_none()

    # Comprobamos que la pregunta tiene un tema asignado
    assert_that(pregunta.tema).is_instance_of(str)
    assert_that(pregunta.tema).is_not_empty()

    # Comprobamos que la pregunta tiene respuestas
    test_respuestas(pregunta)

    # Comprobamos que la pregunta tiene una respuesta correcta
    test_respuesta_correcta(pregunta)

    # Comprobamos que la pregunta tiene una dificultad entre las posibles
    test_dificultad(pregunta)
    
def test_respuestas(pregunta):
    """
    Test para comprobar que la pregunta tiene respuestas
    """
    assert_that(pregunta.respuestas).is_not_empty()
    assert_that(pregunta.respuestas).is_instance_of(dict)

def test_respuesta_correcta(pregunta):
    """
    Test para comprobar que la pregunta tiene una respuesta correcta asignada entre las posibles
    """
    assert_that(pregunta.resp_correcta).esta_entre_las_claves(pregunta.respuestas)

def test_dificultad(pregunta):
    """
    Test para comprobar que la dificultad de una pregunta es una de las posibles
    """
    assert_that(pregunta.dificultad).is_in(Dificultad.Alto, Dificultad.Medio, Dificultad.Bajo)

def esta_entre_las_claves(self, diccionario):
    """
    Extension de assertpy para verificar si un valor esta entre las claves de un diccionario
    """
    esta = False
    for key in diccionario.keys():
        if self.val == key:
            esta = True
            break
    if esta == False:
        self.error(f'{self.val} no esta')

    return self

# Añadimos la extension
add_extension(esta_entre_las_claves)
