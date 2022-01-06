import pytest
from assertpy import assert_that, add_extension
from datetime import date

from importar import *
from opotests.tema import Tema
from opotests.oposicion import Oposicion
from opotests.pregunta import Pregunta

@pytest.fixture
def pregunta():
    datos_pregunta = importar_pregunta('test/preguntas.txt')
    return Pregunta(datos_pregunta[0], datos_pregunta[1], datos_pregunta[2], datos_pregunta[3], datos_pregunta[4], datos_pregunta[5])

@pytest.fixture
def oposicion():
    datos_oposicion= importar_oposicion('test/oposiciones.txt')
    return Oposicion(datos_oposicion[0], datos_oposicion[1], datos_oposicion[2], datos_oposicion[3])

def test_estado_oposicion():
    """
    Test para comprobar que la oposicion tiene los atributos correctos
    """
    datos = importar_oposicion('test/oposiciones.txt')
    oposicion = Oposicion(datos[0], datos[1], datos[2], datos[3])

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

def test_pregunta_tema_oposicion():
    """
    Test para comprobar la relacion entre Pregunta, Tema y Oposicion
    """
    datos_pregunta = importar_pregunta('test/preguntas.txt')
    pregunta = Pregunta(datos_pregunta[0], datos_pregunta[1], datos_pregunta[2], datos_pregunta[3], datos_pregunta[4], datos_pregunta[5])

    datos_oposicion= importar_oposicion('test/oposiciones.txt')
    oposicion = Oposicion(datos_oposicion[0], datos_oposicion[1], datos_oposicion[2], datos_oposicion[3])


    assert_that(pregunta.tema).is_in(oposicion.temas)
    