from enum import Enum, unique

@unique
class Dificultad(Enum):
    """Clase para poder representar el atributo dificultad de la clase Pregunta"""
    Alto = 'Alto'
    Medio = 'Medio'
    Bajo = 'Bajo'
