import pytest
from assertpy import assert_that

from conftest import *
from opotests.pregunta import Pregunta
from opotests.dificultad import Dificultad


def test_estado_pregunta():
    """
    Test para comprobar que la pregunta tiene los atributos correctos
    """
    datos = importar_pregunta('test/preguntas.txt')
    pregunta = Pregunta(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5])

    # Comprobamos que la pregunta tiene un id
    assert_that(pregunta.id).is_instance_of(int)

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
    assert_that(pregunta.respuestas).contains_key(pregunta.resp_correcta)

def test_dificultad(pregunta):
    """
    Test para comprobar que la dificultad de una pregunta es una de las posibles
    """
    assert_that(pregunta.dificultad).is_in(Dificultad.Alto, Dificultad.Medio, Dificultad.Bajo)
