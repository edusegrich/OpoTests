import pytest
from assertpy import assert_that
from datetime import date

from conftest import *
from opotests.tema import Tema
from opotests.grupo import Grupo

def test_estado_oposicion(oposicion):
    """
    Test para comprobar que la oposicion tiene los atributos correctos
    """
    # Comprobamos que la oposicion tiene un titulo
    assert_that(oposicion.titulo).is_instance_of(str)
    assert_that(oposicion.titulo).is_not_empty()

    # Comprobamos que la oposicion tiene un grupo
    test_grupo(oposicion)

    # Comprobamos que la oposicion tiene una lista de temas
    test_temas(oposicion)

    # Comprobamos que la oposicion tiene una fecha
    assert_that(oposicion.fecha).is_instance_of(date)

def test_grupo(oposicion):
    """
    Test para comprobar que el grupo de una oposicion es uno de los posibles
    """
    assert_that(oposicion.grupo).is_in(Grupo.A1, Grupo.A2, Grupo.B, Grupo.C1, Grupo.C2, Grupo.E)

def test_temas(oposicion):
    """
    Test para comprobar que la oposicion tiene una lista de objetos de tipo Tema
    """
    assert_that(oposicion.temas).is_not_empty()
    assert_that(oposicion.temas).is_instance_of(list)

    for tema in oposicion.temas:
        assert_that(tema).is_instance_of(Tema)

def test_pregunta_tema_oposicion(pregunta, oposicion):
    """
    Test para comprobar la relacion entre Pregunta, Tema y Oposicion
    """
    assert_that(oposicion.temas).contains(pregunta.tema)
