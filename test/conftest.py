import pytest
from opotests.examen import Examen
from opotests_utils import importar_oposicion, importar_pregunta, importar_preguntas
from assertpy import add_extension
    
@pytest.fixture
def pregunta():
    pregunta = importar_pregunta('test/preguntas.txt')
    return pregunta

@pytest.fixture
def oposicion():
    oposicion = importar_oposicion('test/oposiciones.txt')
    return oposicion

@pytest.fixture
def examen():
    oposicion = importar_oposicion('test/oposiciones.txt')
    preguntas = importar_preguntas('test/preguntas.txt')
    examen = Examen(1, oposicion, preguntas)
    return examen
