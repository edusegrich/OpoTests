from enum import Enum, auto, unique

@unique
class Grupo(Enum):
    """Clase para poder representar el atributo grupo de la clase Oposición"""
    A1 = auto()
    A2 = auto()
    B = auto()
    C1 = auto()
    C2 = auto()
    E = auto()
