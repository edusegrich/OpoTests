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

def esta_entre_los_temas(self, lista):
    """
    Extension de assertpy para verificar si un tema (titulo) esta entre los temas de una lista
    """
    esta = False
    for tema in lista:
        if self.val == tema.titulo:
            esta = True
            break
    if esta == False:
        self.error(f'{self.val} no esta')

    return self

# Añadimos la extension
add_extension(esta_entre_los_temas)
