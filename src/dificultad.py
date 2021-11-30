from enum import Enum, auto, unique

@unique
class Dificultad(Enum):
    """Clase para poder representar el atributo dificultad de la clase Pregunta"""
    Alto = auto()
    Medio = auto()
    Bajo = auto()
