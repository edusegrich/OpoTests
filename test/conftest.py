import pytest
import sys

sys.path.append('./')
sys.path.append('./opotests/')
from opotests.examen import Examen
from opotests_utils import importar_oposicion, importar_pregunta, importar_preguntas
    
@pytest.fixture
def pregunta():
    """
    Objeto que representa una pregunta
    """
    pregunta = importar_pregunta('test/preguntas.txt')
    return pregunta

@pytest.fixture
def oposicion():
    """
    Objeto que representa una oposicion
    """
    oposicion = importar_oposicion('test/oposiciones.txt')
    return oposicion

@pytest.fixture
def examen(oposicion):
    """
    Objeto que representa un examen
    """
    preguntas = importar_preguntas('test/preguntas.txt')
    examen = Examen(1, oposicion, preguntas)
    return examen
