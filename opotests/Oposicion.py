from datetime import date

class Oposicion:
    """
    Clase utilizada para representar una Oposicion

    ...

    Attributes
    ----------
    titulo : str
        titulo de la oposición que servirá como identificador
    temas : list
        lista que contiene los temas que componen la oposición
    fecha : date
        fecha en la que tendrá lugar el examen de la oposición
    """

    def __init__(self, titulo, temas, fecha):
        self.__titulo = titulo
        self.__temas = temas
        self.__fecha = fecha
    
    @property
    def titulo(self):
        """Devuelve el titulo de la Oposición"""
        return self.__titulo

    def add_tema(self, tema):
        """Añade un tema al temario de la Oposición"""
        pass
