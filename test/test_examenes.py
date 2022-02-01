import pytest
from assertpy import assert_that
from iteration_utilities import duplicates

from conftest import *
from opotests.pregunta import Pregunta
from opotests.oposicion import Oposicion

def test_estado_examen():
    """
    Test para comprobar que el examen tiene los atributos correctos
    """
    oposicion = importar_oposicion('test/oposiciones.txt')
    preguntas = importar_preguntas('test/preguntas.txt')
    examen = Examen(1, oposicion, preguntas)

    # Comprobamos que el examen tiene un id
    assert_that(examen.id).is_instance_of(int)

    # Comprobamos que el examen tiene una oposicion correspondiente
    assert_that(examen.oposicion).is_instance_of(Oposicion)

    # Comprobamos que el examen tiene una lista de preguntas
    test_preguntas(examen)

def test_temas_de_preguntas(examen):
    """
    Test para comprobar que no hay preguntas de temas que no se encuentren entre el temario de la oposicion a la 
    que corresponde el examen
    """
    temas = examen.oposicion.temas

    for pregunta in examen.preguntas:
        assert_that(pregunta.tema).is_in(temas)

def test_examen_completo(examen):
    """
    Test para comprobar que el examen es completo (hay preguntas de todos los temas de la oposicion que le corresponde)
    """
    temas = examen.oposicion.temas

    for pregunta in examen.preguntas:
        if pregunta.tema in temas:
            temas.remove(pregunta.tema)

    assert_that(temas).is_empty()

def test_preguntas_no_repetidas(examen):
    """
    Test para comprobar que no hay preguntas repetidas en el examen generado
    """
    assert_that(list(duplicates(examen.preguntas))).is_empty()
        
def test_preguntas(examen):
    """
    Test para comprobar que el examen tiene una lista de objetos de tipo Pregunta
    """
    assert_that(examen.preguntas).is_not_empty()
    assert_that(examen.preguntas).is_instance_of(list)

    for pregunta in examen.preguntas:
        assert_that(pregunta).is_instance_of(Pregunta)
