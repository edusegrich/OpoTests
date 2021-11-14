class Tema:
    """
    Clase utilizada para representar un Tema de una Oposicion

    ...

    Attributes
    ----------
    titulo : str
        titulo del tema que servirá como identificador
    """

    def __init__(self, titulo):
        self.__titulo = titulo
    
    @property
    def titulo(self):
        """Devuelve el titulo del Tema"""
        return self.__titulo
